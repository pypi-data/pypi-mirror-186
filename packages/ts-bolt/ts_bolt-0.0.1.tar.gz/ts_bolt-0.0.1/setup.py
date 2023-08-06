# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ts_bolt', 'ts_bolt.datamodules']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'gluonts>=0.11.7,<0.12.0',
 'loguru>=0.6.0,<0.7.0',
 'pandas==1.5.2',
 'pytorch-lightning>=1.8.6,<2.0.0',
 'torch>=1.13.1,<2.0.0']

setup_kwargs = {
    'name': 'ts-bolt',
    'version': '0.0.1',
    'description': 'The Lightning Bolt for Time Series Data and Models',
    'long_description': 'None',
    'author': 'LM',
    'author_email': 'hi@leima.is',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
