from .pcjs_api import PCJsApi


class FDSServer(PCJsApi):
    def __init__(self, url):
        super().__init__(url)

    def get_all_version(self):
        return self.getJsBySystem("AllVersion")

    def get_version(self, version_name):
        return self.getJsBySystem("GetVersion", {"version": version_name})

    def download_fdf(self, id_fdf, name, version):
        return self.getResolveBySystem("DownloadFdf",
                                       {"id": id_fdf, "name": name, "version": version}).content
