# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['forgecore', 'forgecore.default_files']

package_data = \
{'': ['*']}

install_requires = \
['click', 'python-dotenv']

entry_points = \
{'console_scripts': ['forge = forgecore.cli:cli']}

setup_kwargs = {
    'name': 'forge-core',
    'version': '1.0.0',
    'description': 'Core library for Forge',
    'long_description': '# forge-core\n\nAll Forge packages should depend on `forge-core`.\n\nIt provides the following:\n\n- the `forge` CLI (autodiscovers `forge-x` commands)\n- default Django `manage.py`, `wsgi.py`, and `asgi.py` files\n- the `Forge` class with path, tmp, and executable utils\n',
    'author': 'Dave Gaeddert',
    'author_email': 'dave.gaeddert@dropseed.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.forgepackages.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
