#  !/usr/bin/env python
#   -*- coding: utf-8 -*-
#
#  __main__.py
#
#  Copyright © 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
import os
import pathlib
import sys

from git_helper.core import GitHelper
from git_helper.__main__ import commit_changed_files
from git_helper.utils import get_git_status, check_git_status

from project_list import project_list

repos_dir = pathlib.Path("/media/VIDEO/Syncthing/Python/01 GitHub Repos").absolute()


def git_push(repo_path: pathlib.Path) -> int:
	"""
	Check the ``git`` status of the given repository

	:param repo_path: Path to the repository root
	:type repo_path: pathlib.Path

	:return:
	:rtype: int
	"""

	oldwd = os.getcwd()
	os.chdir(str(repo_path))
	ret = os.system("git push")
	os.chdir(oldwd)
	return ret


with open("status.rst", "w") as fp:
	for repo in project_list:

		repo_path = repos_dir / repo

		status, lines = check_git_status(repo_path)
		if not status:
			print("Git working directory is not clean:\n{}".format(
					"\n".join(lines)), file=sys.stderr)
			print(f"Skipping {repo_path}", file=sys.stderr)
			continue

		line = '='*len(repo)
		fp.write(f"\n{line}\n{repo}\n{line}\n")
		print(f"\n{line}\n{repo}\n{line}")

		status = get_git_status(repo_path)
		print(status)
		fp.write(status)

		gh = GitHelper(repos_dir / repo)
		managed_files = gh.run()
		commit_changed_files(gh.target_repo, managed_files, True)

		git_push(gh.target_repo)
