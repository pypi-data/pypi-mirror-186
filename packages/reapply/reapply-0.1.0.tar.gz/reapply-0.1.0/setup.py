# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reapply']

package_data = \
{'': ['*']}

install_requires = \
['intent-prediction>=0.1.0,<0.2.0']

setup_kwargs = {
    'name': 'reapply',
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
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
