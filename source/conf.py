#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#########################################################
# No need to change anything in this file, except to    #
# replace `package_name` with the actual name of        #
# your package.                                         #
#########################################################

import os
import re
import sys

sys.path.append(os.path.abspath('.'))
sys.path.append(os.path.abspath('..'))

from sphinx.locale import _

from __pkginfo__ import __author__, __version__, __copyright__
from __pkginfo__ import github_username, modname, github_url


rst_prolog = f""".. |pkgname| replace:: {modname}
.. |pkgname2| replace:: ``{modname}``
.. |browse_github| replace:: `Browse the GitHub Repository <{github_url}>`__
.. |ghurl| replace:: {github_url}
"""

project = modname
slug = re.sub(r'\W+', '-', modname.lower())
version = __version__
release = __version__
author = __author__
copyright = __copyright__
language = 'en'

extensions = [
		'sphinx_typo3_theme',
		'sphinx.ext.intersphinx',
		'sphinx.ext.autodoc',
		'sphinx.ext.mathjax',
		'sphinx.ext.viewcode',
		'sphinxcontrib.httpdomain',
		]

templates_path = ['_templates']
html_static_path = ['_static']
s = ['_templates']
source_suffix = '.rst'
exclude_patterns = []

master_doc = 'index'
suppress_warnings = ['image.nonlocal_uri']
pygments_style = 'default'

intersphinx_mapping = {
		'rtd': ('https://docs.readthedocs.io/en/latest/', None),
		'sphinx': ('http://www.sphinx-doc.org/en/stable/', None),
		'python': ('https://docs.python.org/3/', None),
		'domdf_python_tools': ('https://domdf_python_tools.rtfd.io/en/latest/', None),
		}

html_theme = 'sphinx_typo3_theme'
html_theme_path = ["../.."]
html_logo = "profile_pic.jpeg"
html_show_sourcelink = False  # True will show link to source

html_context = {
		# Github Settings
		"display_github": False,  # Integrate GitHub
		"github_user": github_username,  # Username
		"github_repo": modname,  # Repo name
		"github_version": "master",  # Version
		"conf_py_path": "/",  # Path in the checkout to the docs root
		"theme_docstypo3org": True,
		"theme_project_home": "https://www.github.com/domdfcoding"
		}

htmlhelp_basename = slug

latex_documents = [
		('index', '{0}.tex'.format(slug), modname, author, 'manual'),
		]

man_pages = [
		('index', slug, modname, [author], 1)
		]

texinfo_documents = [
		('index', slug, modname, author, slug, modname, 'Miscellaneous'),
		]


# Extensions to theme docs
def setup(app):
	from sphinx.domains.python import PyField
	from sphinx.util.docfields import Field
	
	app.add_object_type(
			'confval',
			'confval',
			objname='configuration value',
			indextemplate='pair: %s; configuration value',
			doc_field_types=[
					PyField(
							'type',
							label=_('Type'),
							has_arg=False,
							names=('type',),
							bodyrolename='class',
							),
					Field(
							'default',
							label=_('Default'),
							has_arg=False,
							names=('default',),
							),
					]
			)
