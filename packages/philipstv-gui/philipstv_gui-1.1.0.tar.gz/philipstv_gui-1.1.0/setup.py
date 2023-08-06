# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['philipstv_gui']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0', 'philipstv>=0.4,<2', 'ttkbootstrap>=1.7.3,<2.0.0']

entry_points = \
{'console_scripts': ['philipstv-gui = philipstv_gui.__main__:main']}

setup_kwargs = {
    'name': 'philipstv-gui',
    'version': '1.1.0',
    'description': 'GUI remote for Philips Android-powered TVs.',
    'long_description': "# PhilipstvTV GUI\n\n[![CI](https://github.com/bcyran/philipstv-gui/workflows/CI/badge.svg?event=push)](https://github.com/bcyran/philipstv/actions?query=event%3Apush+branch%3Amaster+workflow%3ACI)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![pypi](https://img.shields.io/pypi/v/philipstv-gui)](https://pypi.org/project/philipstv-gui/)\n[![versions](https://img.shields.io/pypi/pyversions/philipstv-gui)](https://pypi.org/project/philipstv-gui/)\n[![license](https://img.shields.io/github/license/bcyran/philipstv-gui)](https://github.com/bcyran/philipstv-gui/blob/master/LICENSE)\n\nGUI remote for Philips Android-powered TVs.\n\n![PhilipstvTV GUI screenshots](https://github.com/bcyran/philipstv-gui/raw/master/philipstv-gui.png)\n\nFeatures:\n- Full remote emulation, all standard keys available.\n- List available channels and change between them.\n- List available applications and launch them.\n- Set Ambilight colors for each TV side separately.\n\n## Installation\n\n### PyPI\n```shell\n$ pip install philipstv-gui\n```\n\n### Arch Linux\n[philipstv-gui AUR package](https://aur.archlinux.org/packages/philipstv-gui) is available.\n\n## See also\n- [`philipstv`](https://github.com/bcyran/philipstv) - CLI and library for controlling Philips Android-powered TV's.\n",
    'author': 'Bazyli Cyran',
    'author_email': 'bazyli.cyran@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bcyran/philipstv-gui',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
