# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['gen_gender']

package_data = \
{'': ['*'], 'gen_gender': ['pkl/*']}

install_requires = \
['black>=22.12.0,<23.0.0',
 'debugpy>=1.6.5,<2.0.0',
 'pytest>=7.2.0,<8.0.0',
 'ruff>=0.0.220,<0.0.221',
 'stanza>=1.4.2,<2.0.0']

setup_kwargs = {
    'name': 'gen-gender',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'vmerkurev',
    'author_email': 'v.merkurev@promo-bot.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
