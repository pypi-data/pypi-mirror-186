# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_postgresql_reconnect', 'django_postgresql_reconnect.backend']

package_data = \
{'': ['*']}

install_requires = \
['Django>=3.2,<4.0']

setup_kwargs = {
    'name': 'django-postgresql-reconnect',
    'version': '1.0.3',
    'description': '',
    'long_description': 'None',
    'author': 'CloudBlue LLC',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/cloudblue/django-postgresql-reconnect',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
