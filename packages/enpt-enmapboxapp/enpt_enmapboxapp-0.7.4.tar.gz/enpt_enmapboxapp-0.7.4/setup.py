#!/usr/bin/env python
# -*- coding: utf-8 -*-

# enpt_enmapboxapp, A QGIS EnMAPBox plugin providing a GUI for the EnMAP processing tools (EnPT)
#
# Copyright (C) 2018-2023 Daniel Scheffler (GFZ Potsdam, daniel.scheffler@gfz-potsdam.de)
#
# This software was developed within the context of the EnMAP project supported
# by the DLR Space Administration with funds of the German Federal Ministry of
# Economic Affairs and Energy (on the basis of a decision by the German Bundestag:
# 50 EE 1529) and contributions from DLR, GFZ and OHB System AG.
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License along
# with this program.  If not, see <https://www.gnu.org/licenses/>.

"""The setup script."""

from setuptools import setup, find_packages
import os
from pkgutil import find_loader
from warnings import warn


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

version = {}
with open("enpt_enmapboxapp/version.py", encoding='utf-8') as version_file:
    exec(version_file.read(), version)

req = [
    'psutil',
    # 'qgis',  # conda install -c conda-forge qgis
    # 'enmapbox'  # installation: https://enmap-box.readthedocs.io/en/latest/usr_section/usr_installation.html
    ]

req_setup = []

req_test = ['pytest', 'pytest-cov', 'pytest-reporter-html1', 'urlchecker']

req_doc = ['sphinx-argparse', 'sphinx_rtd_theme']

req_lint = ['flake8', 'pycodestyle', 'pydocstyle']

req_dev = req_setup + req_test + req_doc + req_lint

setup(
    author="Daniel Scheffler",
    author_email='danschef@gfz-potsdam.de',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description="A QGIS EnMAPBox plugin providing a GUI for the EnMAP processing tools (EnPT).",
    extras_require={
        "doc": req_doc,
        "test": req_test,
        "lint": req_lint,
        "dev": req_dev
    },
    install_requires=req,
    license="GPL-3.0-or-later",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords=['enpt_enmapboxapp', 'EnMAP', 'EnMAP-Box', 'hyperspectral', 'remote sensing', 'satellite',
              'processing chain'],
    name='enpt_enmapboxapp',
    packages=find_packages(include=['enpt_enmapboxapp']),
    python_requires='>=3.7',
    scripts=['bin/enpt_run_cmd.bat'] if os.name == 'nt' else ['bin/enpt_run_cmd.sh'],
    setup_requires=req_setup,
    test_suite='tests',
    tests_require=req_test,
    url='https://git.gfz-potsdam.de/EnMAP/GFZ_Tools_EnMAP_BOX/enpt_enmapboxapp',
    version=version['__version__'],
    zip_safe=False,
)


# check for missing dependencies #
##################################

installationlink = 'https://enmap-box.readthedocs.io/en/latest/usr_section/usr_installation.html'

# check for qgis
if not find_loader('qgis'):
    warn('You need to install QGIS to run the EnPT-EnMAPBox-App. See here for installation instructions: %s'
         % installationlink)

# check for enmapbox
if not find_loader('enmapbox'):
    warn('You need to install the EnMAP-Box to run the EnPT-EnMAPBox-App. See here for installation instructions: %s'
         % installationlink)
