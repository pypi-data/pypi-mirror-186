# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['svd_by_viikoshh']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.24.1,<2.0.0']

entry_points = \
{'console_scripts': ['run_svd = main:main']}

setup_kwargs = {
    'name': 'svd-by-viikoshh',
    'version': '0.1.0',
    'description': 'SVD',
    'long_description': '# SVD',
    'author': 'viikoshh',
    'author_email': '105398417+viikoshh@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
