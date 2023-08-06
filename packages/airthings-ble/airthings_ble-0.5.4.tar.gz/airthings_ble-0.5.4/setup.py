# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['airthings_ble']

package_data = \
{'': ['*']}

install_requires = \
['bleak-retry-connector>=1.8.0', 'bleak>=0.15.1']

setup_kwargs = {
    'name': 'airthings-ble',
    'version': '0.5.4',
    'description': 'Manage Airthings BLE devices',
    'long_description': '# airthings-ble\n\nLibrary to control Airthings devices through BLE, primarily meant to be used in Home Assistant.\n',
    'author': 'Vincent Giorgi',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/vincegio/airthings-ble',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
