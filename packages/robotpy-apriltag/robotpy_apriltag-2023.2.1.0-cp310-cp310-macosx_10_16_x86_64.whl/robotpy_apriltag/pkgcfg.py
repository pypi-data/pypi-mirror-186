# fmt: off
# This file is automatically generated, DO NOT EDIT

from os.path import abspath, join, dirname
_root = abspath(dirname(__file__))

libinit_import = "robotpy_apriltag._init_apriltag"
depends = ['wpiutil', 'wpimath_cpp']
pypi_package = 'robotpy-apriltag'

def get_include_dirs():
    return [join(_root, "include"), join(_root, "rpy-include")]

def get_library_dirs():
    return [join(_root, "lib")]

def get_library_dirs_rel():
    return ['lib']

def get_library_names():
    return ['apriltag']

def get_library_full_names():
    return ['libapriltag.dylib']