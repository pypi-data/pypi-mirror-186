# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyipatcher', 'pyipatcher.cli', 'pyipatcher.patchfinder']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0']

entry_points = \
{'console_scripts': ['pyipatcher = pyipatcher.__main__:cli']}

setup_kwargs = {
    'name': 'pyipatcher',
    'version': '1.0.2',
    'description': 'iOS ARM64 patchfinder & iOS ARM64 bootchain patcher',
    'long_description': "# pyipatcher\nIncomplete iOS bootchain patchers in Python\n## Notes\n* ~~It will be pushed to pip as a package later~~\n* You can now install it locally (see Installation)\n* patchfinder64 is ported from [xerub's patchfinder](https://github.com/xerub/patchfinder64)\n* kernelpatcher is ported from [palera1n team's fork of Kernel64Patcher](https://github.com/palera1n/Kernel64Patcher)\n## Installation\n```\ngit clone https://github.com/Mini-Exploit/pyipatcher\ncd pyipatcher\n./install.sh\n```\n## Usage\n```\n$ pyipatcher\npyipatcher version: 1.0.2\nUsage: pyipatcher [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  -h, --help  Show this message and exit.\n\nCommands:\n  kernelpatcher\n  ramdiskpatcher\n```\n## Future plan\n* Complete kernel patcher\n* Add iBoot patcher, ASR patcher, restored_external patcher\n## Credits\nThanks to [plx](https://github.com/justtryingthingsout) for helping me with many fixes\n",
    'author': 'mini_exploit',
    'author_email': '61931266+Mini-Exploit@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Mini-Exploit/pyipatcher',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
