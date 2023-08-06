# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datacooker', 'datacooker.recipes', 'datacooker.utils', 'datacooker.variables']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.4,<2.0.0', 'pandas>=1.5.0,<2.0.0', 'scipy>=1.9.2,<2.0.0']

setup_kwargs = {
    'name': 'datacooker',
    'version': '0.4.0',
    'description': 'Library for data generation based on model specs (Recipes)',
    'long_description': '# Data Cooker\n\n[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=OStatsAA_data-cooker&metric=coverage)](https://sonarcloud.io/summary/new_code?id=OStatsAA_data-cooker)\n\n[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=OStatsAA_data-cooker&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=OStatsAA_data-cooker)\n',
    'author': 'Guilherme',
    'author_email': 'g.lisboa.oliveira@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.12',
}


setup(**setup_kwargs)
