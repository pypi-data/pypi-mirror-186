# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pysportsdb']

package_data = \
{'': ['*']}

install_requires = \
['mock>=5.0.1,<6.0.0', 'requests>=2.28.2,<3.0.0']

setup_kwargs = {
    'name': 'pysportsdb',
    'version': '0.1.0',
    'description': "An simple Python interface to thesportsdb.com's API",
    'long_description': 'pySportsDB\n=========\n\n[![Build Status](https://ci.unbl.ink/api/badges/secstate/pysportsdb/status.svg)](https://ci.unbl.ink/secstate/pysportsdb)\n\nA simple pythonic interface to thesportsdb.com sports data.\n',
    'author': 'Colin Powell',
    'author_email': 'colin@unbl.ink',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
