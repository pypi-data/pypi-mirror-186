import os
from distutils.dir_util import copy_tree

base_dir = os.path.dirname(os.path.abspath(__file__))
clib_path = os.path.join(base_dir, "clib")
compiled_path = os.path.join(clib_path, "compiled")


def make(lib_path, package_name):
    cdir = os.getcwd()
    unbuilt_path = os.path.join(lib_path, package_name)
    built_path = os.path.join(compiled_path, package_name)
    if not os.path.exists(built_path):
        copy_tree(unbuilt_path, built_path)
        os.chdir(built_path)
        os.system("make")  # nosec
        os.chdir(cdir)


make(clib_path, "pigz")
