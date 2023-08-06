# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['glvars']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'pydantic>=1,<2',
 'python-gitlab>=3.9,<4.0',
 'typer[all]>=0.6.1']

entry_points = \
{'console_scripts': ['glvars = glvars.main:app']}

setup_kwargs = {
    'name': 'glvars',
    'version': '0.1.4',
    'description': 'CLI utility for managing variables in Gitlab',
    'long_description': 'None',
    'author': 'Alexey Tylindus',
    'author_email': 'a.tylindus@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
