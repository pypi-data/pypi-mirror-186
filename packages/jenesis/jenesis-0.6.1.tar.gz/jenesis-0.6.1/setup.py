# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['jenesis',
 'jenesis.cmd',
 'jenesis.cmd.add',
 'jenesis.cmd.keys',
 'jenesis.config',
 'jenesis.contracts',
 'jenesis.keyring',
 'jenesis.keyring.amino',
 'jenesis.keyring.infos',
 'jenesis.keyring.linux',
 'jenesis.keyring.macos',
 'jenesis.keyring.test',
 'jenesis.network',
 'jenesis.tasks']

package_data = \
{'': ['*']}

install_requires = \
['blessings>=1.7,<2.0',
 'cosmpy>=0.6.1,<0.7.0',
 'docker>=5.0.3,<6.1.0',
 'graphlib-backport>=1.0.3,<2.0.0',
 'jsonschema>=4.15.0,<5.0.0',
 'jwskate>=0.4.1,<0.6.0',
 'keyring>=23.9.0,<24.0.0',
 'makefun>=1.15.0,<2.0.0',
 'mkdocs-material>=8.3.9,<9.0.0',
 'mkdocs>=1.3.1,<2.0.0',
 'ptpython>=3.0.20,<4.0.0',
 'toml>=0.10.2,<0.11.0',
 'tqdm>=4.64.0,<5.0.0']

entry_points = \
{'console_scripts': ['jenesis = jenesis.cli:main']}

setup_kwargs = {
    'name': 'jenesis',
    'version': '0.6.1',
    'description': 'Command line tool for rapid CosmWasm-based smart contract development',
    'long_description': 'Jenesis is a command line tool for rapid contract and service development for the Fetch.ai blockchain ecosystem and other CosmWasm-enabled blockchains.\n\n# Installation\n\nInstall jenesis for Python 3.7 or newer via PyPI:\n\n```\npip install jenesis\n```\n\n# Getting started\n\n## Create a new project\n\n```\njenesis new my_project\n```\n\n## Initialize jenesis in an existing project directory\n\n```\njenesis init\n```\n\n## Compile contracts\n\n\n```\njenesis compile\n```\n',
    'author': 'Ed FitzGerald',
    'author_email': 'edward.fitzgerald@fetch.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
