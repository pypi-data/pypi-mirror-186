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
import json
import os
from pathlib import Path

import pytest
import responses

from apd.analysis_data import APD_METADATA_CACHE_DIR
from apd.ap_info import cache_ap_info, load_ap_info_from_single_file

DATA_DIR = Path(__file__).parent / "data"
APINFO_PATHS = DATA_DIR / "rds_ap_info.json"
APINFO_MULTIPLEVERSIONS_PATHS = DATA_DIR / "rds_ap_info_2versions.json"


@pytest.fixture
def apinfo():
    """load the requests test data"""
    return load_ap_info_from_single_file(APINFO_PATHS)


@pytest.fixture
def apinfo_multipleversions():
    """load the requests test data"""
    return load_ap_info_from_single_file(APINFO_MULTIPLEVERSIONS_PATHS)


@pytest.fixture
def mocked_responses():
    with responses.RequestsMock() as rsps:
        with open(APINFO_PATHS) as f:
            data = json.load(f)

        rsps.add(
            responses.GET,
            "https://lbap.app.cern.ch/stable/v1/SL/RDs",
            body=json.dumps(data["info"]),
            status=200,
            content_type="application/json",
        )

        rsps.add(
            responses.GET,
            "https://lbap.app.cern.ch/stable/v1/SL/RDs/tags",
            body=json.dumps(data["tags"]),
            status=200,
            content_type="application/json",
        )

        yield rsps


@pytest.fixture(autouse=True)
def patched_get_auth_headers(monkeypatch, tmp_path):
    tokens_path = tmp_path / "tokens.json"
    monkeypatch.setenv("LBAP_TOKENS_FILE", str(tokens_path))
    tokens = {
        "lbapi_token": "lbapi_token",
        "eos_tokens": [
            {"path": "/", "allow_write": True, "token": "eos_token"},
        ],
    }
    tokens_path.write_text(json.dumps(tokens))
    # Wipe the cache in apd.eos
    monkeypatch.delattr("apd.eos._find_suitable_token.tokens", raising=False)
    yield


@pytest.fixture
def apinfo_cache(tmp_path, mocked_responses, monkeypatch):
    """load the requests test data and cache it in a temp dir"""
    cachedir = tmp_path / "cache"
    os.makedirs(cachedir)
    cache_ap_info(cachedir, "SL", "RDs")
    yield cachedir


@pytest.fixture
def apdata_cache(tmp_path):
    """load the requests test data and cache it in a temp dir"""
    cachedir = tmp_path / "datacache"
    os.makedirs(cachedir)
    yield cachedir


@pytest.fixture
def apd_cache(monkeypatch):
    monkeypatch.setenv(APD_METADATA_CACHE_DIR, str(Path(__file__).parent / "cache-dir"))
    yield
