# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['latexcor']

package_data = \
{'': ['*']}

install_requires = \
['chardet>=5.1.0,<6.0.0']

entry_points = \
{'console_scripts': ['latexcor = latexcor.cli:main']}

setup_kwargs = {
    'name': 'latexcor',
    'version': '0.1.7',
    'description': 'latex automation',
    'long_description': None,
    'author': 'David Couronné',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
