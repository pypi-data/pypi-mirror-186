# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['finary']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'finary',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Mathieu Clavier',
    'author_email': 'mathieu.clavier@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
