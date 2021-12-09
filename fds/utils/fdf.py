"""
Folder Downloader File
"""
import os
import zipfile
import shutil
import hashlib


class Fdf:
    def __init__(self, fdf_folder):
        if not os.path.isdir(fdf_folder):
            raise FileNotFoundError("binaries_folder not exist: " + fdf_folder)
        if os.path.abspath(fdf_folder):
            self.fdf_folder = fdf_folder
        else:
            self.fdf_folder = os.path.join(os.getcwd(), fdf_folder)

    def download_fdf(self, fds_web_server, id_fdf, name, version):
        fdf_name = ".".join([str(id_fdf), str(name), str(version), "fdf"])
        if not os.path.isfile(os.path.join(self.fdf_folder, fdf_name)):
            content = fds_web_server.download_fdf(id_fdf, name, version)
            open(os.path.join(self.fdf_folder, fdf_name), "wb").write(content)

    def decompress_fdf(self, id_fdf, name, version, folder):
        fdf_name = ".".join([str(id_fdf), str(name), str(version), "fdf"])
        if not os.path.isfile(os.path.join(self.fdf_folder, fdf_name)):
            raise FileNotFoundError
        zipped = zipfile.ZipFile(os.path.join(self.fdf_folder, fdf_name), "r", zipfile.ZIP_DEFLATED)
        zipped.extractall(folder)

    def create_fdf_file(self, dependency):
        # id.name.version.fdf
        dependency_file_existed = [
            file
            for file in os.listdir(self.fdf_folder)
            if file.split(".")[0] == str(dependency["id"])
        ]
        dependency_version_existed = [
            version.split(".")[-2]
            for version in dependency_file_existed
        ]
        fdf_version = len(dependency_version_existed)
        self.create_zip(os.path.join(".", dependency["folder"]), os.path.join(self.fdf_folder, "temp.fdf"))
        for file in range(len(dependency_file_existed)):
            if self.compare_files(os.path.join(self.fdf_folder, dependency_file_existed[file]),
                             os.path.join(self.fdf_folder, "temp.fdf")):
                fdf_version = dependency_version_existed[file]
                break
        if not os.path.isfile(os.path.join(self.fdf_folder,
                                           ".".join([str(dependency["id"]),
                                                     str(dependency["name"]),
                                                     str(fdf_version),
                                                     "fdf"]))):
            shutil.copy(os.path.join(self.fdf_folder, "temp.fdf"),
                        os.path.join(self.fdf_folder,
                                     ".".join([str(dependency["id"]),
                                               str(dependency["name"]),
                                               str(fdf_version),
                                               "fdf"])))
        os.remove(os.path.join(self.fdf_folder, "temp.fdf"))
        return fdf_version

    @staticmethod
    def create_zip(folder, file):
        if os.path.isfile(file):
            raise FileExistsError
        zipped = zipfile.ZipFile(file, "w", zipfile.ZIP_DEFLATED)
        dir_list = os.listdir(folder)
        for indexed in range(len(dir_list)):
            if os.path.isfile(os.path.join(folder, dir_list[indexed])):
                zipped.write(os.path.join(folder, dir_list[indexed]), dir_list[indexed])
        zipped.close()

    @staticmethod
    def compare_files(a, b):
        file_a = hashlib.sha256(open(a, 'rb').read()).digest()
        file_b = hashlib.sha256(open(b, 'rb').read()).digest()
        return file_a == file_b
