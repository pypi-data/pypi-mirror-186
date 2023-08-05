# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['repocutter']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0',
 'arcon>=0.2.0,<0.3.0',
 'checksumdir>=1.2.0,<2.0.0',
 'cookiecutter>=2.1.1,<3.0.0',
 'gitspy>=0.3.0,<0.4.0',
 'object-colors>=2.2.0,<3.0.0',
 'tomli>=2.0.1,<3.0.0']

entry_points = \
{'console_scripts': ['repocutter = repocutter.__main__:main']}

setup_kwargs = {
    'name': 'repocutter',
    'version': '0.3.0',
    'description': 'Checkout repos to current cookiecutter config',
    'long_description': 'repocutter\n==========\n.. image:: https://img.shields.io/badge/License-MIT-yellow.svg\n    :target: https://opensource.org/licenses/MIT\n    :alt: License\n.. image:: https://img.shields.io/pypi/v/repocutter\n    :target: https://pypi.org/project/repocutter/\n    :alt: PyPI\n.. image:: https://github.com/jshwi/repocutter/actions/workflows/ci.yml/badge.svg\n    :target: https://github.com/jshwi/repocutter/actions/workflows/ci.yml\n    :alt: CI\n.. image:: https://results.pre-commit.ci/badge/github/jshwi/repocutter/master.svg\n   :target: https://results.pre-commit.ci/latest/github/jshwi/repocutter/master\n   :alt: pre-commit.ci status\n.. image:: https://github.com/jshwi/repocutter/actions/workflows/codeql-analysis.yml/badge.svg\n    :target: https://github.com/jshwi/repocutter/actions/workflows/codeql-analysis.yml\n    :alt: CodeQL\n.. image:: https://codecov.io/gh/jshwi/repocutter/branch/master/graph/badge.svg\n    :target: https://codecov.io/gh/jshwi/repocutter\n    :alt: codecov.io\n.. image:: https://readthedocs.org/projects/repocutter/badge/?version=latest\n    :target: https://repocutter.readthedocs.io/en/latest/?badge=latest\n    :alt: readthedocs.org\n.. image:: https://img.shields.io/badge/python-3.8-blue.svg\n    :target: https://www.python.org/downloads/release/python-380\n    :alt: python3.8\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :target: https://github.com/psf/black\n    :alt: Black\n.. image:: https://img.shields.io/badge/linting-pylint-yellowgreen\n    :target: https://github.com/PyCQA/pylint\n    :alt: pylint\n.. image:: https://snyk.io/test/github/jshwi/repocutter/badge.svg\n    :target: https://snyk.io/test/github/jshwi/repocutter/badge.svg\n    :alt: Known Vulnerabilities\n\nCheckout repos to current cookiecutter config\n---------------------------------------------\n\nCheckout one or more repos to current `cookiecutter <https://github.com/cookiecutter/cookiecutter>`_ config\n\nThis will make changes to local repositories, hopefully preserving their history\n\nIdeally only the working tree will change\n\nIgnored files should be backed up\n\nUse with caution\n\nUsage\n-----\n\n.. code-block:: console\n\n    usage: repocutter [-h] [-v] [-a] [-c] PATH [REPOS [REPOS ...]]\n\n    Checkout repos to current cookiecutter config\n\n    positional arguments:\n      PATH                path to cookiecutter template dir\n      REPOS               repos to run cookiecutter over\n\n    optional arguments:\n      -h, --help          show this help message and exit\n      -v, --version       show program\'s version number and exit\n      -a, --accept-hooks  accept pre/post hooks\n      -c, --gc            clean up backups from previous runs\n\nConfiguration\n-------------\n\nCurrently only written for a configuration exactly like below\n\nTechnically a repo would not need to be a `poetry <https://github.com/python-poetry/poetry>`_ project if the below section exists within its pyproject.toml file\n\nThis is the only use case at this time (If there are any other configurations you would like added please leave an `issue <https://github.com/jshwi/repocutter/issues>`_)\n\nEach repository\'s pyproject.toml file will be parsed for data to recreate its working tree\n\nA ``poetry`` section in the project\'s pyproject.toml file that looks like the following...\n\n.. code-block:: toml\n\n    [tool.poetry]\n    description = "Checkout repos to current cookiecutter config"\n    keywords = [\n      "config",\n      "cookiecutter",\n      "jinja2",\n      "repo",\n      "template"\n    ]\n    name = "repocutter"\n    version = "0.2.0"\n\n...will temporarily write to the ``cookiecutter`` project\'s cookiecutter.json file until the repo is created\n\n.. code-block:: json\n\n    {\n      "project_name": "repocutter",\n      "project_version": "0.2.0",\n      "project_description": "Checkout repos to current cookiecutter config",\n      "project_keywords": "config,cookiecutter,jinja2,repo,template",\n    }\n\nThe above configuration will reduce the diff, but it will still work if your config is not exactly the same\n\nWhy?\n----\nAs time goes on, and you use ``cookiecutter`` for new projects, you will make more and more changes to your ``cookiecutter`` repo\n\nYou will find these new project layouts are preferable to your older, more outdated, projects\n\nIf you have a project layout configured with ``cookiecutter`` then it\'s likely you will want this layout for all your projects\n\nConfiguring your existing projects manually is even more tedious than configuring a new project manually, especially if you have a lot of them\n\nBy checking out your projects to your configured ``cookiecutter`` layout, you can use whatever diff tool you use to rollback any undesired changes\n',
    'author': 'jshwi',
    'author_email': 'stephen@jshwisolutions.com',
    'maintainer': 'jshwi',
    'maintainer_email': 'stephen@jshwisolutions.com',
    'url': 'https://pypi.org/project/repocutter/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
