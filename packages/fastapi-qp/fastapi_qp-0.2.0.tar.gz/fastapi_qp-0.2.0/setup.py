# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_qp']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.75.1']

setup_kwargs = {
    'name': 'fastapi-qp',
    'version': '0.2.0',
    'description': '',
    'long_description': 'None',
    'author': 'Henrique Cunha',
    'author_email': 'henrycunh@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
