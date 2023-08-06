# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['use_case_outcome']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'use-case-outcome',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Ross Bown',
    'author_email': 'rossbo@softcat.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
