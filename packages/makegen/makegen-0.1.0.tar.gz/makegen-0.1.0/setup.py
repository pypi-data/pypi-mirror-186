# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['makegen']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'makegen',
    'version': '0.1.0',
    'description': 'Pythonic Implementation of Makefile Generator',
    'long_description': '# Makegen\n\nThis is a python implementation of a makefile generator.',
    'author': 'Goutham Krishna K V',
    'author_email': 'gauthamkrishna9991@live.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
