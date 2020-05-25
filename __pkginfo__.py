# Copyright (C) 2019-2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

# This script based on https://github.com/rocky/python-uncompyle6/blob/master/__pkginfo__.py

import pathlib

__copyright__ = """
2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
"""

__version__ = "2020.05.06"

short_desc = 'description goes here'

__author__ = "Dominic Davis-Foster"
author_email = "dominic@davis-foster.co.uk"
modname = github_username = "domdfcoding"

web = github_url = f"https://github.com/{github_username}/{modname}.github.io"
project_urls = {
		"Documentation": f"https://{modname}.readthedocs.io",  # TODO: Make this link match the package version
		"Issue Tracker": f"{github_url}/issues",
		"Source Code": github_url,
		}

repo_root = pathlib.Path(__file__).parent

install_requires = (repo_root / "requirements.txt").read_text().split("\n")
long_description = (repo_root / "README.rst").read_text() + '\n'
