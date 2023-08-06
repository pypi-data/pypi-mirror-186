###############################################################################
# (c) Copyright 2022 CERN for the benefit of the LHCb Collaboration           #
#                                                                             #
# This software is distributed under the terms of the GNU General Public      #
# Licence version 3 (GPL Version 3), copied verbatim in the file "COPYING".   #
#                                                                             #
# In applying this licence, CERN does not waive the privileges and immunities #
# granted to it by virtue of its status as an Intergovernmental Organization  #
# or submit itself to any jurisdiction.                                       #
###############################################################################
__all__ = ("auth", "authw")

import json
import os
import re
import urllib.parse as urlparse
from pathlib import Path, PurePosixPath


def _find_suitable_token(path: PurePosixPath, allow_write: bool) -> str:
    if not hasattr(_find_suitable_token, "tokens"):
        _find_suitable_token.tokens = json.loads(
            Path(os.environ["LBAP_TOKENS_FILE"]).read_text()
        )
    if path.root == "//":
        path = PurePosixPath(str(path)[1:])
    for eos_token in _find_suitable_token.tokens["eos_tokens"]:
        if allow_write and not eos_token["allow_write"]:
            continue
        if path.is_relative_to(eos_token["path"]):
            return eos_token["token"]

    msg = "No matching token"
    if allow_write:
        msg += " with write access"
    msg += f" found for path: {path}\n"
    msg += "Available tokens:\n"
    for eos_token in _find_suitable_token.tokens["eos_tokens"]:
        msg += f"    * {eos_token['path']}"
        if not eos_token["allow_write"]:
            msg += " (readonly)"
        msg += "\n"
    raise ValueError(msg)


def add_token_to_url(url: str, allow_write: bool) -> str:
    url = urlparse.urlparse(url)
    token = _find_suitable_token(PurePosixPath(url.path), allow_write)
    token = urlparse.unquote(token)
    url_parts = list(url)
    url_parts[4] = urlparse.urlencode(
        dict(urlparse.parse_qsl(url_parts[4]))
        | {"xrd.wantprot": "unix", "authz": token}
    )
    url_with_token = urlparse.urlunparse(url_parts)
    # EOS currently doesn't accept percent encoded URLs despite ':' being a
    # reserved character in URIs. This will be fixed in the next version of EOS
    # but for now we need to unquote the URL.
    url_with_token = url_with_token.replace("authz=zteos64%3A", "authz=zteos64:")
    # EOS also doesn't understand the use of uppercase hex digits for escaped
    # padding characters in base64 encoded tokens so replace them with lowercase
    url_with_token = re.sub(
        r"(&authz=[^&#]+?)((?:%3D){1,3})",
        lambda x: x.groups()[0] + x.groups()[1].lower(),
        url_with_token,
    )
    return url_with_token


def auth(url: str) -> str:
    """Take a PFN and return one with read-only credentials appended"""
    if "LBAP_TOKENS_FILE" in os.environ:
        return add_token_to_url(url, False)
    return url


def authw(url: str) -> str:
    """Take a PFN and return one with read-write credentials appended"""
    if "LBAP_TOKENS_FILE" in os.environ:
        return add_token_to_url(url, True)
    return url
