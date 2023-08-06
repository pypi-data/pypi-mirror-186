# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_idiom_sequence']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'nonebot-plugin-idiom-sequence',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Jerry080801',
    'author_email': 'jerry080801@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
