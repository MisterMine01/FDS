from .pcjs_api import PCJsApi

"""Server Connection to the FDS
Use PCJsApi
"""


class FDSServer(PCJsApi):
    def __init__(self, url):
        """Constructor"""
        super().__init__(url)

    def get_all_version(self):
        """Get all version in the server"""
        return self.getJsBySystem("AllVersion")

    def get_version(self, version_name: str):
        """get the json of a version"""
        return self.getJsBySystem("GetVersion", {"version": version_name})

    def download_fdf(self, id_fdf: str, name: str, version: str):
        """Download a Fdf, return the bytes content of the file"""
        return self.getResolveBySystem("DownloadFdf",
                                       {"id": id_fdf, "name": name, "version": version}).content
