from setuptools import setup
import os
# pip is already distributed with setuptools.
# if you are installing packages with pip, you already have setuptools.

import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def is_package_name(requirement_arg):
    invalid_prefixes = ("-", "#")
    return requirement_arg and not requirement_arg.startswith(invalid_prefixes)


def get_install_requires(filename):
    return [line.strip() for line in read(filename).split("\n") if is_package_name(line)]


setup(
    name='random-python-package-within-monorepo', # This is what you pip install
    version='0.0.1',
    description='This will generate random number for you!',
    # List of actual python files(modules) that you want to distribute.
    py_modules=["random_number"], # This is what people import, not pip install
    package_dir={'':'random_python_package_within_monorepo/random_python_package_within_monorepo'}, # Telling setup tools that our code is under python_package_1 folder. Again, usually this would be `src` usually
    install_requires=get_install_requires("requirements.txt"),
    # install_requires = [ "abcd ~= 1.1", "xyz ~= 2.2" ]
    extra_require = {
        "dev": [
            "pytest>=3.7",
            "twine>=1.11.0",
        ],
    }
)

# 일단 넘어가자...

##### BUILD & PACKAGING ######
# Run "python setup.py" with "bdist_wheel" command to create a wheel file, which is a zip file with all the files you need to distribute your package.
# wheel file is appropriate for distributing your pakckage to python package index(pypi).
# Run `python setup.py bdist_wheel` from ~/repos/urban-octo-waffle/python_package_1
# Run the above command at the same level where the setup.py file is of course
"""
running bdist_wheel
running build
running build_py
creating build
creating build/lib
copying python_package_1/python_package_1/random_number.py -> build/lib
"""
# build folder is setuptools move files during the process of building our wheel file
# Actual code is under build/lib/
# Actual wheel file is under dist/python_package_1-0.0.1-py3-none-any.whl : the distribution file!!

###### SDIST #####
# python setup.py sdist
# generates python_package_1-0.0.1.tar.gz under dist folder

# RUN tar tzf dist/python_package_1-0.0.1.tar.gz 
# Make sure the tar file contains all the files you want to distribute.
# It's missing some test and stuff, so we need to add MANIFEST.in file

###### MANIFEST #####
# pip install check-manifest
# check-manifest --create
"""
(list) davoh@LUSC02F40PZMD6V ~/repos/urban-octo-waffle/python-package-1 (main) $ check-manifest --create
lists of files in version control and sdist do not match!
missing from sdist:
  python_package_1/python_package_1/__init__.py
  python_package_1/python_package_1/tests/test_random_number.py
  requirements.txt
no MANIFEST.in found
suggested MANIFEST.in rules:
  include *.txt
  recursive-include python_package_1 *.py
creating MANIFEST.in
"""

# git add MANIFEST.in
# Now when running tar tzf dist/python_package_1-0.0.1.tar.gz , there are missing files added!
###### Install Locally #####
# pip install -e . 
# -e : install the package in editable mode. This means that if you make changes to the code, you don't have to reinstall the package.
# . : current directory 
# when you pip install, it installs it into site-packages folder, inside your python distribution
# we don't want that while we are working on project! Just wanna use source directory!
# -e links to the code that you are working on rather than copying it to site-packages

# so cannot do import yet, because it is not in our PATH
"""
Obtaining file:///Users/davoh/repos/urban-octo-waffle/python-package-1
Preparing metadata (setup.py) ... done
Installing collected packages: python-package-1
Running setup.py develop for python-package-1
Successfully installed python-package-1-0.0.1
"""


###### BUILD FINALLY #####
# python setup.py bdist_wheel sdist
# ls dist/
#   python_package_1-0.0.1-py3-none-any.whl
#   python_package_1-0.0.1.tar.gz


##### UPLOAD ######
# pip install twine
# twine upload dist/*