# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['micropub']

package_data = \
{'': ['*']}

install_requires = \
['indieauth>=0.0',
 'microformats>=0.0',
 'requests-toolbelt>=0.10.1,<0.11.0',
 'requests>=2.28.1,<3.0.0',
 'txtint>=0.0']

entry_points = \
{'console_scripts': ['micropub = micropub.__main__:main']}

setup_kwargs = {
    'name': 'micropub',
    'version': '0.1.0',
    'description': 'utilities to help implement Micropub servers and clients',
    'long_description': 'None',
    'author': 'Angelo Gladding',
    'author_email': 'angelo@ragt.ag',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
