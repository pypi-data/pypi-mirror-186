# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simplepg']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.5.0,<0.6.0', 'psycopg2>=2.9.5,<3.0.0']

setup_kwargs = {
    'name': 'simplepg',
    'version': '0.1.3',
    'description': 'Simple PostgreSQL connections',
    'long_description': '# SimplePG\n\nSimple PostgreSQL connections',
    'author': 'Mysterious Ben',
    'author_email': 'datascience@tuta.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4.0',
}


setup(**setup_kwargs)
