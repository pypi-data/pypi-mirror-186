# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['retrack', 'retrack.engine', 'retrack.nodes', 'retrack.utils']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.5.2,<2.0.0', 'pydantic>=1.10.4,<2.0.0']

setup_kwargs = {
    'name': 'retrack',
    'version': '0.2.0',
    'description': 'A business rules engine',
    'long_description': None,
    'author': 'Gabriel Guarisa',
    'author_email': 'gabrielguarisa@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.16,<4.0.0',
}


setup(**setup_kwargs)
