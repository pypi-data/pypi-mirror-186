# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fwatch']

package_data = \
{'': ['*']}

install_requires = \
['pathspec>=0.10.3,<0.11.0']

entry_points = \
{'console_scripts': ['fwatch = fwatch.fwatch:main']}

setup_kwargs = {
    'name': 'fwatch',
    'version': '0.1.0',
    'description': 'A very simple file watcher.',
    'long_description': '# fwatch\n\nA very simple file watcher.\n',
    'author': 'Wolf Honore',
    'author_email': 'wolfhonore@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/whonore/fwatch',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
