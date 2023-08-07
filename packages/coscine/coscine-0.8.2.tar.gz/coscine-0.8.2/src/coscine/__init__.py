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
# Coscine Python SDK

The Coscine Python SDK is an open source python package providing
a pythonic interface to the Coscine REST API. It is compatible
with Python versions 3.7+ and has been released under the terms
of the MIT License.

Please note that this python module is developed and maintained
by the scientific community and even though Copyright remains with
RWTH Aachen, it is not an official service that RWTH Aachen
provides support for.

.. include:: ../docs/getting_started.md
.. include:: ../docs/usage.md
.. include:: ../docs/examples.md
.. include:: ../../CONTRIBUTING.md
"""

###############################################################################
# Dependencies
###############################################################################

import logging
from .client import Client, Settings
from .project import Project, ProjectMember, ProjectForm
from .resource import Resource, ResourceForm
from .object import FileObject, MetadataForm
from .graph import ApplicationProfile

###############################################################################

# Set up default logger to '/dev/null'
logging.getLogger("coscine").addHandler(logging.NullHandler())

###############################################################################
