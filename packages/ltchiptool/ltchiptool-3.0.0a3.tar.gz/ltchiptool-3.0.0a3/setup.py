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
{'gui': ['wxPython>=4.2.0,<5.0.0', 'pywin32>=305,<306']}

entry_points = \
{'console_scripts': ['ltchiptool = ltchiptool:cli']}

setup_kwargs = {
    'name': 'ltchiptool',
    'version': '3.0.0a3',
    'description': 'Tools for working with LT-supported IoT chips',
    'long_description': "# ltchiptool\n\nTools for working with LT-supported IoT chips.\n\n## What is this?\n\nThis repository is a collection of tools, used in the [LibreTuya project](https://github.com/kuba2k2/libretuya), that perform some chip-specific tasks, like packaging binary images or uploading firmware to the chip.\n\nSince v2.0.0, it contains a common, chip-independent CLI and API for interacting with supported chips in download mode (reading/writing flash).\n\n## Installation\n\nFrom PyPI:\n\n```shell\npip install ltchiptool\n```\n\nThis will install `ltchiptool` and `uf2tool` packages.\n\n## Usage\n\n```shell\n$ ltchiptool --help\nUsage: ltchiptool [OPTIONS] COMMAND [ARGS]...\n\n  Tools for working with LT-supported IoT chips\n\nOptions:\n  -v, --verbose         Output debugging messages (repeat to output more)\n  -T, --traceback       Print complete exception traceback\n  -t, --timed           Prepend log lines with timing info\n  -r, --raw-log         Output logging messages with no additional styling\n  -i, --indent INTEGER  Indent log messages using graph lines\n  -V, --version         Show the version and exit.\n  -h, --help            Show this message and exit.\n\nCommands:\n  dump      Capture or process device dumps\n  elf2bin   Generate firmware binaries from ELF file\n  flash     Flashing tool - reading/writing\n  link2bin  Link code to binary format\n  list      List boards, families, etc.\n  soc       Run SoC-specific tools\n  uf2       Work with UF2 files\n```\n\n## Flashing/dumping\n\nThere are three main commands used for flashing:\n- `ltchiptool flash file <FILE>` - detect file type based on its contents (i.e. chip from which a dump was acquired), similar to Linux `file` command\n- `ltchiptool flash read <FAMILY> <FILE>` - make a full flash dump of the connected device; specifying the family is required\n- `ltchiptool flash write <FILE>` - upload a file to the device; detects file type automatically (just like the `file` command above)\n\nSupported device families can be checked using `ltchiptool list families` command. In the commands above, you can use any of the family names (name/code/short name/etc).\n\nThe upload UART port and baud rate is detected automatically. To override it, use `-d COMx` or `-d /dev/ttyUSBx`. To change the target baud rate, use `-b 460800`.\nNote that the baud rate is changed after linking. Linking is performed using chip-default baud rate.\n\nIt's not required to specify chip family for writing files - `ltchiptool` tries to recognize contents of the file, and chooses the best settings automatically.\nIf you want to flash unrecognized/raw binaries (or fine-tune the flashing parameters), specify `-f <FAMILY>` and `-s <START OFFSET>`.\n\n## UF2 Example\n\n```shell\n$ ltchiptool uf2 info ./arduinotest_22.08.01_wb2l_BK7231T_lt0.8.0.uf2\nFamily: BK7231T / Beken 7231T\nTags:\n - BOARD: wb2l\n - DEVICE_ID: d80e20c2\n - LT_VERSION: 0.8.0\n - FIRMWARE: arduinotest\n - VERSION: 22.08.01\n - OTA_VERSION: 01\n - DEVICE: LibreTuya\n - BUILD_DATE: 6d08e862\n - LT_HAS_OTA1: 01\n - LT_HAS_OTA2: 00\n - LT_PART_1: app\n - LT_PART_2:\nData chunks: 1871\nTotal binary size: 478788\n```\n",
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
