# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ltchiptool',
 'ltchiptool.commands',
 'ltchiptool.commands.flash',
 'ltchiptool.gui',
 'ltchiptool.gui.panels',
 'ltchiptool.gui.work',
 'ltchiptool.models',
 'ltchiptool.soc',
 'ltchiptool.soc.ambz',
 'ltchiptool.soc.ambz.util',
 'ltchiptool.soc.ambz2',
 'ltchiptool.soc.ambz2.util',
 'ltchiptool.soc.bk72xx',
 'ltchiptool.soc.bk72xx.util',
 'ltchiptool.util',
 'uf2tool',
 'uf2tool.binpatch',
 'uf2tool.models',
 'uf2tool.upload']

package_data = \
{'': ['*']}

install_requires = \
['bk7231tools>=1.2.1,<2.0.0',
 'click>=8.1.3,<9.0.0',
 'colorama>=0.4.5,<0.5.0',
 'importlib-metadata>=4.12.0,<5.0.0',
 'prettytable>=3.3.0,<4.0.0',
 'pycryptodomex>=3.15.0,<4.0.0',
 'xmodem>=0.4.6,<0.5.0']

extras_require = \
{'gui': ['wxPython>=4.2.0,<5.0.0'],
 'gui:sys_platform == "win32"': ['pywin32>=305,<306']}

entry_points = \
{'console_scripts': ['ltchiptool = ltchiptool:cli']}

setup_kwargs = {
    'name': 'ltchiptool',
    'version': '3.0.0a5',
    'description': 'Tools for working with LT-supported IoT chips',
    'long_description': '# ltchiptool\n\nUniversal, easy-to-use GUI flashing/dumping tool for BK7231, RTL8710B and RTL8720C. Also contains some CLI utilities for binary firmware manipulation.\n\n<div align="center">\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![PyPI](https://img.shields.io/pypi/v/ltchiptool)](https://pypi.org/project/ltchiptool/)\n\n[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/libretuya/ltchiptool?include_prereleases&label=GUI%20release)](https://github.com/libretuya/ltchiptool/releases/latest)\n\n![Screenshot](.github/screenshot.png)\n</div>\n\n## What is this?\n\nThis repository is a collection of tools, used in the [LibreTuya project](https://github.com/kuba2k2/libretuya), that perform some chip-specific tasks, like packaging binary images or uploading firmware to the chip.\n\nSince v2.0.0, it contains a common, chip-independent CLI and API for interacting with supported chips in download mode (reading/writing flash).\n\nSince v3.0.0, it contains a beginner-friendly GUI for flashing firmware or dumping flash contents.\n\n# Usage/documentation\n<div style="text-align: center">\n\n## [Available here](https://docs.libretuya.ml/docs/flashing/tools/ltchiptool/)\n</div>\n\n## License\n\n```\nMIT License\n\nCopyright (c) 2022 Kuba Szczodrzyński\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.\n\n```\n',
    'author': 'Kuba Szczodrzyński',
    'author_email': 'kuba@szczodrzynski.pl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
