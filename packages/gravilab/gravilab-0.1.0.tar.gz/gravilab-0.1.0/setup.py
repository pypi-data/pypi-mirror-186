# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gravilab', 'gravilab.base', 'gravilab.formats', 'gravilab.input']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.19,<2.0',
 'obspy>=1.2.2,<2.0.0',
 'pandas>=1.1,<2.0',
 'spicypy>=0.4.1,<0.5.0']

extras_require = \
{':python_full_version <= "3.7.0"': ['importlib-metadata>=1.1.3']}

setup_kwargs = {
    'name': 'gravilab',
    'version': '0.1.0',
    'description': 'TODO',
    'long_description': 'None',
    'author': 'Artem Basalaev',
    'author_email': 'artem.basalaev@physik.uni-hamburg.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
