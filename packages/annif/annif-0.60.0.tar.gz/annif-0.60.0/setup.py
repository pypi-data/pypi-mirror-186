# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['annif',
 'annif.analyzer',
 'annif.backend',
 'annif.corpus',
 'annif.lexical',
 'annif.transform']

package_data = \
{'': ['*'],
 'annif': ['openapi/*',
           'static/*',
           'static/css/*',
           'static/fonts/*',
           'static/img/*',
           'static/js/*',
           'templates/*']}

install_requires = \
['click-log',
 'click>=8.1.0,<8.2.0',
 'connexion[swagger-ui]>=2.14.0,<2.15.0',
 'flask-cors',
 'flask>=1.0.4,<3',
 'gensim>=4.3.0,<4.4.0',
 'gunicorn',
 'joblib>=1.2.0,<1.3.0',
 'nltk',
 'numpy>=1.24.0,<1.25.0',
 'optuna>=2.10.0,<2.11.0',
 'python-dateutil',
 'rdflib>=4.2,<7.0',
 'scikit-learn==1.2.0',
 'scipy>=1.10.0,<1.11.0',
 'simplemma>=0.9.0,<0.10.0',
 'stwfsapy>=0.3.0,<0.4.0',
 'swagger_ui_bundle',
 'tomli>=2.0.0,<2.1.0']

extras_require = \
{'fasttext': ['fasttext-wheel==0.9.2'],
 'nn': ['tensorflow-cpu>=2.11.0,<2.12.0', 'lmdb==1.4.0'],
 'omikuji': ['omikuji>=0.5.0,<0.6.0'],
 'spacy': ['spacy>=3.4.0,<3.5.0'],
 'voikko': ['voikko'],
 'yake': ['yake==0.4.5']}

entry_points = \
{'console_scripts': ['annif = annif.cli:cli']}

setup_kwargs = {
    'name': 'annif',
    'version': '0.60.0',
    'description': 'Automated subject indexing and classification tool',
    'long_description': '<img src="https://annif.org/static/img/annif-RGB.svg" width="150">\n\n[![DOI](https://zenodo.org/badge/100936800.svg)](https://zenodo.org/badge/latestdoi/100936800)\n[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)\n[![CI/CD](https://github.com/NatLibFi/Annif/actions/workflows/cicd.yml/badge.svg)](https://github.com/NatLibFi/Annif/actions/workflows/cicd.yml)\n[![codecov](https://codecov.io/gh/NatLibFi/Annif/branch/master/graph/badge.svg)](https://codecov.io/gh/NatLibFi/Annif)\n[![Code Climate](https://codeclimate.com/github/NatLibFi/Annif/badges/gpa.svg)](https://codeclimate.com/github/NatLibFi/Annif)\n[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/NatLibFi/Annif/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/NatLibFi/Annif/?branch=master)\n[![codebeat badge](https://codebeat.co/badges/e496f151-93db-4f0e-9e30-bc3339e58ca4)](https://codebeat.co/projects/github-com-natlibfi-annif-master)\n[![CodeQL](https://github.com/NatLibFi/Annif/actions/workflows/codeql.yml/badge.svg)](https://github.com/NatLibFi/Annif/actions/workflows/codeql.yml)\n[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=NatLibFi_Annif&metric=alert_status)](https://sonarcloud.io/dashboard?id=NatLibFi_Annif)\n[![docs](https://readthedocs.org/projects/annif/badge/?version=latest)](https://annif.readthedocs.io/en/latest/index.html)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\nAnnif is an automated subject indexing toolkit. It was originally created as\na statistical automated indexing tool that used metadata from the\n[Finna.fi](https://finna.fi) discovery interface as a training corpus.\n\nThis repo contains a rewritten production version of Annif based on the\n[prototype](https://github.com/osma/annif). It is a work in progress, but\nalready functional for many common tasks.\n\n[Finto AI](https://ai.finto.fi/) is a service based on Annif; see the [source code for Finto AI](https://github.com/NatLibFi/FintoAI).\n\n# Basic install\n\nAnnif is developed and tested on Linux. If you want to run Annif on Windows or Mac OS, the recommended way is to use Docker (see below) or a Linux virtual machine.\n\nYou will need Python 3.8+ to install Annif.\n\nThe recommended way is to install Annif from\n[PyPI](https://pypi.org/project/annif/) into a virtual environment.\n\n    python3 -m venv annif-venv\n    source annif-venv/bin/activate\n    pip install annif\n\nYou will also need NLTK data files:\n\n    python -m nltk.downloader punkt\n\nStart up the application:\n\n    annif\n\nSee [Getting Started](https://github.com/NatLibFi/Annif/wiki/Getting-started)\nin the wiki for more details.\n\n# Docker install\n\nYou can use Annif as a pre-built Docker container. Please see the \n[wiki documentation](https://github.com/NatLibFi/Annif/wiki/Usage-with-Docker)\nfor details.\n\n# Development install\n\nA development version of Annif can be installed by cloning the [GitHub\nrepository](https://github.com/NatLibFi/Annif).\n[Poetry](https://python-poetry.org/) is used for managing dependencies and virtual environment for the development version.\n\nSee [CONTRIBUTING.md](CONTRIBUTING.md) for information on [unit tests](CONTRIBUTING.md#unit-tests), [code style](CONTRIBUTING.md#code-style), [development flow](CONTRIBUTING.md#development-flow) etc. details that are useful when participating in Annif development.\n\n## Installation and setup\n\nClone the repository.\n\nSwitch into the repository directory.\n\nInstall [pipx](https://pypa.github.io/pipx/) and Poetry if you don\'t have them. First pipx:\n\n    python3 -m pip install --user pipx\n    python3 -m pipx ensurepath\n\nOpen a new shell, and then install Poetry: \n\n    pipx install poetry\n\nPoetry can be installed also without pipx: check the [Poetry documentation](https://python-poetry.org/docs/master/#installation). \n\nCreate a virtual environment and install dependencies:\n\n    poetry install\n\nBy default development dependencies are included. Use option `-E` to install dependencies for selected optional features (`-E "extra1 extra2"` for multiple extras), or install all of them with `--all-extras`. By default the virtual environment directory is not under the project directory, but there is a [setting for selecting this](https://python-poetry.org/docs/configuration/#virtualenvsin-project).\n\nEnter the virtual environment:\n\n    poetry shell\n\nYou will also need NLTK data files:\n\n    python -m nltk.downloader punkt\n\nStart up the application:\n\n    annif\n\n# Getting help\n\nMany resources are available:\n\n * [Usage documentation in the wiki](https://github.com/NatLibFi/Annif/wiki)\n * [Annif tutorial](https://github.com/NatLibFi/Annif-tutorial) for learning to use Annif\n * [annif-users](https://groups.google.com/forum/#!forum/annif-users) discussion forum\n * [Internal API documentation](https://annif.readthedocs.io) on ReadTheDocs\n * [annif.org](https://annif.org) project web site\n\n# Publications / How to cite\n\nTwo articles about Annif have been published in peer-reviewed Open Access\njournals. The software itself is also archived on Zenodo and\nhas a [citable DOI](https://doi.org/10.5281/zenodo.5654173).\n\n## Citing the software itself\n\nSee "Cite this repository" in the details of the repository.\n\n## Annif articles\n<ul>\n<li> \nSuominen, O.; Inkinen, J.; Lehtinen, M., 2022. \nAnnif and Finto AI: Developing and Implementing Automated Subject Indexing.\nJLIS.It, 13(1), pp. 265–282. URL:\nhttps://www.jlis.it/index.php/jlis/article/view/437\n<details>\n<summary>See BibTex</summary>\n    \n    @article{suominen2022annif,\n      title={Annif and Finto AI: Developing and Implementing Automated Subject Indexing},\n      author={Suominen, Osma and Inkinen, Juho and Lehtinen, Mona},\n      journal={JLIS.it},\n      volume={13},\n      number={1},\n      pages={265--282},\n      year={2022},\n      doi = {10.4403/jlis.it-12740},\n      url={https://www.jlis.it/index.php/jlis/article/view/437},\n    }\n</details>\n</li> \n<li> \nSuominen, O.; Koskenniemi, I, 2022.\nAnnif Analyzer Shootout: Comparing text lemmatization methods for automated subject indexing.\nCode4Lib Journal, (54). URL:\nhttps://journal.code4lib.org/articles/16719\n<details>\n<summary>See BibTex</summary>\n\n    @article{suominen2022analyzer,\n      title={Annif Analyzer Shootout: Comparing text lemmatization methods for automated subject indexing},\n      author={Suominen, Osma and Koskenniemi, Ilkka},\n      journal={Code4Lib J.},\n      number={54},\n      year={2022},\n      url={https://journal.code4lib.org/articles/16719},\n    }\n</details>\n</li> \n<li> \nSuominen, O., 2019. Annif: DIY automated subject indexing using multiple\nalgorithms. LIBER Quarterly, 29(1), pp.1–25. DOI:\nhttps://doi.org/10.18352/lq.10285\n<details>\n<summary>See BibTex</summary>\n\n    @article{suominen2019annif,\n      title={Annif: DIY automated subject indexing using multiple algorithms},\n      author={Suominen, Osma},\n      journal={{LIBER} Quarterly},\n      volume={29},\n      number={1},\n      pages={1--25},\n      year={2019},\n      doi = {10.18352/lq.10285},\n      url = {https://doi.org/10.18352/lq.10285}\n    }\n</details>\n</li>\n</ul>\n\n# License\n\nThe code in this repository is licensed under Apache License 2.0, except for the\ndependencies included under `annif/static/css` and `annif/static/js`,\nwhich have their own licenses, see the file headers for details.\nPlease note that the [YAKE](https://github.com/LIAAD/yake) library is licended\nunder [GPLv3](https://www.gnu.org/licenses/gpl-3.0.txt), while Annif is\nlicensed under the Apache License 2.0. The licenses are compatible, but\ndepending on legal interpretation, the terms of the GPLv3 (for example the\nrequirement to publish corresponding source code when publishing an executable\napplication) may be considered to apply to the whole of Annif+Yake if you\ndecide to install the optional Yake dependency.\n',
    'author': 'National Library of Finland',
    'author_email': 'finto-posti@helsinki.fi',
    'maintainer': 'Osma Suominen',
    'maintainer_email': 'osma.suominen@helsinki.fi',
    'url': 'https://annif.org',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
