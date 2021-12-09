import os
import json
from ..server import FDSServer

"""
Folder Downloader Version
Interact with all version of the opened project
"""


class Fdv:
    fds_web_server: FDSServer
    """FDS Server"""
    version_folder: str
    """folder where json version was saved"""

    def __init__(self, version_folder: str, fds_web_server: FDSServer = None):
        """Constructor"""
        self.fds_web_server = fds_web_server
        if not os.path.isdir(version_folder):
            raise FileNotFoundError("version_folder not exist: " + version_folder)
        if os.path.abspath(version_folder):
            self.version_folder = version_folder
        else:
            self.version_folder = os.path.join(os.getcwd(), version_folder)

    def get_all_version(self):
        """Get all version from the server"""
        if self.fds_web_server is None:
            raise AttributeError("fds_web_server not initialized")
        else:
            return self.fds_web_server.get_all_version()

    def get_all_downloaded_version(self):
        """Get all downloaded version from the folder"""
        return [".".join(file.split(".")[0:-1]) for file in os.listdir(self.version_folder)]

    def download_fdv(self, version_name: str):
        """Download a version in the server and save it in the folder"""
        if self.fds_web_server is None:
            raise AttributeError("fds_web_server not initialized")
        else:
            open(os.path.join(self.version_folder, version_name + ".fdv"),
                 "w").write(json.dumps(self.fds_web_server.get_version(version_name)))

    def get_fdv_data(self, version_name: str):
        """Get the dict of a downloaded version"""
        if os.path.isfile(os.path.join(self.version_folder, version_name + ".fdv")):
            return json.load(open(os.path.join(self.version_folder, version_name + ".fdv")))

    def write_version(self, name: str, version_data: dict):
        """Write a version"""
        open(os.path.join(self.version_folder, name + ".fdv"), "w").write(
            json.dumps(version_data, indent=4)
        )
