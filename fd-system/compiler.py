from .utils import *
import os

"""
FDS Compiler
Compile a FDD for used in a FDS Server
"""


class FDSCompiler:
    fdd: Fdd
    """Folder Download Data"""
    fdf: Fdf
    """Folder Download File"""
    fdv: Fdv
    """Folder Download Version"""

    def __init__(self, dependency_data_fdd: str, fdf_folder: str, version_folder: str):
        """Constructor"""
        self.fdd = Fdd(dependency_data_fdd)
        self.fdf = Fdf(fdf_folder)
        self.fdv = Fdv(version_folder)

    def create_new_version(self, name: str, game_folder: str, executable: str = None):
        """Create a new version with a name and contains the folder.
        A executable can be added.
        """
        if not os.path.isdir(game_folder):
            raise FileNotFoundError("game_folder not exist: " + game_folder)
        if not os.path.abspath(game_folder):
            game_folder = os.path.join(os.getcwd(), game_folder)
        work_path = os.getcwd()
        os.chdir(game_folder)
        version_data = {
            "name": name,
            "executable": executable
        }
        dependency_used = self.fdd.dependency_compiler_from_main()
        for i in range(len(dependency_used)):
            dependency_used[i]["version"] = str(self.fdf.create_fdf_file(dependency_used[i]))
        version_data["dependency"] = dependency_used
        self.fdv.write_version(name, version_data)
        os.chdir(work_path)
