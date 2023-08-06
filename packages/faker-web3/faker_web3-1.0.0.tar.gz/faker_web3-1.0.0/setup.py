# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['faker_web3']

package_data = \
{'': ['*']}

install_requires = \
['faker>=16.4.0,<17.0.0', 'web3>=5.31.3,<6.0.0']

setup_kwargs = {
    'name': 'faker-web3',
    'version': '1.0.0',
    'description': 'Web3-related fake data provider for Python Faker',
    'long_description': '# faker_web3\n\nWeb3-related fake data provider for Python Faker\n\n## Installation\n\n```\npip install faker_web3\n```\n\n## Usage:\n\n```python\nfrom faker import Faker\n\nfrom faker_web3 import Web3Provider\n\nfake = Faker()\nfake.add_provider(Web3Provider)\n```\n\n### Private keys\n\n```python\nfake.web3_private_key()\n# 0x1db498f960c133fd83351160687c91b6e41340959c9f03a810e8078f062562d1\n```\n',
    'author': 'Rares Stanciu',
    'author_email': 'rcstanciu@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
