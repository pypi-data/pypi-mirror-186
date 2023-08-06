# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jara_utils', 'jara_utils.decorators', 'jara_utils.normalization']

package_data = \
{'': ['*']}

install_requires = \
['pytz>=2022.7.1,<2023.0.0', 'types-pytz>=2022.7.1.0,<2023.0.0.0']

setup_kwargs = {
    'name': 'jara-utils',
    'version': '1.0.0',
    'description': 'A package with basic stuff.',
    'long_description': '=================\nJara core package\n=================\n\n    Jara means bear in `Sesotho`_.\n\n.. image:: https://img.shields.io/badge/python-3.11.x-blue.svg\n    :alt: Python 3.11.x\n\n.. image:: https://img.shields.io/badge/code_style-flake8-brightgreen.svg\n    :alt: Flake8\n\n.. image:: https://img.shields.io/badge/dependency_manager-poetry-blueviolet.svg\n    :alt: Poetry\n\nWhy?\n~~~~\nSometimes I start a new project and I need to implement again same methods and after create tests for each method. This package will provide common methods like ``str_2_bool`` or other methods check ``README.rst`` for all methods available.\n\nHow to contribute to the package?\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nClone project locally and then:\n    * Install all dependencies including the test and the dev oanes: ``poetry install -E test -D``;\n    * Do changes in the project;\n    * Create unittests (please make sure  you will keep coverage to 100%);\n    * Run all sanity commands (pytest, flake8, mypy, bandit);\n    * Check if there is any duplicated or dead fixtures by running ``pytest`` with ``--dead-fixtures`` and ``--dup-fixtures``;\n\nNote: Run commands using poetry: ``poetry run <command>``;\n\nWhat you will find in this package?\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nBasically will contain utils methods to avoid write them in all projects. Some examples:\n\n* decorator to benchmark methods;\n* methods to handle environment variables;\n* some utils methods such as: ``snake_2_camel``, ``str_2_bool``.\n\n\n.. _Sesotho: https://en.wikipedia.org/wiki/Sotho_language\n',
    'author': 'Serban Senciuc',
    'author_email': 'senciuc.serban@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/senciucserban/jara-utils',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9.16,<4.0.0',
}


setup(**setup_kwargs)
