###############################################################################
# (c) Copyright 2021-2022 for the benefit of the LHCb Collaboration           #
#                                                                             #
# This software is distributed under the terms of the GNU General Public      #
# Licence version 3 (GPL Version 3), copied verbatim in the file "COPYING".   #
#                                                                             #
# In applying this licence, CERN does not waive the privileges and immunities #
# granted to it by virtue of its status as an Intergovernmental Organization  #
# or submit itself to any jurisdiction.                                       #
###############################################################################

import copy
import itertools
import logging
import os
from collections import defaultdict

from apd.ap_info import (
    SampleCollection,
    fetch_ap_info,
    iterable,
    load_ap_info,
    safe_casefold,
)
from apd.data_cache import DataCache

logger = logging.getLogger("apd")

APD_METADATA_CACHE_DIR = "APD_METADATA_CACHE_DIR"
APD_METADATA_LIFETIME = "APD_METADATA_LIFETIME"
APD_DATA_CACHE_DIR = "APD_DATA_CACHE_DIR"


def _validate_tags(tags, default_tags=None):
    """Method that checks the dictionary of tag names, values that should be used
    to filter the data accordingly.

     - Special cases are handled: tags "name" and "version" as well as "data" and "mc"
        (which are converted to a "config" value).
     - tag values cannot be None
     - tag values cannot be of type bytes
     - int tag values are converted to string
    """

    # Merging the default tags with the ones passed
    effective_tags = tags
    if default_tags:
        for t, v in default_tags.items():
            if t not in effective_tags:
                effective_tags[t] = v

    # Final dict that will be returned
    cleaned = {}

    # name and version are special tags in our case, we check their validity
    if "name" in effective_tags:
        raise Exception("name is not supported on AnalysisData objects")

    version = effective_tags.get("version", None)
    if version and iterable(version):
        raise Exception("version argument doesn't support iterables")

    # Special handling for the data and mc tags to avoid having to
    # use the config tag
    # The config tag is set according to the following table:
    #
    # | mc\data |    True    |    False   |      None      |
    # |:-------:|:----------:|:----------:|:--------------:|
    # |   True  | ValueError |     mc     |       mc       |
    # |  False  |    lhcb    | ValueError |      lhcb      |
    # |   None  |    lhcb    |     mc     | config not set |

    dataval = effective_tags.get("data", None)
    mcval = effective_tags.get("mc", None)
    config = None

    # We only set the config if one of the options data or mc was specified
    if dataval is None:
        # In this case we check whether mc has been specified and use that
        if mcval is not None:
            if mcval:
                config = "mc"
            else:
                config = "lhcb"
    # dataval has been explicitly set to true
    elif dataval:
        if mcval:
            raise ValueError("values of data= and mc= are inconsistent")
        config = "lhcb"
    # dataval has been explicitly set to false
    else:
        if mcval is not None and not mcval:
            # mcval explicitly set to False in contradiction with dataval
            raise ValueError("values of data= and mc= are inconsistent")
        config = "mc"

    # Check if config was set as well !
    if config:
        explicit_config = effective_tags.get("config", None)
        if explicit_config is not None:
            if explicit_config != config:
                raise ValueError("cannot specify data or mc as well as config")
        cleaned["config"] = config

    # Applying other checks
    for t, v in effective_tags.items():
        # Ignore those as we translated it to config already
        if t in ["data", "mc"]:
            continue
        if v is None:
            raise TypeError(f"{t} value is None")
        if isinstance(v, bytes):
            raise TypeError(f"{t} value is of type {type(v)}")
        if isinstance(v, int) and not isinstance(v, bool):
            cleaned[t] = str(v)
        else:
            cleaned[t] = v
    return cleaned


def sample_check(samples, tags):
    """Filter the SampleCollection and check that we have the
    samples that we expect"""

    # Fixing the dict to make sure each item is a list
    ltags = {}
    dimensions = tags.keys()
    for tag, value in tags.items():
        if not iterable(value):
            ltags[safe_casefold(tag)] = [safe_casefold(value)]
        else:
            ltags[safe_casefold(tag)] = [safe_casefold(v) for v in value]

    logger.debug("Checking samples for tags: %s", str(ltags))

    # Cardinal product of all the lists
    products = list(itertools.product(*ltags.values()))
    hist = {p: 0 for p in products}

    # Iterating on the samples an increasing the count
    for stags in samples.itertags():
        coordinates = tuple(safe_casefold(stags[d]) for d in dimensions)
        try:
            hist[coordinates] = hist[coordinates] + 1
        except KeyError as ke:
            raise KeyError(
                f"Encountered sample with tags {str(coordinates)} which does not match filtering criteria {str(dict(ltags))}"
            ) from ke

    # Now checking whether we have one entry per bin
    errors = []
    for coordinate, sample_count in hist.items():
        if sample_count != 1:
            logger.debug("Error %d samples for %s", sample_count, {str(coordinate)})
            errors.append((dict(zip(dimensions, coordinate)), sample_count))
    return errors


__analysis_map = {}


def get_analysis_data(
    working_group,
    analysis,
    metadata_cache=None,
    data_cache=None,
    api_url="https://lbap.app.cern.ch",
    ap_date=None,
    **kwargs,
):
    """Cache with the same process"""
    key = (working_group, analysis, ap_date)
    if key in __analysis_map:
        # As we keep an instance for each WG/Analysis, we need to copy and apply our own defaults
        ad = copy.deepcopy(__analysis_map[key])
        ad.data_cache = data_cache
        ad.default_tags = _validate_tags(kwargs)
        return ad
    ad = AnalysisData(
        working_group, analysis, metadata_cache, data_cache, api_url, ap_date, **kwargs
    )
    __analysis_map[key] = ad
    return ad


class AnalysisData:
    """Class allowing to access the metadata for a specific analysis.

    Default values for the tags to filter the data can be passed as argument to the contructor.
    Similarly for the required working group and analysis names.
    e.g. datasets = AnalysisData("b2oc", "b02dkpi", polarity="magdown")

    Invoking () returns a list of PFNs corresponding to the requested dataset
    Keyword arguments are interpreted as tags

    Combining all of the tags must give a unique dataset, else an error is raised.

    To get PFNs from multiple datasets lists can be passed as arguments.
    The single call
        datasets(eventtype="27163904", datatype=[2017, 2018], polarity=["magup", "magdown"])
    is equivalent to
        datasets(eventtype="27163904", datatype=2017, polarity="magup") +
        datasets(eventtype="27163904", datatype=2017, polarity="magdown") +
        datasets(eventtype="27163904", datatype=2018, polarity="magup") +
        datasets(eventtype="27163904", datatype=2018, polarity="magdown")
    """

    def __init__(
        self,
        working_group,
        analysis,
        metadata_cache=None,
        data_cache=None,
        api_url="https://lbap.app.cern.ch",
        ap_date=None,
        **kwargs,
    ):

        """
        Constructor that configures the can either fetch the data from the AP service or load from a local cache.

        Analysis Production tags can be specified as keyword arguments
        to specify the data to be analyzed.
        """
        self.working_group = working_group
        self.analysis = analysis
        # Tags is a list of tags that can be used to restrict the samples that will be used
        self.default_tags = _validate_tags(kwargs)

        #  self.samples is a SampleCollection filled in with the values
        metadata_cache = metadata_cache or os.environ.get(APD_METADATA_CACHE_DIR, "")
        need_clean_fetch = False
        if metadata_cache:
            if isinstance(metadata_cache, SampleCollection):
                logger.debug("Using SampleCollection passed to constructor")
                self.samples = metadata_cache
            else:
                logger.debug("Using metadata cache %s", metadata_cache)
                try:
                    self.samples, _ = load_ap_info(
                        metadata_cache, working_group, analysis, ap_date=ap_date
                    )
                except FileNotFoundError:
                    logger.debug(
                        "Could not find cache in %s, loading from remote",
                        metadata_cache,
                    )
                    need_clean_fetch = True
        else:
            logger.debug(
                "No cache set, fetching Analysis Production data from %s", api_url
            )
            need_clean_fetch = True

        if need_clean_fetch:
            self.samples = fetch_ap_info(
                working_group, analysis, None, api_url, ap_date=ap_date
            )

        self.available_tags = defaultdict(set)
        for sample in self.samples:
            for k, v in self.samples._sampleTags(sample).items():
                self.available_tags[k].add(v)

        # Now dealing with data cache
        data_cache = data_cache or os.environ.get(APD_DATA_CACHE_DIR, None)
        if isinstance(data_cache, str):
            self.data_cache = DataCache(data_cache)
        else:
            self.data_cache = data_cache

    def __call__(
        self,
        *,
        version=None,
        name=None,
        return_pfns=True,
        check_data=True,
        showmax=10,
        **tags,
    ):
        # pylint: disable-msg=too-many-locals
        """Main method that returns the dataset info.
        The normal behaviour is to return the PFNs for the samples but setting
        return_pfns to false returns the SampleCollection"""

        # Cannot mix data from 2 versions in the same dataset
        if not version:
            version = self.default_tags.get("version", None)

        if iterable(version):
            raise Exception("version argument doesn't support iterables")

        # Establishing the list of samples to run on
        samples = self.samples

        if name:
            if version:
                # No need to apply other tags, this specifies explicitly a specific dataset
                # We return it straight away
                logger.debug("Filtering for version/name %s/%s", name, version)
                samples = samples.filter("version", version)
                if len(samples) == 0:
                    raise KeyError(f"No version {version}")
                samples = samples.filter("name", name)
                if len(samples) == 0:
                    raise KeyError(f"No name {name}")
            else:
                # We check whether a version was specified in the default tags
                samples = samples.filter("name", name)
                if len(samples) != 1:
                    raise ValueError(
                        f"{len(samples)} matching {name}, should be exactly 1"
                    )
        else:
            # Merge the current tags with the default passed to the constructor
            # and check that they are consistent
            effective_tags = _validate_tags(tags, self.default_tags)

            if version:
                effective_tags["version"] = version

            for tagname, tagvalue in effective_tags.items():
                logger.debug("Filtering for %s = %s", tagname, tagvalue)

            # Applying the filters in one go
            samples = samples.filter(**effective_tags)
            logger.debug("Matched %d samples", len(samples))

            # Filter samples and check that we have what we expect
            if check_data:
                errors = sample_check(samples, effective_tags)
                if len(errors) > 0:
                    error_txt = f"{len(errors)} problem(s) found\n"
                    for etags, ecount in errors:
                        if etags:
                            error_txt += f"{str(etags)}: "
                        error_txt += f"{ecount} samples for the same configuration found, this is ambiguous:"
                        if ecount > 0:
                            error_txt += (
                                f"(only the first {showmax} samples printed)"
                                if (ecount > showmax)
                                else ""
                            )
                            match_list = [
                                str(m)
                                for m in itertools.islice(
                                    samples.filter(**etags).itertags(), 0, showmax
                                )
                            ]
                            error_txt += "".join(
                                ["\n" + " " * 5 + str(m) for m in match_list]
                            )
                    logger.debug("Error loading data: %s", error_txt)
                    raise ValueError("Error loading data: " + error_txt)

        if return_pfns:
            return self._transform_pfns(samples.PFNs())

        return samples

    def _transform_pfns(self, pfns):
        """Method to return PFNs, useful as it can be overriden in inheriting classes"""
        if not self.data_cache:
            return pfns
        return [self.data_cache(pfn) for pfn in pfns]

    def __str__(self):
        txt = f"AnalysisProductions: {self.working_group} / {self.analysis}\n"
        txt += str(self.samples)
        return txt

    def __repr__(self):
        return f"<AnalysisData: WG={self.analysis}, analysis={self.working_group}, n_samples={len(self.samples)}>"

    def summary(self, tags: list = None) -> dict:
        """prepares a summary of the Analysis Production info"""

        # Deal with the tags first
        tag_summary = {}
        if tags:
            for tag in tags:
                if tag in self.available_tags:
                    try:
                        values = sorted(self.available_tags[tag])
                    except TypeError as exc:
                        raise ValueError(
                            f"Could not sort the values for tag ({tag}). Please check that the values are sensible.\n"
                        ) from exc
                    values = list(self.available_tags[tag])
                    tag_summary[tag] = values
                else:
                    raise ValueError(
                        f"Requested tag ({tag}) not valid for the given production (wg: {self.working_group}, analysis: {self.analysis})!"
                    )
        else:
            tag_summary = dict(self.available_tags)

        summary = {}
        summary["tags"] = tag_summary

        # If we specify the tags to be list, we assume the general information should not be printed
        if not tags:
            summary["analysis"] = self.analysis
            summary["working_group"] = self.working_group
            summary["Number_of_files"] = self.samples.file_count()
            summary["Bytecount"] = self.samples.byte_count()

        return summary
