# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scadi']

package_data = \
{'': ['*']}

install_requires = \
['cliff>=3.10.0,<4.0.0']

entry_points = \
{'cliff.scadi': ['inline = scadi.inline:Inline'],
 'console_scripts': ['scadi = scadi.main:main']}

setup_kwargs = {
    'name': 'scadi',
    'version': '0.1.3',
    'description': 'SCAD Inliner: Roll up OpenSCAD includes into the main file for easy sharing.',
    'long_description': '|pypiversion| |pypiwheel| |pypipyversions| |pypilicense| |pypidownloads| |precommit|\n\n=====\nscadi\n=====\n\nCommand-line tool for rolling up all includes into the main file of your model so that you can easily share it online.\n\nInstallation\n============\n\n::\n\n   pip3 install scadi\n\nUsage\n=====\n\n::\n\n   scadi inline ./my-model.scad\n\nThe above command will create a file called ``./inline-my-model.scad`` that can be shared on sites that have OpenSCAD customizers.\n\nLicense\n=======\n\nCopyright 2021 Nascent Maker, nascentmaker.com.\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of\nthis software and associated documentation files (the "Software"), to deal in\nthe Software without restriction, including without limitation the rights to\nuse, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of\nthe Software, and to permit persons to whom the Software is furnished to do so,\nsubject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS\nFOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR\nCOPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER\nIN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN\nCONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\nSupport me\n==========\n\nIf you found that this tool saved you some time and you want to give back, please consider using Ko-Fi to buy me a coffee.\n\n.. image:: https://ko-fi.com/img/githubbutton_sm.svg\n   :target: https://ko-fi.com/S6S7GJUG3\n   :alt: ko-fi\n\n.. |pypiversion| image:: https://img.shields.io/pypi/v/scadi\n   :alt: PyPI\n\n.. |pypipyversions| image:: https://img.shields.io/pypi/pyversions/scadi\n   :alt: PyPI - Python Version\n\n.. |pypiwheel| image:: https://img.shields.io/pypi/wheel/scadi\n   :alt: PyPI - Wheel\n\n.. |pypilicense| image:: https://img.shields.io/pypi/l/scadi\n   :alt: PyPI - License\n\n.. |pypidownloads| image:: https://img.shields.io/pypi/dm/scadi\n   :alt: PyPI - Downloads\n\n.. |precommit| image:: https://results.pre-commit.ci/badge/github/NascentMaker/scadi/main.svg\n   :target: https://results.pre-commit.ci/latest/github/NascentMaker/scadi/main\n   :alt: pre-commit.ci status\n',
    'author': 'Nascent Maker',
    'author_email': 'hello@nascentmaker.com',
    'maintainer': 'Nascent Maker',
    'maintainer_email': 'hello@nascentmaker.com',
    'url': 'https://nascentmaker.com/py/scadi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
