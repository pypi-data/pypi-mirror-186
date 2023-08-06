# copyright 2004-2014 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact http://www.logilab.fr/ -- mailto:contact@logilab.fr
#
# This file is part of yams.
#
# yams is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# yams is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with yams. If not, see <http://www.gnu.org/licenses/>.
"""Yams packaging information."""
__docformat__ = "restructuredtext en"

# pylint: disable-msg=W0622

# package name
modname = "yams"

# release version
numversion = (0, 49, 1)
version = ".".join(str(num) for num in numversion)

# license and copyright
license = "LGPL"

# short and long description
description = "entity / relation schema"

# author name and email
author = "Logilab"
author_email = "devel@logilab.fr"

# home page
web = "https://forge.extranet.logilab.fr/open-source/%s" % modname

# mailing list
mailinglist = "mailto://python-projects@lists.logilab.org"

# executable
scripts = ["bin/yams-check", "bin/yams-view"]

install_requires = [
    "setuptools",
    "logilab-common >= 1.9.0",
    "python-dateutil",
]

classifiers = [
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
]
