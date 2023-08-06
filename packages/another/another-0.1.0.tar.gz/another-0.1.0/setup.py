# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['another']

package_data = \
{'': ['*']}

install_requires = \
['granian>=0.2.1,<0.3.0', 'uvicorn>=0.20.0,<0.21.0']

setup_kwargs = {
    'name': 'another',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Another\n"Another" Python backend framework, for fun.',
    'author': 'Vahid Al',
    'author_email': 'thevahidal@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
