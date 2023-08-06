# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pynedra']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'dicomgenerator>=0.4.0,<0.5.0',
 'factory-boy>=3.2.1,<4.0.0',
 'pydicom>=2.3.0,<3.0.0',
 'pytest>=7.1.2,<8.0.0',
 'requests>=2.27.1,<3.0.0',
 'six>=1.15.0,<2.0.0',
 'urllib3>=1.26.9,<2.0.0',
 'xmltodict>=0.13.0,<0.14.0']

setup_kwargs = {
    'name': 'pynedra',
    'version': '0.1.6',
    'description': 'Pynedra',
    'long_description': 'None',
    'author': 'barbara73',
    'author_email': 'barbara.jesacher@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
