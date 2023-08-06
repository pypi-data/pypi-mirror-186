# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['koldstart']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'koldstart',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Burkay Gur',
    'author_email': 'burkay@fal.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
