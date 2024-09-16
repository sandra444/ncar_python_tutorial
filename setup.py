# https://ncar.github.io/python-tutorial/tutorials/yourfirst.html#using-a-built-in-package
# reminders
# in outer directory
# $ git clone https://github.com/username/some_package.git
# $ pip install some_package
# or, shortcut two in one
# $ pip install git+https://github.com/username/some_package.git
# if the package is on PyPI, it is even easier
# $ pip install some_package

# The setup.py file is a Python file necessary for package distribution. 
# This file tells pip how to install your package into the common Python space for your python interpreter. 

from distutils.core import setup

setup(
    name="mysci",
    version="1.0.0",
    description="A sample package",
    author="Xdev",
    author_email="xdev@ucar.edu",
    packages=["mysci"],
    install_requires=[],
)

# dependencies (install_requires) which is set to an empty list since our current package uses no external packages.
