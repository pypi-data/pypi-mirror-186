# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['myepg_georgia']

package_data = \
{'': ['*']}

install_requires = \
['pyjwt>=2.5.0,<3.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'myepg-georgia',
    'version': '1.0.2',
    'description': '',
    'long_description': '',
    'author': 'Giorgi Kotchlamazashvili',
    'author_email': 'georgedot@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>3.8',
}


setup(**setup_kwargs)
