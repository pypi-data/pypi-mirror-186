# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gb_projects_pages']

package_data = \
{'': ['*']}

install_requires = \
['PyMySQL>=0.10.1,<0.11.0',
 'mysql-connector-python>=8.0.22,<9.0.0',
 'mysql-connector>=2.2.9,<3.0.0',
 'pysftp>=0.2.9,<0.3.0',
 'requests>=2.25.0,<3.0.0']

entry_points = \
{'console_scripts': ['gb_projects_pages = '
                     'gb_projects_pages.projects_pages:main']}

setup_kwargs = {
    'name': 'gb-projects-pages',
    'version': '1.0.4',
    'description': 'CLI command for updating the Ensembl projects pages',
    'long_description': 'None',
    'author': 'leannehaggerty',
    'author_email': 'leannehaggerty@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
