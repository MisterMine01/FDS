from .utils import Fdf, Fdv
from .server import FDSServer
import shutil
import os

"""
FDS Client.
Can connect to a FDS server, download and start a Version.
"""


class FDSClient:
    fdf: Fdf
    """Folder Downloader File"""
    fdv: Fdv
    """Folder Downloader Version"""
    fds_web_server: FDSServer
    """FDS Server"""

    def __init__(self, fdf_folder: str, fdv_folder: str, fds_web_server: FDSServer):
        """Constructor"""
        self.fds_web_server = fds_web_server
        self.fdf = Fdf(fdf_folder)
        self.fdv = Fdv(fdv_folder, fds_web_server)

    def download_version(self, version_name: str):
        """Download a version by his name"""
        if version_name not in self.fdv.get_all_downloaded_version():
            self.fdv.download_fdv(version_name)
        fdv_data = self.fdv.get_fdv_data(version_name)
        for i in fdv_data["dependency"]:
            self.fdf.download_fdf(i["id"], i["name"], i["version"], self.fds_web_server)

    def start_version(self, version_name: str, decompressed_folder: str):
        """Start a version"""
        print(version_name)
        self.download_version(version_name)
        try:
            shutil.rmtree(decompressed_folder)
        except FileNotFoundError:
            pass
        os.mkdir(decompressed_folder)
        fdv_data = self.fdv.get_fdv_data(version_name)
        for dependency in range(len(fdv_data["dependency"])):
            try:
                os.mkdir(os.path.join(decompressed_folder,
                                      fdv_data["dependency"][dependency]["folder"]))
            except FileExistsError:
                pass
            self.fdf.decompress_fdf(fdv_data["dependency"][dependency]["id"],
                                    fdv_data["dependency"][dependency]["name"],
                                    fdv_data["dependency"][dependency]["version"],
                                    os.path.join(decompressed_folder, fdv_data["dependency"][dependency]["folder"]))
        return fdv_data["executable"]
