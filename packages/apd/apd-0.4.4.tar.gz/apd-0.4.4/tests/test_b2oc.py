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

import pytest

from apd import AnalysisData


@pytest.mark.parametrize("with_tokens", [[False], [True]])
def test_by_name(with_tokens, apd_cache, monkeypatch):
    if not with_tokens:
        monkeypatch.delenv("LBAP_TOKENS_FILE")
    datasets = AnalysisData("b2oc", "b02dkpi")

    pfns = datasets(version="v0r0p2518507", name="2018_15164022_magup")
    assert len(pfns) == 6

    pfns = datasets(version="v0r0p2970193", name="2018_15164022_magup")
    assert len(pfns) == 1 and "00145075_00000001" in pfns[0]

    with pytest.raises(Exception, match="version argument doesn't support iterables"):
        datasets(version=["v0r0p2518507", "v0r0p2970193"], name="2018_15164022_magup")

    with pytest.raises(Exception, match="version argument doesn't support iterables"):
        datasets(version={"v0r0p2518507", "v0r0p2970193"}, name="2018_15164022_magup")

    pfns = set(
        datasets(
            version="v0r0p2970193",
            name=["2018_15164022_magup", "2018_15164022_magdown"],
        )
    )

    if with_tokens:
        assert pfns == {
            "root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2018/B02DKPI.ROOT/00145075/0000/00145075_00000001_1.b02dkpi.root?xrd.wantprot=unix&authz=eos_token",
            "root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2018/B02DKPI.ROOT/00145077/0000/00145077_00000001_1.b02dkpi.root?xrd.wantprot=unix&authz=eos_token",
        }
    else:
        assert pfns == {
            "root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2018/B02DKPI.ROOT/00145075/0000/00145075_00000001_1.b02dkpi.root",
            "root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2018/B02DKPI.ROOT/00145077/0000/00145077_00000001_1.b02dkpi.root",
        }

    assert pfns == set(
        datasets(
            version="v0r0p2970193",
            name={"2018_15164022_magup", "2018_15164022_magdown"},
        )
    )


def test_defaults_version(apd_cache):
    datasets = AnalysisData("b2oc", "b02dkpi", version="v0r0p2518507")
    pfns = datasets(name="2018_15164022_magup")
    assert len(pfns) == 6

    datasets = AnalysisData("b2oc", "b02dkpi", version="v0r0p2970193")
    pfns = datasets(name="2018_15164022_magup")
    assert len(pfns) == 1 and "00145075_00000001" in pfns[0]

    with pytest.raises(Exception, match="version argument doesn't support iterables"):
        AnalysisData("b2oc", "b02dkpi", version=["v0r0p2518507", "v0r0p2970193"])
    with pytest.raises(Exception, match="version argument doesn't support iterables"):
        AnalysisData("b2oc", "b02dkpi", version={"v0r0p2518507", "v0r0p2970193"})


def test_defaults_name(apd_cache):
    with pytest.raises(
        Exception, match="name is not supported on AnalysisData objects"
    ):
        AnalysisData(
            "b2oc", "b02dkpi", version="v0r0p2518507", name="2018_15164022_magup"
        )
    with pytest.raises(
        Exception, match="name is not supported on AnalysisData objects"
    ):
        AnalysisData("b2oc", "b02dkpi", name="2018_15164022_magup")


def test_defaults_tag_override(apd_cache):
    datasets = AnalysisData(
        "b2oc", "b02dkpi", datatype=2018, polarity=["magup", "magdown"]
    )

    pfns = datasets(datatype="2011", eventtype="11164047", polarity="magdown")
    assert len(pfns) == 5 and all("00128098_0000" in x for x in pfns)

    pfns = datasets(version="v0r0p2970193", eventtype="15164022", polarity="magup")
    assert len(pfns) == 1 and "00145075_00000001" in pfns[0]

    pfns = datasets(version="v0r0p2970193", eventtype=15164022, polarity="magup")
    assert len(pfns) == 1 and "00145075_00000001" in pfns[0]

    pfns = datasets(version="v0r0p2970193", eventtype="15164022", polarity="magup")
    assert len(pfns) == 1 and "00145075_00000001" in pfns[0]

    pfns = datasets(version="v0r0p2970193", eventtype=15164022, polarity="MagUp")
    assert len(pfns) == 1 and "00145075_00000001" in pfns[0]

    with pytest.raises(Exception, match="Error"):  # TODO: This should be more specific
        datasets(eventtype=15164022, polarity="magup")


def test_by_tag_single(apd_cache):
    datasets = AnalysisData("b2oc", "b02dkpi")

    pfns = datasets(datatype="2011", eventtype="11164047", polarity="magdown")
    assert len(pfns) == 5 and all("00128098_0000" in x for x in pfns)

    pfns = datasets(
        version="v0r0p2970193", datatype="2018", eventtype="15164022", polarity="magup"
    )
    assert len(pfns) == 1 and "00145075_00000001" in pfns[0]

    pfns = datasets(
        version="v0r0p2970193", datatype=2018, eventtype=15164022, polarity="magup"
    )
    assert len(pfns) == 1 and "00145075_00000001" in pfns[0]

    pfns = datasets(
        version="v0r0p2970193", datatype=2018, eventtype="15164022", polarity="magup"
    )
    assert len(pfns) == 1 and "00145075_00000001" in pfns[0]

    pfns = datasets(
        version="v0r0p2970193", datatype="2018", eventtype=15164022, polarity="MagUp"
    )
    assert len(pfns) == 1 and "00145075_00000001" in pfns[0]

    with pytest.raises(
        Exception, match=r"Error loading data: 1 problem\(s\) found"
    ):  # TODO: This should be more specific
        datasets(datatype="2018", eventtype=15164022, polarity="magup")


def test_by_tag_multiple(apd_cache):
    datasets = AnalysisData("b2oc", "b02dkpi")

    pfns = datasets(datatype=["2012", "2011"], eventtype="11164047", polarity="magdown")
    assert len(pfns) == 12 and all(
        any(y in x for y in ["00128098_0000", "00128228_00000"]) for x in pfns
    )

    pfns = datasets(
        datatype=["2012", "2011"], eventtype="11164047", polarity=["magup", "magdown"]
    )
    assert len(pfns) == 22 and all(
        any(
            y in x
            for y in [
                "00128098_0000",
                "00128228_00000",
                "00128204_000",
                "00128212_0000",
            ]
        )
        for x in pfns
    )

    with pytest.raises(
        Exception, match=r"Error loading data: 4 problem\(s\) found"
    ):  # TODO: This should be more specific
        datasets(datatype=["2012", "2011"], polarity=["magup", "magdown"])

    with pytest.raises(
        Exception, match=r"Error loading data: 2 problem\(s\) found"
    ):  # TODO: This should be more specific
        datasets(datatype=["2015", "2016"], polarity=["magoff"])

    pfns = datasets(datatype=["2015", "2016"], polarity=["magup", "magdown"], mc=False)
    assert len(pfns) == 519 and all(
        any(
            y in x for y in ["00121802_00", "00121816_00", "00121814_00", "00121794_00"]
        )
        for x in pfns
    )
    pfns2 = datasets(
        datatype=["2015", "2016"], polarity=["magup", "magdown"], data=True
    )
    assert pfns == pfns2


def test_data_mc_tags(apd_cache):
    datasets = AnalysisData("b2oc", "b02dkpi")

    with pytest.raises(ValueError, match="values of data= and mc= are inconsistent"):
        datasets(
            datatype=["2015", "2016"], polarity=["magup", "magdown"], data=True, mc=True
        )

    with pytest.raises(ValueError, match="values of data= and mc= are inconsistent"):
        datasets(
            datatype=["2015", "2016"],
            polarity=["magup", "magdown"],
            data=False,
            mc=False,
        )


def test_missing_by_name(apd_cache):
    datasets = AnalysisData("b2oc", "b02dkpi")
    with pytest.raises(KeyError):
        datasets(version="i-do-no-exist", name="2018_15164022_magup")
    with pytest.raises(KeyError):
        datasets(version="v0r0p2970193", name="i-do-not-exist")


def test_missing_by_tags(apd_cache):
    datasets = AnalysisData("b2oc", "b02dkpi")
    with pytest.raises(KeyError):
        datasets(version="i-do-no-exist", name="2018_15164022_magup")
    with pytest.raises(KeyError):
        datasets(version="v0r0p2970193", name="i-do-not-exist")


def test_analysis_case_sensitivity(apd_cache):
    datasets = AnalysisData("b2oc", "b02dkpi")
    assert len(datasets.samples) == 1694
    assert len(AnalysisData("B2OC", "B02DKPI").samples) == 1694

    pfns = datasets(version="v0r0p2970193", name="2018_15164022_magup")
    assert len(pfns) == 1 and "00145075_00000001" in pfns[0]

    pfns = datasets(version="V0R0P2970193", name="2018_15164022_MAGUP")
    assert len(pfns) == 1 and "00145075_00000001" in pfns[0]


def test_name_case_sensitivity(apd_cache):
    datasets = AnalysisData("b2oc", "b02dkpi")
    pfns = datasets(version="v0r0p2970193", name="2018_15164022_MAGUP")
    assert len(pfns) == 1 and "00145075_00000001" in pfns[0]
