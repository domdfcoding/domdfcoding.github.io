import tabulate

header = """\
======================
Build Status
======================


"""

corner = "+"
side = "|"
top = "-"


class Project:
	def __init__(
			self, name, *,
			travis=True, travis_name=None, travis_site="com",
			appveyor=False, appveyor_name=None,
			rtfd=True, rtfd_name=None,
			# TODO: docker
			):
		self.name = str(name)
		self.travis = travis
		self.travis_site = travis_site
		self.appveyor = appveyor
		self.rtfd = rtfd
		
		if travis_name:
			self.travis_name = str(travis_name)
		else:
			self.travis_name = self.name
		
		if appveyor_name:
			self.appveyor_name = str(appveyor_name)
		else:
			self.appveyor_name = self.name

		if rtfd_name:
			self.rtfd_name = str(rtfd_name)
		else:
			self.rtfd_name = self.name

	def table_data(self):
		return [
				self.name,
				self.travis_badge if self.travis else '',
				self.rtfd_badge if self.rtfd else '',
				self.appveyor_badge if self.appveyor else '',
				]

	@property
	def appveyor_badge(self):
		return f"""
.. image:: https://img.shields.io/appveyor/build/domdfcoding/{self.appveyor_name}/master?logo=appveyor
    :target: https://ci.appveyor.com/project/domdfcoding/{self.appveyor_name}
    :alt: {self.name} build status (Appveyor)\
"""


	@property
	def travis_badge(self):
		if self.travis_site != "com":
			svg_url = f"https://img.shields.io/travis/domdfcoding/{self.travis_name}/master?logo=travis"
		else:
			svg_url = f"https://img.shields.io/travis/{self.travis_site}/domdfcoding/{self.travis_name}/master?logo=travis"
		
		return f"""
.. image:: {svg_url}
    :target: https://travis-ci.{self.travis_site}/domdfcoding/{self.travis_name}
    :alt: {self.name} build status (Travis CI)\
"""
	
	@property
	def rtfd_badge(self):
		
		return f"""
.. image:: https://readthedocs.org/projects/{self.rtfd_name}/badge/?version=latest
    :target: https://{self.rtfd_name}.readthedocs.io/en/latest/?badge=latest
    :alt: {self.name} documentation status\
"""

projects = [
		Project("domdf_python_tools"),
		Project("domdf_wxpython_tools"),
		Project("domdf_spreadsheet_tools"),
		Project("chemistry_tools"),
		Project("mathematical"),
		Project("Cawdrey", travis_site="org", rtfd_name="cawdrey"),
		Project("singledispatch-json"),

		Project("PyMassSpec", travis_site="org", appveyor=True, rtfd_name="pymassspec"),
		Project("pyms-nist-search", travis=False, appveyor=True),
		Project("msp2lib", appveyor=True),
		Project("rsc-on-this-day"),
		Project("custom_wx_icons"),
		Project("wxIconSaver"),
		Project("PySetWacom"),
		Project("dummy_wx"),
		]

table = tabulate.tabulate([project.table_data() for project in projects], tablefmt="rst")
print(table)

with open("source/build_status.rst", "w") as fp:
	fp.write(header)
	fp.write(table)
