###############################################################################
# Coscine Python SDK
# Copyright (c) 2018-2022 RWTH Aachen University
# Licensed under the terms of the MIT License
###############################################################################
# Coscine, short for Collaborative Scientific Integration Environment is
# a platform for research data management (RDM).
# For more information on Coscine visit https://www.coscine.de/.
#
# Please note that this python module is open source software primarily
# developed and maintained by the scientific community. It is not
# an official service that RWTH Aachen provides support for.
###############################################################################

###############################################################################
# File description
###############################################################################

"""
This setup script builds and installs the Coscine Python SDK package.
For a local installation use:
cd ./coscine-python-sdk
py -m pip install .

It is usually not necessary to edit this file, since all package metadata
is defined in 'src/coscine/__about__.py'.
"""

###############################################################################
# Dependencies
###############################################################################

import setuptools

###############################################################################
# Module globals / Constants
###############################################################################

# Serves as a container for package metadata.
# Dynamically loaded from ./src/coscine/about.py
about = {}

# Read package metadata into $about
with open("src/coscine/__about__.py", "r", encoding="utf-8") as fd:
	exec(fd.read(), about)

# Use README.md as package description for display on PyPi
# and similar sourcecode hosting platforms.
# Prepends local links with the repository url to ensure display of
# images and other media on external platforms such as PyPi.
# Local links in README.md are marked with the prefix './data'.
with open("README.md", "r", encoding="utf-8") as fd:
	readme = fd.read()
	description = readme.replace("./data", \
		about["__url__"] + "-/raw/master/data")

###############################################################################
# Classes / Functions / Scripts
###############################################################################

setuptools.setup(
	name = about["__title__"],
	version = about["__version__"],
	description = about["__summary__"],
	long_description = description,
	long_description_content_type = "text/markdown",
	author = about["__author__"],
	author_email = about["__contact__"],
	license = about["__license__"],
	packages = setuptools.find_packages(where="src"),
	keywords = about["__keywords__"],
	package_data = {"coscine": ["data/*"]},
	install_requires = about["__dependencies__"],
	url = about["__url__"],
	project_urls = about["__project_urls__"],
	classifiers = [
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10",
		"Programming Language :: Python :: 3.11",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Topic :: Scientific/Engineering",
		"Topic :: Software Development",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Intended Audience :: Science/Research",
		"Intended Audience :: Developers",
		"Development Status :: 4 - Beta",
		"Typing :: Typed"
	],
	package_dir = {"": "src"},
	python_requires = about["__pyver__"]
)

###############################################################################
