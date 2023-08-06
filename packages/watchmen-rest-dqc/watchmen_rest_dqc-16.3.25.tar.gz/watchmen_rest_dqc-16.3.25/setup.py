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
['watchmen-dqc==16.3.25', 'watchmen-rest==16.3.25']

extras_require = \
{'mongodb': ['watchmen-storage-mongodb==16.3.25'],
 'mssql': ['watchmen-storage-mssql==16.3.25'],
 'mysql': ['watchmen-storage-mysql==16.3.25'],
 'oracle': ['watchmen-storage-oracle==16.3.25'],
 'oss': ['watchmen-storage-oss==16.3.25'],
 'postgresql': ['watchmen-storage-postgresql==16.3.25'],
 's3': ['watchmen-storage-s3==16.3.25']}

setup_kwargs = {
    'name': 'watchmen-rest-dqc',
    'version': '16.3.25',
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
