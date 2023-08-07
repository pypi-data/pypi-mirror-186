# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ggvlib',
 'ggvlib.google',
 'ggvlib.hubspot',
 'ggvlib.io',
 'ggvlib.mixpanel',
 'ggvlib.reporting',
 'ggvlib.twilio']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3,<4.0.0',
 'db-dtypes>=1.0.4,<2.0.0',
 'google-api-python-client>=2.65.0,<3.0.0',
 'google-auth-oauthlib>=0.8.0,<0.9.0',
 'google-cloud-bigquery-storage>=2.16.2,<3.0.0',
 'google-cloud-bigquery>=3.3.5,<4.0.0',
 'google-cloud-scheduler>=2.7.3,<3.0.0',
 'google-cloud-secret-manager>=2.12.6,<3.0.0',
 'google-cloud-storage>=2.5.0,<3.0.0',
 'google-crc32c>=1.5.0,<2.0.0',
 'jsonschema>=4.17.0,<5.0.0',
 'loguru==0.5.0',
 'pandas>=1.5.1,<2.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'pyyaml>=6.0,<7.0',
 'sendgrid>=6.9.7,<7.0.0']

setup_kwargs = {
    'name': 'ggvlib',
    'version': '0.2.14',
    'description': '',
    'long_description': 'None',
    'author': 'Adam Hoffstein',
    'author_email': 'adam.hoffstein@gogox.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
