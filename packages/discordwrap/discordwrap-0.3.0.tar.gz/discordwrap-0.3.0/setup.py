# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['discordwrap']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'discordwrap',
    'version': '0.3.0',
    'description': '',
    'long_description': 'None',
    'author': 'josh',
    'author_email': 'josh@mjbrowns.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
