# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['correctimport']

package_data = \
{'': ['*']}

install_requires = \
['pathsingleton==0.1.0']

setup_kwargs = {
    'name': 'correctimport',
    'version': '0.1.0',
    'description': 'Fixing the imports for packaging',
    'long_description': '',
    'author': 'Yashesh Dasari',
    'author_email': 'yasheshdasari@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
