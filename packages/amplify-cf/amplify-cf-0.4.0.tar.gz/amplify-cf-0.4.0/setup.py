# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['amplify_cf']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'boto3-stubs[cloudformation,essential,appsync]>=1.24.56,<2.0.0',
 'boto3>=1.24.47,<2.0.0',
 'click>=8.1.3,<9.0.0',
 'inquirer>=2.10.0,<3.0.0',
 'python-box>=6.0.2,<7.0.0',
 'python-dotenv>=0.20.0,<0.21.0']

entry_points = \
{'console_scripts': ['amplify-cf = amplify_cf.cli:cmd']}

setup_kwargs = {
    'name': 'amplify-cf',
    'version': '0.4.0',
    'description': 'CloudFormation toolkit for amplify.',
    'long_description': None,
    'author': 'Epsy Engineering',
    'author_email': 'engineering@epsyhealth.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
