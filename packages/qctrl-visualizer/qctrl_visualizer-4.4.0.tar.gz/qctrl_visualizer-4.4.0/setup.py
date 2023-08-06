# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qctrlvisualizer']

package_data = \
{'': ['*']}

install_requires = \
['qctrl-commons>=17.8.0,<18.0.0', 'toml>=0.10.0,<0.11.0']

extras_require = \
{':python_full_version >= "3.7.2" and python_version < "3.8"': ['matplotlib>=3.2,<3.5.2',
                                                                'numpy>=1.21.6,<2.0.0'],
 ':python_version >= "3.8" and python_version < "3.12"': ['matplotlib>=3.6.3',
                                                          'numpy>=1.23.5,<2.0.0']}

setup_kwargs = {
    'name': 'qctrl-visualizer',
    'version': '4.4.0',
    'description': 'Q-CTRL Visualizer',
    'long_description': '# Q-CTRL Visualizer\n\nProvides visualization of data for Q-CTRL’s Python products.\n',
    'author': 'Q-CTRL',
    'author_email': 'support@q-ctrl.com',
    'maintainer': 'Q-CTRL',
    'maintainer_email': 'support@q-ctrl.com',
    'url': 'https://q-ctrl.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.2,<3.12',
}


setup(**setup_kwargs)
