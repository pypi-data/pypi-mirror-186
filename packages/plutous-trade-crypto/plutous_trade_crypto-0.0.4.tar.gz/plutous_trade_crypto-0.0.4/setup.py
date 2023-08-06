# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['plutous',
 'plutous.trade',
 'plutous.trade.crypto',
 'plutous.trade.crypto.exchanges']

package_data = \
{'': ['*']}

install_requires = \
['ccxt>=2.4.24', 'pandas>=1.5.2']

setup_kwargs = {
    'name': 'plutous-trade-crypto',
    'version': '0.0.4',
    'description': 'Plutous Crypto Trading Library',
    'long_description': '# plutous-trade-crypto\nPlutous Crypto Trading Library\n',
    'author': 'Cheun Hong',
    'author_email': 'cheunhong@plutous.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10',
}


setup(**setup_kwargs)
