# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wsiml']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'wsiml',
    'version': '0.0',
    'description': 'Project to support machine learning on whole slide images. Currently a placeholder in pre-alpha.',
    'long_description': 'None',
    'author': 'S. Joshua Swamidass',
    'author_email': 'swamidass@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
