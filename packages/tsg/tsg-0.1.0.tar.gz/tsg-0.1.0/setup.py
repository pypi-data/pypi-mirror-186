# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tsg']

package_data = \
{'': ['*']}

install_requires = \
['pygame>=2.1.2,<3.0.0']

entry_points = \
{'console_scripts': ['tsg = tsg:main']}

setup_kwargs = {
    'name': 'tsg',
    'version': '0.1.0',
    'description': 'A Typing Speed Game',
    'long_description': '# TSG\n\nTyping Speed Test\n\n## License\n\nMIT\n',
    'author': 'Eliaz Bobadilla',
    'author_email': 'ultirequiem@pm.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
