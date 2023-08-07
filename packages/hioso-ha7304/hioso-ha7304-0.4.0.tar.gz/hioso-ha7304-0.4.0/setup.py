# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hioso_ha7304']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=21.0.0,<23.0.0', 'cachetools>=5.2.1,<6.0.0', 'requests>=2.28.0,<3.0.0']

setup_kwargs = {
    'name': 'hioso-ha7304',
    'version': '0.4.0',
    'description': '',
    'long_description': None,
    'author': 'hexatester',
    'author_email': 'hexatester@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
