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
# install package (test to local computer)
# $ pip install .
# to confirm, use
# $ conda list    (we should see mysci)
# to uninstall
# $ pip uninstall mysci
# install from GitHub
# $ pip install git+https://github.com/Username/Project.git
# https://github.com/sandra444/ncar_python_tutorial.git
# (fileplay) C:\Users\Sandra Karcher\OneDrive\adell\repos\ncar_python_tutorial>pip install git+https://github.com/sandra444/ncar_python_tutorial.git
# $ conda list
# to put on PyPI
# $ pip install twine
# By installing this package, a new utility called twine will be installed that you can use to upload your package. 
# First, however, we need to build a distribution package using our newly created setup.py file. 
# To do that, execute the following command in the same directory where the setup.py file is located:
# $ python setup.py sdist bdist_wheel
# Then, to upload your newly created distribution package to PyPI, execute the following:
# $ twine upload dist/*
# see this page for more details https://ncar.github.io/python-tutorial/tutorials/yourfirst.html#using-a-built-in-package
