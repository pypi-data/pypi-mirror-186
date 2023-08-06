#!/usr/bin/env python
from setuptools import setup, find_packages

with open('README.md', encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='nautobot-sfp-inventory',
    author='Gesellschaft für wissenschaftliche Datenverarbeitung mbH Göttingen',
    author_email="netzadmin@gwdg.de",
    version='0.5.0',
    license='Apache-2.0',
    url='https://gitlab-ce.gwdg.de/gwdg-netz/nautobot-plugins/nautobot-sfp-inventory',
    description='A Nautobot plugin for SFP inventory management',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages('.'),
    include_package_data=True,
    zip_safe=False,
)
