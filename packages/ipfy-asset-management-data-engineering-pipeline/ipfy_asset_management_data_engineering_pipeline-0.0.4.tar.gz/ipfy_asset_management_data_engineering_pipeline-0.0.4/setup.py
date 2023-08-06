# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ipfy_asset_management_data_engineering_pipeline',
 'ipfy_asset_management_data_engineering_pipeline.Boursorama',
 'ipfy_asset_management_data_engineering_pipeline.CreditAgricoleAlsace']

package_data = \
{'': ['*']}

install_requires = \
['ipfy-asset-management-pdf-to-table>=0.2.5,<0.3.0',
 'ipykernel>=6.20.1,<7.0.0',
 'numpy>=1.24.1,<2.0.0',
 'pandas>=1.5.2,<2.0.0',
 'pylint>=2.15.10,<3.0.0',
 'pypiserver>=1.5.1,<2.0.0',
 'pytest>=7.2.0,<8.0.0',
 'typing==3.5']

setup_kwargs = {
    'name': 'ipfy-asset-management-data-engineering-pipeline',
    'version': '0.0.4',
    'description': 'Python package to exctract table from pdf',
    'long_description': '# package-python-ipfy-asset-management-data-engineering-pipeline\nData Engineering pipeline that unify tables extracted from pdf files\n',
    'author': 'Yannick Flores',
    'author_email': 'yannick.flores1992@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
