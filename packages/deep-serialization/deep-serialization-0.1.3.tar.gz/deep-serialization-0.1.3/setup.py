# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deep_serialization']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['deep-serialization = '
                     'deep_serialization:deep_serialization']}

setup_kwargs = {
    'name': 'deep-serialization',
    'version': '0.1.3',
    'description': 'Automatic python objects JSON serialization',
    'long_description': '# Deep Serializer\n\nUtil can serialize almost python objects to json.\n',
    'author': 'Vyacheslav Tamarin',
    'author_email': 'vyacheslav.tamarin@yandex.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
