# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fzf']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'krfzf-py',
    'version': '0.0.4',
    'description': 'Fzf.py - A Pythonic Fzf Wrapper',
    'long_description': '',
    'author': 'justfoolingaround',
    'author_email': 'kr.justfoolingaround@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
