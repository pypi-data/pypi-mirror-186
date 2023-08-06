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
from pathlib import Path

import pytest

from apd import AnalysisData
from apd.data_cache import DataCache


def test_url():
    cache = DataCache("/tmp")

    remote = "root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2012/INCLBDSHCX_WS.ROOT/00169880/0000/00169880_00000007_1.inclbdshcx_ws.root"
    local = cache.remote_to_local(remote)
    assert (
        str(local)
        == "/tmp/eos/lhcb/grid/prod/lhcb/MC/2012/INCLBDSHCX_WS.ROOT/00169880/0000/00169880_00000007_1.inclbdshcx_ws.root"
    )

    with pytest.raises(ValueError):
        local = cache.remote_to_local("/data/test")

    with pytest.raises(ValueError):
        cache.remote_to_local("")


def test_use_data_cache(apd_cache, apdata_cache, apinfo_cache):
    dc = DataCache(apdata_cache)
    datasets = AnalysisData("SL", "RDs", data_cache=dc)
    lfns = datasets(name="mc_13266069_2018_magup", version="v0r0p1735460")

    # Check that the 1st file is remote
    assert dc(lfns[0]).startswith("root")

    # Create a fake local copy and check that the cache object really returns it
    l0 = Path(dc.remote_to_local(lfns[0]))
    l0.parent.mkdir(parents=True, exist_ok=True)
    l0.write_text("test")
    assert str(dc(lfns[0])).startswith(str(apdata_cache))

    # Now check the PFNs from the dataset
    lfns2 = datasets(name="mc_13266069_2018_magup", version="v0r0p1735460")
    assert lfns2[0].startswith(str(apdata_cache))
