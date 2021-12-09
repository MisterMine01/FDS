import json
import os
from ..version import FDD_version

"""
Folder Downloader Data
Interact with the Data, who's dependency
"""


class Fdd:
    dependency_data: str
    """File path"""
    def __init__(self, dependency_data):
        """Constructor"""
        if os.path.splitext(dependency_data)[1].lower() != ".fdd".lower():
            raise AttributeError("dependency_data is not fdd file")
        if not os.path.isfile(dependency_data):
            open(dependency_data, "w").write(json.dumps({"compiler_version": FDD_version,
                                                         "dependency": []},
                                                        indent=4))
        if os.path.abspath(dependency_data):
            self.dependency_data = dependency_data
        else:
            self.dependency_data = os.path.join(os.getcwd(), dependency_data)

    def load_dependency_data(self):
        """add dependency in pwd not existed yet and return all dependency"""
        dependency_js = json.load(open(self.dependency_data))
        all_folder = self.tree(".")
        for i in range(len(all_folder)):
            if all_folder[i][0] not in [folder["folder"] for folder in dependency_js["dependency"]]:
                dependency_js["dependency"].append(
                    {
                        "id": len(dependency_js["dependency"]),
                        "folder": all_folder[i][0],
                        "name": all_folder[i][1]
                    }
                )
        open(self.dependency_data, "w").write(json.dumps(dependency_js, indent=4))
        return dependency_js

    def dependency_compiler_from_main(self):
        """return dependency needed in the pwd"""
        dependency_data = self.load_dependency_data()
        dependency_require = []
        for dependency in dependency_data["dependency"]:
            if os.path.isdir(dependency["folder"]):
                dependency_require.append(dependency)
                """
                    {
                        "id": dependency["id"],
                        "name": dependency["name"],
                        "folder": dependency["folder"],
                        "version": str(self.create_fdf_file(dependency))
                    }
                )"""
        return dependency_require

    @staticmethod
    def tree(rst):
        """find all folder and sub-folder in a dir"""
        folders = [[rst, os.path.basename(rst)]]
        for fold in os.listdir(rst):
            if os.path.isdir(os.path.join(rst, fold)):
                for loaded in Fdd.tree(os.path.join(rst, fold)):
                    folders.append(loaded)
        return folders
