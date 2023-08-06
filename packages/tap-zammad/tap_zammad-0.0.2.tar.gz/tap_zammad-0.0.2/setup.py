# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tap_zammad', 'tap_zammad.tests']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25.1,<3.0.0', 'singer-sdk>=0.16.0,<0.17.0']

entry_points = \
{'console_scripts': ['tap-zammad = tap_zammad.tap:TapZammad.cli']}

setup_kwargs = {
    'name': 'tap-zammad',
    'version': '0.0.2',
    'description': 'tap-zammad is a Singer tap for Zammad, built with the Meltano SDK for Singer Taps.',
    'long_description': 'None',
    'author': 'Luis Ventura',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.1,<3.11',
}


setup(**setup_kwargs)
