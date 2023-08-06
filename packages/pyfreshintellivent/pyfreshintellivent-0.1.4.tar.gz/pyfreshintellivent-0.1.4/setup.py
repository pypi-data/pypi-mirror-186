# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyfreshintellivent']

package_data = \
{'': ['*']}

install_requires = \
['bleak-retry-connector>=2.1.0', 'bleak>=0.19.0']

setup_kwargs = {
    'name': 'pyfreshintellivent',
    'version': '0.1.4',
    'description': 'Manage Fresh Intellivent Sky bathroom ventilation fan',
    'long_description': '# pyfreshintellivent\nPython interface for Fresh Intellivent Sky bathroom Fan using Bluetooth Low Energy.\n\n# Features\n* Supports Windows 10, version 16299 (Fall Creators Update) or greater\n* Supports Linux distributions with BlueZ >= 5.43\n* OS X/macOS support via Core Bluetooth API, from at least OS X version 10.11\n\n# Projects using this library\n* [Fresh Intellivent Sky integration for Home Asssistant](https://github.com/angoyd/freshintelliventHacs)',
    'author': 'Ståle Storø Hauknes',
    'author_email': 'walnut-caprice.04@icloud.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/LaStrada/pyfreshintellivent',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
