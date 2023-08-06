# -*- coding: utf-8 -*-

# Copyright (C) 2022 Maxime Lecomte - David Sherman - Clémence Frioux - Inria BSO - Pleiade
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from glob import glob
from os.path import basename, splitext
from pathlib import Path

from setuptools import find_packages, setup

long_description = (Path(__file__).parent / "README.md").read_text()

setup(
    name             = 'CoCoMiCo',
    version          = '0.2.1',
    url              = 'https://gitlab.inria.fr/ccmc/CoCoMiCo',
    license          = 'GPLv3+',
    description      = 'COoperation and COmpetition potentials in MIcrobial COmunities',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author           = 'Maxime lecomte',
    author_email     = 'maxime.lecomte@inria.fr,clemence.frioux@inria.fr',
    project_urls={
        # "Documentation": "https://CoCoMiCo.gitlabpages.inria.fr/",
        # "Changelog": "https://CoCoMiCo.gitlabpages.inria.fr/en/latest/changelog.html",
        "Issue Tracker": "https://gitlab.inria.fr/CCMC/CoCoMiCo/issues",
    },
    keywords=[
        "microbial communities", "bioinformatics"
    ],
    classifiers      = [
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Unix',
        ],
    packages         = find_packages(where='src'),
    package_dir      = {'': 'src'},
    py_modules       = [splitext(basename(path))[0] for path in glob('src/*.py')],
    package_data={
        "cocomico": [
            "encodings/score.lp",
            "toys/communities.json",
            "toys/seeds.sbml",
            "toys/sbml/Com1Org1.sbml",
            "toys/sbml/Com1Org2.sbml",
            "toys/sbml/Com1Org2.sbml",
            "toys/sbml/Com1Org2.sbml",
            "toys/sbml/Com1Org3.sbml",
            "toys/sbml/Com2Org1.sbml",
            "toys/sbml/Com2Org2.sbml",
            "toys/sbml/Com2Org3.sbml",
            "toys/sbml/Com2Org4.sbml",
            ]
    },
    python_requires  = ">=3.8",
    entry_points     = {'console_scripts': ['cocomico = cocomico.__main__:main']},
    install_requires = ['clyngor_with_clingo', 'pandas', 'matplotlib']
)
