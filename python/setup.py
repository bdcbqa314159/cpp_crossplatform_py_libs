# setup.py
from setuptools import setup, Extension
import os
import platform


basename = os.path.basename(__file__)
dirname = os.path.dirname(__file__)

# Path to the pre-built module

source_dir = os.path.join(dirname, '..')

libraries_dir = os.path.join(source_dir, 'libraries')
binary_dir = os.path.join(source_dir, 'build', 'bin')

library_dir = os.path.join(libraries_dir, 'my_lib')
library_python_interface_dir = os.path.join(libraries_dir, 'my_lib_python_interface')


library_python_interface_src = os.path.join(library_python_interface_dir, 'src')
library_python_interface_includes = os.path.join(library_python_interface_dir, 'includes')
library_src = os.path.join(library_dir, 'src')
library_includes = os.path.join(library_dir, 'includes')


all_sources = [os.path.join(library_python_interface_src, "py_functions.cpp"),
               os.path.join(library_src, "functions.cpp")]

all_includes = [library_python_interface_includes, library_includes]


sfc_module = Extension('superfastcode', sources=all_sources,
                       include_dirs=all_includes,
                       library_dirs=[binary_dir],
                       libraries=['superfastcode', 'my_lib'],
                       language='c++',)

setup(
    name='superfastcode',
    version='1.0',
    author='Bernardo Cohen',
    description='Python Package with superfastcode C++ extension',
    ext_modules=[sfc_module],
)
