#!/usr/bin/env python
from setuptools import setup, find_packages

with open('README.md', encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='nautobot-cable-utils',
    author='Gesellschaft für wissenschaftliche Datenverarbeitung mbH Göttingen',
    version='0.10.0',
    license='Apache-2.0',
    url='https://gitlab-ce.gwdg.de/gwdg-netz/nautobot-plugins/nautobot-cable-utils/',
    description='A Nautobot plugin for working with cables',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages('.'),
    include_package_data=True,
    install_requires=[
        "igraph"
    ],
    zip_safe=False,
)
