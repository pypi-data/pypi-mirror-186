#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2023 Greg Albrecht <oss@undef.net>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author:: Greg Albrecht W2GMD <oss@undef.net>
#

"""ADSBCOT Setup."""

import os
import sys

import setuptools

__title__ = "adsbcot"
__version__ = "5.1.2"
__author__ = "Greg Albrecht W2GMD <oss@undef.net>"
__copyright__ = "Copyright 2023 Greg Albrecht"
__license__ = "Apache License, Version 2.0"


def publish():
    """Publish this package to pypi."""
    if sys.argv[-1] == "publish":
        os.system("python setup.py sdist")
        os.system("twine upload dist/*")
        sys.exit()


publish()


def read_readme(readme_file="README.rst") -> str:
    """Read the contents of the README file for use as a long_description."""
    readme: str = ""
    this_directory = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(this_directory, readme_file), encoding="UTF-8") as rmf:
        readme = rmf.read()
    return readme


setuptools.setup(
    version=__version__,
    name=__title__,
    packages=[__title__],
    package_dir={__title__: __title__},
    url=f"https://github.com/ampledata/{__title__}",
    entry_points={"console_scripts": [f"{__title__} = {__title__}.commands:main"]},
    description="ADS-B to Cursor on Target Gateway.",
    author="Greg Albrecht",
    author_email="oss@undef.net",
    package_data={"": ["LICENSE"]},
    license="Apache License, Version 2.0",
    long_description=read_readme(),
    zip_safe=False,
    include_package_data=True,
    install_requires=["aircot >= 1.2.0", "pytak >= 5.4.0", "aiohttp < 4.0.0"],
    extras_require={"with_pymodes": "pymodes >= 2.8"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
    keywords=["ADS-B", "ADSB", "Cursor on Target", "ATAK", "TAK", "CoT"],
)
