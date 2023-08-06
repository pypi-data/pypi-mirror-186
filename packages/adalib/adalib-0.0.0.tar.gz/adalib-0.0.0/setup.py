# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['adalib']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'adalib',
    'version': '0.0.0',
    'description': 'Dummy package containing nothing',
    'long_description': '# Adalib\n\nTODO\n',
    'author': 'Adamatics Aps',
    'author_email': 'info@adamatics.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
