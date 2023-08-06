# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['watchmen_rest_dqc',
 'watchmen_rest_dqc.admin',
 'watchmen_rest_dqc.monitor',
 'watchmen_rest_dqc.topic_profile',
 'watchmen_rest_dqc.util']

package_data = \
{'': ['*']}

install_requires = \
['watchmen-dqc==16.4.6', 'watchmen-rest==16.4.6']

extras_require = \
{'boto3': ['boto3>=1.24.20,<2.0.0'],
 'mongodb': ['watchmen-storage-mongodb==16.4.6'],
 'mssql': ['watchmen-storage-mssql==16.4.6'],
 'mysql': ['watchmen-storage-mysql==16.4.6'],
 'oracle': ['watchmen-storage-oracle==16.4.6'],
 'oss': ['watchmen-storage-oss==16.4.6'],
 'postgresql': ['watchmen-storage-postgresql==16.4.6'],
 's3': ['watchmen-storage-s3==16.4.6']}

setup_kwargs = {
    'name': 'watchmen-rest-dqc',
    'version': '16.4.6',
    'description': '',
    'long_description': 'None',
    'author': 'botlikes',
    'author_email': '75356972+botlikes456@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
