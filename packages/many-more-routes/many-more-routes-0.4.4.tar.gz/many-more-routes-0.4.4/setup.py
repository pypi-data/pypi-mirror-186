# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['many_more_routes']

package_data = \
{'': ['*']}

install_requires = \
['openpyxl>=3.0.9,<4.0.0', 'pydantic>=1.9.1,<2.0.0']

entry_points = \
{'console_scripts': ['mmrcli = many_more_routes.cli:cli']}

setup_kwargs = {
    'name': 'many-more-routes',
    'version': '0.4.4',
    'description': 'Routing tools for the More project',
    'long_description': None,
    'author': 'Kim TImothy Engh',
    'author_email': 'kimothy@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
