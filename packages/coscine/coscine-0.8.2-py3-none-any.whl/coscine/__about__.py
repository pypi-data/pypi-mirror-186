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
This file contains package metadata primarily intended for setup.py but
also accessed by various source files in src/.
"""

###############################################################################
# Module globals / Constants
###############################################################################

# Package title/name as it would appear in PyPi
__title__ = "coscine"

# Current package version
# Do not set version to 1.0.0 before Coscine end of pilot phase
__version__ = "0.8.2"

# Short package description
__summary__ = ("The Coscine Python SDK provides a pythonic interface to "
											"the Coscine REST API.")

# Package copyright owner
__author__ = "RWTH Aachen University"

# Coscine contact (Note: This is the official Coscine contact email!)
# Only for copyright claims, licensing issues or sourcecode hosting!
# Please do not direct bug reports or feature requests to that address!
# They are not responsible for the development, they "just" represent Coscine!
__contact__ = "coscine@itc.rwth-aachen.de"

# Package license
__license__ = "MIT License"

# Package keywords/tags (must be given as a list!)
__keywords__ = ["Coscine", "RWTH Aachen", "Research Data Management"]

# Package dependencies (must be given as a list!)
__dependencies__ = [
	"rdflib",
	"requests",
	"requests-toolbelt",
	"tqdm",
	"colorama",
	"prettytable",
	"appdirs",
	"python-dateutil"
]

# Python version required
__pyver__ = ">=3.7"

# Project url (official sourcecode hosting)
__url__ = ("https://git.rwth-aachen.de/coscine/community-features/"
											"coscine-python-sdk/")

# Additional urls for e.g. bug reports and documentation
__project_urls__ = {
	"Issues": __url__ + "-/issues",
	"Documentation": ("https://coscine.pages.rwth-aachen.de/"
					"community-features/coscine-python-sdk/")
}

###############################################################################
