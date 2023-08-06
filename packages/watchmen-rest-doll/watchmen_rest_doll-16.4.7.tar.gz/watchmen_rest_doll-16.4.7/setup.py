# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['watchmen_rest_doll',
 'watchmen_rest_doll.admin',
 'watchmen_rest_doll.analysis',
 'watchmen_rest_doll.auth',
 'watchmen_rest_doll.console',
 'watchmen_rest_doll.gui',
 'watchmen_rest_doll.meta_import',
 'watchmen_rest_doll.sso',
 'watchmen_rest_doll.sso.saml',
 'watchmen_rest_doll.system',
 'watchmen_rest_doll.util']

package_data = \
{'': ['*']}

install_requires = \
['bcrypt>=3.2.0,<4.0.0',
 'passlib>=1.7.4,<2.0.0',
 'python-multipart>=0.0.5,<0.0.6',
 'watchmen-data-surface==16.4.7',
 'watchmen-indicator-surface==16.4.7',
 'watchmen-inquiry-surface==16.4.7',
 'watchmen-pipeline-surface==16.4.7']

extras_require = \
{'boto3': ['boto3>=1.24.20,<2.0.0'],
 'collector': ['watchmen-collector-kernel==16.4.7'],
 'kafka': ['kafka-python>=2.0.2,<3.0.0', 'aiokafka>=0.7.2,<0.8.0'],
 'mongodb': ['watchmen-storage-mongodb==16.4.7'],
 'mssql': ['watchmen-storage-mssql==16.4.7'],
 'mysql': ['watchmen-storage-mysql==16.4.7', 'cryptography>=36.0.2,<37.0.0'],
 'oracle': ['watchmen-storage-oracle==16.4.7'],
 'oss': ['watchmen-storage-oss==16.4.7'],
 'postgresql': ['watchmen-storage-postgresql==16.4.7'],
 'prometheus': ['starlette-prometheus>=0.9.0,<0.10.0'],
 'rabbit': ['aio-pika>=7.1.2,<8.0.0'],
 's3': ['watchmen-storage-s3==16.4.7'],
 'sso': ['python3-saml>=1.14.0,<2.0.0', 'cryptography>=36.0.2,<37.0.0'],
 'standard-ext-writer': ['requests>=2.27.1,<3.0.0'],
 'trino': ['watchmen-inquiry-trino==16.4.7']}

setup_kwargs = {
    'name': 'watchmen-rest-doll',
    'version': '16.4.7',
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
