# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['zeal_cli', 'zeal_cli.zeal']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'beautifulsoup4>=4.10.0,<5.0.0',
 'lxml>=4.9.1,<5.0.0',
 'requests>=2.27.1,<3.0.0']

entry_points = \
{'console_scripts': ['zeal-cli = zeal_cli:main']}

setup_kwargs = {
    'name': 'zeal-cli',
    'version': '2.0.0.dev2',
    'description': '',
    'long_description': "# Zeal CLI\nZeal CLI is a command-line-interface for managing [Zeal](https://zealdocs.org/) docsets on Linux. It's syntax is roughly based on the basic syntax of the `apt` package manager, because Zeal CLI is basically a package manager for docsets.\n\n## Features\n- Simple, familiar command-line interface\n- Gets docsets from the same source as Zeal\n- Easy to install and use - no additional dependencies required.\n- Docsets can still be managed within the Zeal GUI\n- Free and Open-Source\n\n## Technologies\n- Python 3\n- PyInstaller\n\n## Usage\nView the [usage documentation](usage.md) for using instructions.\n\n## Contact\nTo submit a Bug Report or Feature Request, please open a [GitHub Issue](https://github.com/Morpheus636/zeal-cli/issues/new).\n\nTo ask a question or get support, you can join my [Discord Server](https://discord.morpheus636.com) or create a Discussions thread within this repository.\n\n## Contributing\nThis project is maintained my Morpheus636. Contribution guidelines for all of my projects can be found at https://docs.morpheus636.com/contributing\n\n## Credits\n- Zeal_CLI sources docsets from [Dash](https://kapeli.com/dash), just like Zeal. Special thanks to Dash's developer, [Kapeli](https://github.com/Kapeli) for granting me permission to use their docsets.\n\n# Copyright Notice\n© Copyright 2021-2022 Josh Levin ([Morpheus636](https://github.com/morpheus636))\n\nThis repository (and everything in it) is free software: you can redistribute it and/or modify\nit under the terms of the GNU General Public License as published by\nthe Free Software Foundation, either version 3 of the License, or\n(at your option) any later version.\n\nThis repository is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\nGNU General Public License for more details.\n\nYou should have received a copy of the GNU General Public License\nalong with this repository.  If not, see <https://www.gnu.org/licenses/>.\n",
    'author': 'Josh Levin',
    'author_email': 'morpheus636@morpheus636.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/morpheus636/zeal-cli',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
