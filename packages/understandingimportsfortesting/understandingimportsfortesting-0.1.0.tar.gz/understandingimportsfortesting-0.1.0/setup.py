# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['understandingimportsfortesting']

package_data = \
{'': ['*']}

install_requires = \
['pathsingleton==0.1.0']

setup_kwargs = {
    'name': 'understandingimportsfortesting',
    'version': '0.1.0',
    'description': 'Fixing imports in Python',
    'long_description': 'None',
    'author': 'Yashesh Dasari',
    'author_email': 'yasheshdasari@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
