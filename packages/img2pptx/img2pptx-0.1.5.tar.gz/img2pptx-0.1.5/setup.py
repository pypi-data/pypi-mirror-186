# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['img2pptx']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'python-pptx>=0.6.21,<0.7.0']

entry_points = \
{'console_scripts': ['img2pptx = img2pptx.img2pptx:create_pptx']}

setup_kwargs = {
    'name': 'img2pptx',
    'version': '0.1.5',
    'description': '',
    'long_description': None,
    'author': 'MasterGowen',
    'author_email': 'mastergowen@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/MasterGowen/img-to-pptx',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>3.7,<4.0',
}


setup(**setup_kwargs)
