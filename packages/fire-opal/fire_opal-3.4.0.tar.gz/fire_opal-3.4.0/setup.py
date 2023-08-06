# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fireopal', 'fireopal.core', 'fireopal.core.router', 'fireopal.functions']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.0,<9.0.0', 'qctrl-client>=3.0.0,<4.0.0', 'tenacity>=8.1.0,<9.0.0']

setup_kwargs = {
    'name': 'fire-opal',
    'version': '3.4.0',
    'description': 'Fire Opal Client',
    'long_description': "# Fire Opal Client\n\nThe Fire Opal Client package is a Python client for Q-CTRL's Fire Opal product.\n",
    'author': 'Q-CTRL',
    'author_email': 'support@q-ctrl.com',
    'maintainer': 'Q-CTRL',
    'maintainer_email': 'support@q-ctrl.com',
    'url': 'https://q-ctrl.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
