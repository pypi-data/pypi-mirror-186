# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['geneity_oracle',
 'geneity_oracle.batch_request_engine',
 'geneity_oracle.interface',
 'geneity_oracle.query']

package_data = \
{'': ['*'], 'geneity_oracle': ['config/*', 'config/oracle_users/*']}

install_requires = \
['cx-oracle==8.0.1',
 'geneity-config>=20.10.0',
 'geneity-logger>=20.10.0',
 'toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'geneity-oracle',
    'version': '0.2.6',
    'description': 'Library for connections to oracle for geneity python3 apps',
    'long_description': None,
    'author': 'Trading Bonus and Bet Team',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
