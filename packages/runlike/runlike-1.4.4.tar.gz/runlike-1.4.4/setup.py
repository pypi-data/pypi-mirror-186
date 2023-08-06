# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['runlike']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.1,<9.0.0']

entry_points = \
{'console_scripts': ['runlike = runlike.runlike:main']}

setup_kwargs = {
    'name': 'runlike',
    'version': '1.4.4',
    'description': 'Reverse-engineer docker run command line arguments based on running containers',
    'long_description': 'None',
    'author': 'Assaf Lavie',
    'author_email': 'a@assaflavie.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
