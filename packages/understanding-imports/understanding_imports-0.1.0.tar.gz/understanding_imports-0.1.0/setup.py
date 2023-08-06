# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['understanding_imports']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'understanding-imports',
    'version': '0.1.0',
    'description': '',
    'long_description': 'Hey, this is a test.',
    'author': 'Yashesh Dasari',
    'author_email': 'ydasari@thornhillmedical.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
