import fds

Compiler = fds.FDSCompiler("dependency.fdd", "fdf_folder", "version_folder")
Compiler.create_new_version("1.0", "folder")
