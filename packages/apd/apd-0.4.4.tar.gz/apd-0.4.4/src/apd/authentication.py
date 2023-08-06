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
__all__ = ("device_authorization_login", "get_auth_headers", "logout")

import base64
import binascii
import hashlib
import json
import os
import secrets
import socket
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import NoReturn

import requests

OIDC_BASE_URL = "https://auth.cern.ch/auth/realms/cern/protocol/openid-connect"
SSO_CLIENT_ID = "lhcb-analysis-productions"
LBAPI_BASE_URL = "https://lbap.app.cern.ch"


def stderr(*args: str):
    sys.stderr.write(" ".join(map(str, args)) + "\n")
    sys.stderr.flush()


def _user_token_file() -> Path:
    return Path().home() / ".config" / "apd" / "user-token.json"


def _login_gitlab_jwt(tokens_file: Path) -> NoReturn:
    r = requests.get(
        f"{LBAPI_BASE_URL}/gitlab/credentials/",
        timeout=10,
        headers={"Authorization": f"Bearer {os.environ['CI_JOB_JWT_V2']}"},
    )
    if not r.ok:
        raise RuntimeError(f"Failed to get credentials with: {r.json().get('detail')}")
    _write_request(r, tokens_file)


def _login_sso(token_file: Path) -> NoReturn:
    """Login to the CERN SSO and obtain a user token."""
    token_response = device_authorization_login(SSO_CLIENT_ID)
    expires = datetime.now(tz=timezone.utc) + timedelta(days=9)
    r = requests.post(
        f"{LBAPI_BASE_URL}/user/tokens/create",
        headers={"Authorization": f"Bearer {token_response['access_token']}"},
        json={
            "description": f"Token for apd generated on {socket.gethostname()}",
            "expires": expires.isoformat(),
        },
        timeout=10,
    )
    r.raise_for_status()
    _write_request(r, token_file)


def _write_request(r: requests.Response, path: Path) -> NoReturn:
    """Write the response (i.e. the token) as a read-only file on disk"""
    # Ensure the data is valid JSON
    data = json.dumps(r.json())

    # Create and write a file with a random filename in the same
    # directory and rename it once the write operation is done
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path = path.parent / (path.name + secrets.token_urlsafe())
    with temp_path.open("w") as fh:
        temp_path.chmod(0o500)
        fh.write(data)
    os.rename(temp_path, path)


def _auth_ok(token) -> NoReturn:
    r = requests.get(
        f"{LBAPI_BASE_URL}/user/",
        headers={"Authorization": f"Bearer {token}"},
        timeout=5,
    )
    r.raise_for_status()


def get_auth_headers() -> dict[str, str]:
    if "LBAP_TOKENS_FILE" in os.environ:
        tokens_file = Path(os.environ["LBAP_TOKENS_FILE"])
        if not tokens_file.read_text():
            _login_gitlab_jwt(tokens_file)
        token = json.loads(tokens_file.read_text())["lbapi_token"]
    else:
        token_file = _user_token_file()
        try:
            token = json.loads(token_file.read_text())
            _auth_ok(token)
        except Exception:  # pylint: disable=broad-except
            _login_sso(token_file)
            token = json.loads(token_file.read_text())
    return dict(headers={"Authorization": f"Bearer {token}"})


def logout():
    if "LBAP_TOKENS_FILE" in os.environ:
        tokens_file = Path(os.environ["LBAP_TOKENS_FILE"])
        tokens_file.unlink()
    token_file = _user_token_file()
    if token_file.is_file():
        token_file.unlink()


def device_authorization_login(clientid=SSO_CLIENT_ID):
    """Get an OIDC token by using Device Authorization Grant.

    :param clientid: Client ID of a public client with device authorization grant enabled.
    """
    random_state = binascii.hexlify(os.urandom(8))
    # code_verifier: https://www.rfc-editor.org/rfc/rfc7636#section-4.1
    # 48*2 = 96 characters, which is within 43-128 limits.
    code_verifier = binascii.hexlify(os.urandom(48))

    # code_challenge: https://www.rfc-editor.org/rfc/rfc7636#section-4.2
    # BUT Keycloak decided to reject any base64 input containing '=' (!!)
    # so we have to remove it even if we are following the standard.
    code_challenge = (
        base64.urlsafe_b64encode(hashlib.sha256(code_verifier).digest())
        .decode()
        .replace("=", "")
    )

    r = requests.post(
        f"{OIDC_BASE_URL}/auth/device",
        data={
            "client_id": clientid,
            "state": random_state,
            "code_challenge_method": "S256",
            "code_challenge": code_challenge,
        },
        verify=True,
        timeout=30,
    )

    if not r.ok:
        stderr(r.text)
        raise Exception(
            "Authentication request failed: Device authorization response was not successful."
        )

    auth_response = r.json()

    stderr("CERN SINGLE SIGN-ON\n")
    stderr("On your tablet, phone or computer, go to:")
    stderr(auth_response["verification_uri"])
    stderr("and enter the following code:")
    stderr(auth_response["user_code"])
    stderr()
    stderr("You may also open the following link directly and follow the instructions:")
    stderr(auth_response["verification_uri_complete"])
    stderr()
    stderr("Waiting for login...")

    signed_in = False
    while not signed_in:
        time.sleep(5)
        r_token = requests.post(
            f"{OIDC_BASE_URL}/token",
            data={
                "client_id": clientid,
                "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
                "device_code": auth_response["device_code"],
                "code_verifier": code_verifier,
            },
            verify=True,
            timeout=30,
        )
        signed_in = r_token.ok

    token_response = r_token.json()
    return token_response
