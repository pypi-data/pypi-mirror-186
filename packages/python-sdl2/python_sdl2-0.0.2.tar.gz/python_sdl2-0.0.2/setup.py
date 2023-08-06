# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pysdl2']

package_data = \
{'': ['*']}

install_requires = \
['pysdl2-dll>=2.26.2,<3.0.0']

setup_kwargs = {
    'name': 'python-sdl2',
    'version': '0.0.2',
    'description': 'python wrapper for SDL2',
    'long_description': '# pysdl2\npython wrapper for SDL2\n',
    'author': 'luzhixing12345',
    'author_email': 'luzhixing12345@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
