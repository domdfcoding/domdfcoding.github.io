# stdlib
from git_helper import readme
import git_helper.readme
import pathlib
import re

# 3rd party
import git_helper.readme
from git_helper.core import GitHelper
from jinja2 import BaseLoader, Environment


repos_dir = pathlib.Path("/media/VIDEO/Syncthing/Python/01 GitHub Repos").absolute()
projects_file = pathlib.Path("/media/VIDEO/Syncthing/Python/00 Projects/domdfcoding.github.io/source/projects.rst")

links_block_template = Environment(loader=BaseLoader).from_string("""\
.. start links {{ unique_name.lstrip("_") }}

View the project on `GitHub <https://github.com/{{ username }}/{{ repo_name }}>`_.
Read the `documentation <https://{{ repo_name.lower() }}.rtfd.io>`_.

.. end links
""")


def create_links_block(
		username, repo_name, unique_name=''):
	if unique_name:
		unique_name = f"_{unique_name}"
	return links_block_template.render(
			username=username, repo_name=repo_name, unique_name=unique_name)


def populate_projects(templates):
	"""

	:param templates:
	:type templates: jinja2.Environment
	"""

	shields_block = git_helper.readme.create_shields_block(
			"domdfcoding",
			templates.globals["repo_name"],
			templates.globals["version"],
			templates.globals["enable_conda"],
			templates.globals["enable_tests"],
			templates.globals["travis_site"],
			templates.globals["pypi_name"],
			templates.globals["import_name"],
			)

	if templates.globals["license"] == "GNU General Public License v2 (GPLv2)":
		shields_block.replace(
				f"https://img.shields.io/github/license/domdfcoding/{templates.globals['repo_name']}",
				"https://img.shields.io/badge/license-GPLv2-orange")

	links_block = create_links_block("domdfcoding", templates.globals["repo_name"], templates.globals["import_name"])

	unique_name = templates.globals["import_name"].replace("_", "\\_")
	projects = projects_file.read_text()

	if f"""\
{templates.globals["modname"]}
-----""" not in projects:
		projects += f"""
{templates.globals["modname"]}
{'-' * (len(templates.globals["modname"]) + 5)}

.. description goes here

.. start links {templates.globals['import_name']}
.. end links {templates.globals['import_name']}

.. start shields {templates.globals['import_name']}
.. end shields {templates.globals['import_name']}

"""
	
	projects = re.sub(
			fr'(?s)(\.\. start shields {unique_name})(.*?)(\.\. end shields)',
			shields_block,
			projects
			)

	projects = re.sub(
			fr'(?s)(\.\. start links {unique_name})(.*?)(\.\. end links)',
			links_block,
			projects
			)

	with projects_file.open("w") as fp:
		fp.write(projects)


def depopulate_projects(templates):
	"""

	:param templates:
	:type templates: jinja2.Environment
	"""

	unique_name = templates.globals["import_name"].replace("_", "\\_")
	projects = projects_file.read_text()

	projects = re.sub(
			fr'(?s)(\.\. start shields {unique_name})(.*?)(\.\. end shields)',
			f".. start shields {templates.globals['import_name']}\n.. end shields",
			projects,
			)

	projects = re.sub(
			fr'(?s)(\.\. start links {unique_name})(.*?)(\.\. end links)',
			f".. start links {templates.globals['import_name']}\n.. end links",
			projects,
			)

	with projects_file.open("w") as fp:
		fp.write(projects)


if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser(description='')
	parser.add_argument('--populate', action="store_true", default=False,
						help='Populate the `projects.rst` file.')
	parser.add_argument('--depopulate', action="store_true", default=False,
						help='Depopulate the `projects.rst` file to make for easier editing.')

	args = parser.parse_args()

	for repo in [
			"domdf_python_tools",
			"domdf_wxpython_tools",
			"domdf_spreadsheet_tools",
			"chemistry_tools",
			"mathematical",
			"cawdrey",
			"singledispatch-json",
			"git_helper",
			# "pyms-github",
			# "msp2lib",
			"extras_require",
			# "notebook2script",
			]:
		repo_path = repos_dir / repo
		gh = GitHelper(repo_path)

		if args.depopulate:
			depopulate_projects(gh.templates)
		else:
			populate_projects(gh.templates)

