# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['intent_prediction']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'intent-prediction',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Kiran Gadhave',
    'author_email': 'kirangadhave2@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
