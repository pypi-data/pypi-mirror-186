# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['twidge', 'twidge.widgets']

package_data = \
{'': ['*']}

install_requires = \
['rich>=13.2.0,<14.0.0', 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['twidge = twidge.__main__:cli']}

setup_kwargs = {
    'name': 'twidge',
    'version': '1.1.2',
    'description': 'Terminal Widgets.',
    'long_description': "\n# Twidge\n\nSimple terminal widgets for simple people.\n\nThis package is mostly intended for my own personal use, but have at it.\n\n\n## Quick Start\n\n#### Install\n\n```sh\npython -m pip install twidge\n```\n\n#### Echo Keypresses\n\n```sh\npython -m twidge echo\n```\n\n```python\nfrom twidge.widgets import echo\n\necho.run()\n```\n\n#### Text Editor\n\n```sh\npython -m twidge edit 'Hello World'\n```\n\n```python\nfrom twidge.widgets import editstr\n\ncontent = editstr.run('Hello World!')\n```\n\n#### Dictionary Editor\n\n```sh\npython -m twidge editdict name,email,username,password\n```\n\n```python\nfrom twidge.widgets import editdict\n\nfavorite_colors = {'Alice': 'red', 'Bob': 'blue'}\ncontent = editdict.run(favorite_colors)\n```\n\n## Issues\n\nMany - known and unknown. Issues welcome.\n",
    'author': 'Aidan Courtney',
    'author_email': 'aidanfc97@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/aidaco/twidge',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
