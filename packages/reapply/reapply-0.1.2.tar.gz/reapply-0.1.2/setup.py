# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['reapply', 'reapply.apply', 'reapply.captions', 'reapply.intent']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'reapply',
    'version': '0.1.2',
    'description': '',
    'long_description': '',
    'author': 'Kiran Gadhave',
    'author_email': 'kirangadhave2@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
