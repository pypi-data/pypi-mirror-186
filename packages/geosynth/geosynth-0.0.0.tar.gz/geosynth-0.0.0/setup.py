# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['geosynth']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'geosynth',
    'version': '0.0.0',
    'description': 'Geosynth Dataset.',
    'long_description': '',
    'author': 'Geomagical Labs',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
