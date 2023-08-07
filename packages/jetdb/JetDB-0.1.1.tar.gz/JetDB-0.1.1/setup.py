# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jetdb']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'jetdb',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Srijeet Aditya',
    'author_email': 'adityasrijeet12355@egmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
