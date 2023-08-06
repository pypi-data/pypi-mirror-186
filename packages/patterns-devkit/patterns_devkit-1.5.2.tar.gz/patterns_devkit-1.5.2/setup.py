# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['patterns',
 'patterns.cli',
 'patterns.cli.commands',
 'patterns.cli.configuration',
 'patterns.cli.services',
 'patterns.node']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.0,<9.0.0',
 'platformdirs>=2.4.0,<3.0.0',
 'pydantic>=1.8.1,<2.0.0',
 'pyyaml>=6.0,<7.0',
 'requests>=2.27.1,<3.0.0',
 'rich>=12.0.1,<13.0.0',
 'ruyaml>=0.91.0,<0.92.0',
 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['patterns = patterns.cli.main:main']}

setup_kwargs = {
    'name': 'patterns-devkit',
    'version': '1.5.2',
    'description': 'Data pipelines from re-usable components',
    'long_description': 'None',
    'author': 'AJ Alt',
    'author_email': 'aj@patterns.app',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
