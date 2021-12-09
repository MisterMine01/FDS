import os
import json


class Fdv:
    def __init__(self, version_folder, fds_web_server=None):
        self.fds_web_server = fds_web_server
        if not os.path.isdir(version_folder):
            raise FileNotFoundError("version_folder not exist: " + version_folder)
        if os.path.abspath(version_folder):
            self.version_folder = version_folder
        else:
            self.version_folder = os.path.join(os.getcwd(), version_folder)

    def get_all_version(self):
        if self.fds_web_server is None:
            raise AttributeError("fds_web_server not initialized")
        else:
            return self.fds_web_server.get_all_version()

    def get_all_downloaded_version(self):
        return [".".join(file.split(".")[0:-1]) for file in os.listdir(self.version_folder)]

    def download_fdv(self, version_name):
        if self.fds_web_server is None:
            raise AttributeError("fds_web_server not initialized")
        else:
            open(os.path.join(self.version_folder, version_name + ".fdv"),
                 "w").write(json.dumps(self.fds_web_server.get_version(version_name)))

    def get_fdv_data(self, version_name):
        if os.path.isfile(os.path.join(self.version_folder, version_name + ".fdv")):
            return json.load(open(os.path.join(self.version_folder, version_name + ".fdv")))

    def write_version(self, name, version_data):
        open(os.path.join(self.version_folder, name + ".fdv"), "w").write(
            json.dumps(version_data, indent=4)
        )
