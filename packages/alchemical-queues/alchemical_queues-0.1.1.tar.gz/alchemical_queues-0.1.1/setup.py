# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['alchemical_queues', 'alchemical_queues.tasks']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1,<2', 'typing_extensions']

entry_points = \
{'console_scripts': ['alchemical_worker = alchemical_queues.tasks.cli:cli']}

setup_kwargs = {
    'name': 'alchemical-queues',
    'version': '0.1.1',
    'description': 'Task Queues on pure SQLAlchemy',
    'long_description': 'None',
    'author': 'Thijs Miedema',
    'author_email': 'mail@tmiedema.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
