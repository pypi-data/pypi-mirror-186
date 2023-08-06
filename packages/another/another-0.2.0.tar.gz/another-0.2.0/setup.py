# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['another']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'another',
    'version': '0.2.0',
    'description': '',
    'long_description': '# Another\n"Another" Python backend framework, for fun.',
    'author': 'Vahid Al',
    'author_email': 'thevahidal@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
