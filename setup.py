from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in lapillaga_frappe/__init__.py
from lapillaga_frappe import __version__ as version

setup(
	name="lapillaga_frappe",
	version=version,
	description="Personal Portfolio Frappe App",
	author="Luis Pillaga",
	author_email="lpillaga@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
