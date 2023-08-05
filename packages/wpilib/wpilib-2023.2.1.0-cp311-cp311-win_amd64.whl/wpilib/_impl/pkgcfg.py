# fmt: off
# This file is automatically generated, DO NOT EDIT

from os.path import abspath, join, dirname
_root = abspath(dirname(__file__))

libinit_import = "wpilib._impl._init_wpilibc"
depends = ['wpiHal', 'wpiutil', 'wpimath_cpp', 'ntcore']
pypi_package = 'wpilib'

def get_include_dirs():
    return [join(_root, "include"), join(_root, "rpy-include")]

def get_library_dirs():
    return [join(_root, "lib")]

def get_library_dirs_rel():
    return ['lib']

def get_library_names():
    return ['wpilibc']

def get_library_full_names():
    return ['wpilibc.dll']