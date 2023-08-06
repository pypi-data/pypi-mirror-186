# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['caronte_infra',
 'caronte_infra.database.config',
 'caronte_infra.database.connection']

package_data = \
{'': ['*']}

install_requires = \
['caronte-api-common>=0.2.0,<0.3.0',
 'motor>=3.1.1,<4.0.0',
 'pydantic>=1.10.4,<2.0.0']

setup_kwargs = {
    'name': 'caronte-api-infra',
    'version': '0.1.0',
    'description': 'Infraestructure package to integrate services',
    'long_description': '# Caronte-infra',
    'author': 'Giovani Liskoski Zanini',
    'author_email': 'giovanilzanini@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
