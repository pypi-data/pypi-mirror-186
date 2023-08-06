# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['modelos']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'modelos',
    'version': '0.1.0',
    'description': 'An operating system for machine learning',
    'long_description': '# model-os\nAn operating system for machine learning\n',
    'author': 'Patrick Barker',
    'author_email': 'patrickbarkerco@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
