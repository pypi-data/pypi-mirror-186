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

import subprocess
from pathlib import Path


class DataCache:
    """Class in charge of dealing with the caching of ROOT files in a local directory"""

    def __init__(self, root_dir):
        self.root = Path(root_dir)
        if not self.root.exists():
            self.root.mkdir()

    def remote_to_local(self, remote):
        """Convert a remote file name to the correponding path onthe local disk"""
        r = Path(remote)
        if "?" in r.name:
            # Remove the arguments to the ROOT URL if there are some
            r = Path(*(r.parts[:-1] + (r.name.split("?")[0],)))
        # We assume that the first two parts are the protocol (root) and the
        # EOS server
        if not r.parts:
            raise ValueError(f"Unusable remote: {remote}.")
        if not r.parts[0].startswith("root"):
            raise ValueError(f"{r}: Remote file {remote} not a ROOT file")
        return self.root / Path(*r.parts[2:])

    def has_local_copy(self, remote):
        local = self.remote_to_local(remote)
        if not local:
            return False
        return local.exists()

    def __call__(self, remote):
        """Check whether a local copy of the is present,
        if yes return its path otherwise return the remote"""
        local = self.remote_to_local(remote)
        if not local:
            return remote
        return str(local) if local.exists() else remote

    def copy_locally(self, remote):
        local = self.remote_to_local(remote)
        local.parent.mkdir(parents=True, exist_ok=True)
        cmd = ["xrdcp", "--silent", str(remote), str(local)]
        result = subprocess.run(cmd, check=True, timeout=1000)
        return result
