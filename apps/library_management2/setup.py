from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in library_management2/__init__.py
from library_management2 import __version__ as version

setup(
	name="library_management2",
	version=version,
	description="library management 2",
	author="baset",
	author_email="b@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
