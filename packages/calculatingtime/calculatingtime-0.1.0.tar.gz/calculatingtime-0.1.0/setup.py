# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['calculatingtime']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'calculatingtime',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
