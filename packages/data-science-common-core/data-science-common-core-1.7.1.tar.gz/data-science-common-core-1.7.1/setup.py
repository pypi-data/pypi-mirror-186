# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['common']

package_data = \
{'': ['*']}

install_requires = \
['catboost>=1.0.6,<2.0.0',
 'db-dtypes>=1.0.2,<2.0.0',
 'google-cloud-bigquery-storage>=2.14.1,<3.0.0',
 'google-cloud-bigquery>=3.2.0,<4.0.0',
 'google-cloud-storage>=2.4.0,<3.0.0',
 'grpcio==1.51.1',
 'gspread-dataframe>=3.3.0,<4.0.0',
 'gspread>=5.4.0,<6.0.0',
 'imblearn>=0.0,<0.1',
 'importlib-metadata>=5.2.0,<6.0.0',
 'matplotlib>=3.5.2,<4.0.0',
 'pandas>=1.4.3,<2.0.0',
 'pgzip>=0.3.1,<0.4.0',
 'pkginfo>=1.8.3,<2.0.0',
 'protobuf>=3.20.1,<4.0.0',
 'python-dotenv>=0.20.0,<0.21.0',
 'scikit-learn>=1.1.1,<1.2.0',
 'scipy>=1.9.3,<2.0.0',
 'setuptools>=65.6.3,<66.0.0',
 'slack-sdk>=3.17.2,<4.0.0',
 'statsmodels>=0.13.2,<0.14.0',
 'toml>=0.10.2,<0.11.0',
 'tomli>=2.0.1,<3.0.0',
 'tqdm>=4.64.0,<5.0.0',
 'webencodings>=0.5.1,<0.6.0']

setup_kwargs = {
    'name': 'data-science-common-core',
    'version': '1.7.1',
    'description': 'Data Science Common Core',
    'long_description': None,
    'author': 'Unsal Gokdag',
    'author_email': 'unsal.gokdag@forto.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
