from .utils import *
import os


class FDSCompiler:
    def __init__(self, dependency_data_fdd, fdf_folder, version_folder):
        self.fdd = Fdd(dependency_data_fdd)
        self.fdf = Fdf(fdf_folder)
        self.fdv = Fdv(version_folder)

    def create_new_version(self, name, game_folder, executable=None):
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
