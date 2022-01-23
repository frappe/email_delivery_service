from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in email_delivery_service/__init__.py
from email_delivery_service import __version__ as version

setup(
	name="email_delivery_service",
	version=version,
	description=".",
	author="Rutwik Hiwalkar",
	author_email="rutwik@frappe.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires,
)
