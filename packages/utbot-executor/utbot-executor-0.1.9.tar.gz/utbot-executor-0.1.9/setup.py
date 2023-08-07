# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['utbot_executor']

package_data = \
{'': ['*']}

install_requires = \
['coverage>=6.5.0,<7.0.0', 'deep-serialization>=0.1.3,<0.2.0']

entry_points = \
{'console_scripts': ['utbot-executor = utbot_executor:utbot_executor']}

setup_kwargs = {
    'name': 'utbot-executor',
    'version': '0.1.9',
    'description': '',
    'long_description': '# UtBot Executor\n\nUtil for python code execution and state serialization.\n',
    'author': 'Vyacheslav Tamarin',
    'author_email': 'vyacheslav.tamarin@yandex.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
