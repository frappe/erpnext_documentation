# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in erpnext_documentation/__init__.py
from erpnext_documentation import __version__ as version

setup(
	name='erpnext_documentation',
	version=version,
	description='To manage erpnext user manual',
	author='Frappe Technologies Pvt Ltd',
	author_email='developers@erpnext.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)