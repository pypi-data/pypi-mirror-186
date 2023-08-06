###############################################################################
# (c) Copyright 2021 CERN for the benefit of the LHCb Collaboration           #
#                                                                             #
# This software is distributed under the terms of the GNU General Public      #
# Licence version 3 (GPL Version 3), copied verbatim in the file "COPYING".   #
#                                                                             #
# In applying this licence, CERN does not waive the privileges and immunities #
# granted to it by virtue of its status as an Intergovernmental Organization  #
# or submit itself to any jurisdiction.                                       #
###############################################################################
#
# The command line tools use the click and click-log packages for easier development
#
import logging
import os
import sys
import tempfile

import click
import click_log
import requests

from .analysis_data import (
    APD_DATA_CACHE_DIR,
    APD_METADATA_CACHE_DIR,
    APD_METADATA_LIFETIME,
    get_analysis_data,
)
from .ap_info import InvalidCacheError, cache_ap_info, load_ap_info
from .authentication import get_auth_headers, logout
from .data_cache import DataCache
from .rich_console import console, error_console

logger = logging.getLogger("apd")
click_log.basic_config(logger)


common_help = """
Variables:

APD_METADATA_CACHE_DIR: Specify the location of the information cache,
    and reuse the cached information instead of reloading every time.

APD_METADATA_LIFETIME: Delay after which the cache should be considered
    as invalid and reloaded.

APD_DATA_CACHE_DIR: Specify the location of the location where a copy
    of the files will be kept.
"""


def common_docstr(sep="\n"):
    """
    Append the common help to all the functions docstring
    """

    def _decorator(func):
        func.__doc__ = sep.join([func.__doc__, common_help])
        return func

    return _decorator


def exception_handler(exception_type, exception, _):
    # All your trace are belong to us!
    # your format
    error_console.print(f"{exception_type.__name__}: {exception}")


sys.excepthook = exception_handler


def setup_cache(cache_dir, working_group, analysis, ap_date=None):
    """Utility function that checks whether the data for the Analysis
    is cached already and does it if needed."""
    if not cache_dir:
        cache_dir = "/tmp/apd_cache"
        logger.debug("Cache directory not set, using %s", cache_dir)
    try:
        lifetime = os.environ.get(APD_METADATA_LIFETIME, None)
        load_ap_info(
            cache_dir,
            working_group,
            analysis,
            ap_date=ap_date,
            maxlifetime=lifetime,
        )
    except FileNotFoundError:
        logger.debug(
            "Caching information for %s/%s to %s for time %s",
            working_group,
            analysis,
            cache_dir,
            ap_date,
        )
        cache_ap_info(cache_dir, working_group, analysis, ap_date=ap_date)
    except InvalidCacheError:
        logger.debug(
            "Invalid cache. reloading information for %s/%s to %s for time %s",
            working_group,
            analysis,
            cache_dir,
            ap_date,
        )
        cache_ap_info(cache_dir, working_group, analysis, ap_date=ap_date)
    return cache_dir


def _process_common_tags(eventtype, datatype, polarity, config, name, version):
    """Util to simplify the parsing of common tags"""
    filter_tags = {}
    if name is not None:
        filter_tags["name"] = name
    if version is not None:
        filter_tags["version"] = version
    if eventtype != ():
        filter_tags["eventtype"] = eventtype
    if datatype != ():
        filter_tags["datatype"] = datatype
    if polarity != ():
        filter_tags["polarity"] = polarity
    if config != ():
        filter_tags["config"] = config
    return filter_tags


@click.command()
def cmd_login():
    """Login to the Analysis Productions endpoint"""
    if "CI_JOB_JWT_V2" in os.environ and "LBAP_TOKENS_FILE" not in os.environ:
        _, token_file = tempfile.mkstemp(prefix="apd-", suffix=".json")
        os.environ["LBAP_TOKENS_FILE"] = token_file
        print(f"export LBAP_TOKENS_FILE={token_file}")
    try:
        r = requests.get(
            "https://lbap.app.cern.ch/user/",
            **get_auth_headers(),
            timeout=10,
        )
        r.raise_for_status()
        console.print(f"Login successful as {r.json()['username']}")
    except Exception:  # pylint: disable=broad-except
        # Ensure GitLab CI jobs exit if something goes wrong
        if "CI_JOB_JWT_V2" in os.environ:
            print("exit 42")
        raise


@click.command()
def cmd_logout():
    """Login to the Analysis Productions endpoint"""
    logout()


@click.command()
@click.argument("cache_dir")
@click.argument("working_group")
@click.argument("analysis")
@click.option("--date", default=None, help="analysis date in ISO 8601 format")
@click_log.simple_verbosity_option(logger)
def cmd_cache_ap_info(cache_dir, working_group, analysis, date):
    logger.debug(
        "Caching information for %s/%s to %s for time %s",
        working_group,
        analysis,
        cache_dir,
        date,
    )
    cache_ap_info(cache_dir, working_group, analysis, ap_date=date)


@click.command()
@click.argument("working_group")
@click.argument("analysis")
@click.option(
    "--cache_dir",
    default=os.environ.get(APD_METADATA_CACHE_DIR, None),
    help="Specify location of the cache for the analysis metadata",
)
@click.option("--tag", default=None, help="Tag to filter datasets", multiple=True)
@click.option(
    "--value",
    default=None,
    help="Tag value used if the name is specified",
    multiple=True,
)
@click.option(
    "--eventtype", default=None, help="eventtype to filter the datasets", multiple=True
)
@click.option(
    "--datatype", default=None, help="datatype to filter the datasets", multiple=True
)
@click.option(
    "--polarity", default=None, help="polarity to filter the datasets", multiple=True
)
@click.option(
    "--config", default=None, help="Config to use (e.g. lhcb or mc)", multiple=True
)
@click.option("--name", default=None, help="dataset name")
@click.option("--version", default=None, help="dataset version")
@click.option("--date", default=None, help="analysis date in ISO 8601 format")
@click_log.simple_verbosity_option(logger)
@common_docstr()
def cmd_list_pfns(
    working_group,
    analysis,
    cache_dir,
    tag,
    value,
    eventtype,
    datatype,
    polarity,
    config,
    name,
    version,
    date,
):
    """List the PFNs for the analysis, matching the tags specified.
    This command checks that the arguments are not ambiguous."""

    cache_dir = setup_cache(cache_dir, working_group, analysis, date)

    # Loading the data and filtering/displaying
    datasets = get_analysis_data(
        working_group, analysis, metadata_cache=cache_dir, ap_date=date
    )
    filter_tags = _process_common_tags(
        eventtype, datatype, polarity, config, name, version
    )
    filter_tags |= dict(zip(tag, value))
    for f in datasets(**filter_tags):
        click.echo(f)


@click.command()
@click.argument("working_group")
@click.argument("analysis")
@click.option(
    "--cache_dir",
    default=os.environ.get(APD_METADATA_CACHE_DIR, None),
    help="Specify location of the cache for the analysis metadata",
)
@click.option("--tag", default=None, help="Tag to filter datasets", multiple=True)
@click.option(
    "--value",
    default=None,
    help="Tag value used if the name is specified",
    multiple=True,
)
@click.option(
    "--eventtype", default=None, help="eventtype to filter the datasets", multiple=True
)
@click.option(
    "--datatype", default=None, help="datatype to filter the datasets", multiple=True
)
@click.option(
    "--polarity", default=None, help="polarity to filter the datasets", multiple=True
)
@click.option(
    "--config", default=None, help="Config to use (e.g. lhcb or mc)", multiple=True
)
@click.option("--name", default=None, help="dataset name")
@click.option("--version", default=None, help="dataset version")
@click.option("--date", default=None, help="analysis date in ISO 8601 format")
@click_log.simple_verbosity_option(logger)
@common_docstr()
def cmd_list_samples(
    working_group,
    analysis,
    cache_dir,
    tag,
    value,
    eventtype,
    datatype,
    polarity,
    config,
    name,
    version,
    date,
):
    """List the samples for the analysis, matching the tags specified.
    This command does not check whether the data set in unambiguous"""

    # Dealing with the cache
    cache_dir = setup_cache(cache_dir, working_group, analysis, date)

    # Loading the data and filtering/displaying
    datasets = get_analysis_data(
        working_group, analysis, metadata_cache=cache_dir, ap_date=date
    )
    filter_tags = filter_tags = _process_common_tags(
        eventtype, datatype, polarity, config, name, version
    )
    filter_tags |= dict(zip(tag, value))
    matching = datasets(check_data=False, return_pfns=False, **filter_tags)
    click.echo(matching)


@click.command()
@click.argument("working_group")
@click.argument("analysis")
@click.option(
    "--cache_dir",
    default=os.environ.get(APD_METADATA_CACHE_DIR, None),
    help="Specify location of the cache for the analysis metadata",
)
@click.option(
    "--tag",
    default=None,
    help="Tag for which the values should be listed",
    multiple=True,
)
@click.option("--date", default=None, help="analysis date in ISO 8601 format")
@click_log.simple_verbosity_option(logger)
@common_docstr()
def cmd_summary(
    working_group,
    analysis,
    cache_dir,
    tag,
    date,
):
    """Print a summary of the information available about the specified analysis."""
    # Dealing with the cache
    cache_dir = setup_cache(cache_dir, working_group, analysis, date)

    # Loading the dataset and displaying its summary
    datasets = get_analysis_data(
        working_group, analysis, metadata_cache=cache_dir, ap_date=date
    )
    datasets = get_analysis_data(
        working_group, analysis, metadata_cache=cache_dir, ap_date=date
    )
    datasets = get_analysis_data(
        working_group, analysis, metadata_cache=cache_dir, ap_date=date
    )
    console.print(datasets.summary(tag))


@click.command()
@click.argument("working_group")
@click.argument("analysis")
@click.option(
    "--cache_dir",
    default=os.environ.get(APD_METADATA_CACHE_DIR, None),
    help="Specify location of the cache for the analysis metadata",
)
@click.option(
    "--data_cache_dir",
    default=os.environ.get(APD_DATA_CACHE_DIR, None),
    help="Specify location of the cache for the analysis metadata",
)
@click.option(
    "-n",
    "--dry-run",
    type=bool,
    default=False,
    is_flag=True,
    help="Show which file should be copied instead of doing the actual copy",
)
@click.option("--tag", default=None, help="Tag to filter datasets", multiple=True)
@click.option(
    "--value",
    default=None,
    help="Tag value used if the name is specified",
    multiple=True,
)
@click.option(
    "--eventtype", default=None, help="eventtype to filter the datasets", multiple=True
)
@click.option(
    "--datatype", default=None, help="datatype to filter the datasets", multiple=True
)
@click.option(
    "--polarity", default=None, help="polarity to filter the datasets", multiple=True
)
@click.option("--name", default=None, help="dataset name")
@click.option("--version", default=None, help="dataset version")
@click.option("--date", default=None, help="analysis date in ISO 8601 format")
@click_log.simple_verbosity_option(logger)
@common_docstr()
def cmd_cache_pfns(
    working_group,
    analysis,
    cache_dir,
    data_cache_dir,
    dry_run,
    tag,
    value,
    eventtype,
    datatype,
    polarity,
    name,
    version,
    date,
):
    """List the PFNs for the analysis, matching the tags specified.
    This command checks that the arguments are not ambiguous."""
    # pylint: disable-msg=too-many-locals
    cache_dir = setup_cache(cache_dir, working_group, analysis, date)

    if not data_cache_dir:
        raise Exception("Please specify the location of the data cache")
    data_cache = DataCache(data_cache_dir)
    # Loading the data and filtering/displaying
    datasets = get_analysis_data(
        working_group, analysis, metadata_cache=cache_dir, ap_date=date
    )
    filter_tags = {}
    if name is not None:
        filter_tags["name"] = name
    if version is not None:
        filter_tags["version"] = version
    if eventtype != ():
        filter_tags["eventtype"] = eventtype
    if datatype != ():
        filter_tags["datatype"] = datatype
    if polarity != ():
        filter_tags["polarity"] = polarity
    filter_tags |= dict(zip(tag, value))

    for f in datasets(check_data=False, **filter_tags):
        local = data_cache.remote_to_local(f)
        if dry_run:
            print(str(f))
            if local.exists():
                click.echo(f"Already local for {f}: {str(local)}")
            click.echo(f"Would copy {f} to {data_cache.remote_to_local(f)}")
        else:
            if local.exists():
                click.echo(f"Local copy for {f} {str(local)} already present.")
            else:
                click.echo(f"Copying {f} to {data_cache.remote_to_local(f)}")
                data_cache.copy_locally(f)
