# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['streamlit_data_management']

package_data = \
{'': ['*']}

install_requires = \
['arrow>=1.2.3,<2.0.0',
 'pandas>=1.5.2,<2.0.0',
 'plotly>=5.12.0,<6.0.0',
 'streamlit>=1.17.0,<2.0.0',
 'supabase>=0.7.1,<0.8.0']

setup_kwargs = {
    'name': 'streamlit-data-management',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Denver Noell',
    'author_email': 'dnoell@ppeng.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
