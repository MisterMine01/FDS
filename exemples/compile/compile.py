import fds
import os

folder = "to-compile"

Compiler = fds.FDSCompiler(os.path.join(folder, "Utopia.fdd"),
                           os.path.join(folder, "Fdf"),
                           os.path.join(folder, "version")
                           )

for i in os.listdir(os.path.join(folder, "Utopia")):
    print("create "+i)
    Compiler.create_new_version(i, os.path.join(folder, "Utopia", i),
                                [
                                    x
                                    for x in os.listdir(os.path.join(folder, "Utopia", i))
                                    if os.path.splitext(x)[1] == ".exe"
                                ][0]
                                )