# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['proximity', 'proximity.vendor']

package_data = \
{'': ['*']}

install_requires = \
['numpy', 'polliwog>=3.0.0a0,<4.0.0', 'rtree==1.0.1', 'scipy', 'vg>=2.0.0']

setup_kwargs = {
    'name': 'proximity',
    'version': '2.0.1',
    'description': 'Mesh proximity queries based on libspatialindex and rtree, extracted from Trimesh',
    'long_description': 'None',
    'author': 'Paul Melnikow',
    'author_email': 'github@paulmelnikow.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://proximity.readthedocs.io/en/stable/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
