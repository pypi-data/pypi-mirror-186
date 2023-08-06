# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['configloader']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'configloaders',
    'version': '0.1.1',
    'description': 'Load configurations from various types of configuration files',
    'long_description': 'Load configurations from various types of configuration files',
    'author': 'jawide',
    'author_email': 'jawide@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
