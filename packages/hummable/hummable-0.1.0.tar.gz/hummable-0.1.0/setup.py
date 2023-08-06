# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hummable']

package_data = \
{'': ['*']}

install_requires = \
['bleak>=0.19.5,<0.20.0']

setup_kwargs = {
    'name': 'hummable',
    'version': '0.1.0',
    'description': 'Bluetooth BLE for Human Beings',
    'long_description': '# Bluetooth BLE for Human Beings\n\nThis is a simple library for interacting with BLE devices. It is\ndesigned to be easy to use and understand, and to be a good starting point for building your own BLE applications.\n\nThis library is based on [BLEAK](https://bleak.readthedocs.io/en/latest/).\n\n- [x] Discovering devices and simple filtering\n- [x] Reading GATT characteristics periodically\n- [x] Receiving notifications from GATT characteristics\n- [ ] Writing GATT characteristics\n\n',
    'author': 'Daniel Fett',
    'author_email': 'fett@danielfett.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
