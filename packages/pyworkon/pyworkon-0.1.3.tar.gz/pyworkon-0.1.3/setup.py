# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyworkon',
 'pyworkon.interfaces',
 'pyworkon.interfaces.shell',
 'pyworkon.interfaces.shell.commands',
 'pyworkon.interfaces.tui',
 'pyworkon.interfaces.tui.widgets',
 'pyworkon.providers',
 'pyworkon.providers.bitbucket',
 'pyworkon.providers.github',
 'pyworkon.providers.gitlab']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'appdirs>=1.4.4,<2.0.0',
 'asgiref>=3.5.0,<4.0.0',
 'fuzzyfinder>=2.1.0,<3.0.0',
 'httpx>0.23.0',
 'orm[sqlite]>=0.3.1,<0.4.0',
 'prompt-toolkit>=3.0.28,<4.0.0',
 'pydantic>=1.10.0,<2.0.0',
 'python-nubia>=0.2b5,<0.3',
 'rich-click>=1.6.0,<2.0.0',
 'rich>=13.1.0,<14.0.0',
 'sqlalchemy>=1.4.41,<2.0.0,!=1.4.42',
 'uplink-httpx>=2.0,<3.0']

entry_points = \
{'console_scripts': ['pyworkon = pyworkon.__main__:run'],
 'pipx.run': ['rich-cli = pyworkon.__main__:run']}

setup_kwargs = {
    'name': 'pyworkon',
    'version': '0.1.3',
    'description': 'Software Development Project Management Tool',
    'long_description': "```bash\n$$$$$$$\\            $$\\      $$\\                     $$\\\n$$  __$$\\           $$ | $\\  $$ |                    $$ |\n$$ |  $$ |$$\\   $$\\ $$ |$$$\\ $$ | $$$$$$\\   $$$$$$\\  $$ |  $$\\  $$$$$$\\  $$$$$$$\\\n$$$$$$$  |$$ |  $$ |$$ $$ $$\\$$ |$$  __$$\\ $$  __$$\\ $$ | $$  |$$  __$$\\ $$  __$$\\\n$$  ____/ $$ |  $$ |$$$$  _$$$$ |$$ /  $$ |$$ |  \\__|$$$$$$  / $$ /  $$ |$$ |  $$ |\n$$ |      $$ |  $$ |$$$  / \\$$$ |$$ |  $$ |$$ |      $$  _$$<  $$ |  $$ |$$ |  $$ |\n$$ |      \\$$$$$$$ |$$  /   \\$$ |\\$$$$$$  |$$ |      $$ | \\$$\\ \\$$$$$$  |$$ |  $$ |\n\\__|       \\____$$ |\\__/     \\__| \\______/ \\__|      \\__|  \\__| \\______/ \\__|  \\__|\n          $$\\   $$ |\n          \\$$$$$$  |\n           \\______/\n```\n# PyWorkon\n\n[![PyPI version][pypi-version]][pypi-link]\n[![PyPI platforms][pypi-platforms]][pypi-link]\n[![GitHub Discussion][github-discussions-badge]][github-discussions-link]\n[![Conda-Forge][conda-badge]][conda-link]\n\nPyWorkon is a command line interface to enter and manage your software projects. It is powered by [Nubia](https://github.com/facebookincubator/python-nubia) and [Rich](https://github.com/Textualize/rich) for the shell interface and [Textual](https://github.com/Textualize/textual) for it's TUI.\n\n## Installation\n\nYou can install this library from [PyPI](https://pypi.org/project/pyworkon/) with `pip`:\n\n```bash\npython3 -m pip install pyworkon\n```\n\nor install it with `pipx`:\n```bash\npipx install pyworkon\n```\n\n\nYou can also use `pipx` to run the library without installing it:\n\n```bash\npipx run pyworkon\n```\n\n## Features\n\npyworkon currently provides the following features (get help with `-h` or `--help`):\n\n- Enter existing projects and start your favourite IDE (configurable)\n- Project (GIT Repository) management\n  - Create new projects from templates\n  - Delete or archive projects\n- Multiple (GIT hosting) providers\n  - [GitHub](http://github.com/) and [GitHub Enterprise](https://github.com/enterprise)\n  - [GitLab](https://gitlab.com/) and your self hosted GitLab instance(s)\n  - [Bitbucket](https://bitbucket.org/)\n- TUI (terminal user interface) and shell interface.\n- Highly customizable\n\n\n## Examples\n\n\n**`workon` command:**\n\nEnter an existing [GitHub project](https://github.com/chassing/pyworkon). (Github provider must be configured before hand)\n\n![GIF of the workon command](https://github.com/chassing/pyworkon/releases/download/v0.3.0/tui.gif)\n\n\n![GIF of the TUI functionality](https://github.com/chassing/pyworkon/releases/download/v0.3.0/tui.gif)\n\n\n## Development\n\n[![pre-commit.ci status][pre-commit-badge]][pre-commit-link]\n[![Code style: black][black-badge]][black-link]\n\nSee [CONTRIBUTING.md](https://github.com/chassing/pyworkon/blob/main/.github/CONTRIBUTING.md) for details on how to set up a development environment.\n\n\n[black-badge]:              https://img.shields.io/badge/code%20style-black-000000.svg\n[black-link]:               https://github.com/psf/black\n[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/pyworkon\n[conda-link]:               https://github.com/conda-forge/pyworkon-feedstock\n[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github\n[github-discussions-link]:  https://github.com/chassing/pyworkon/discussions\n[pypi-link]:                https://pypi.org/project/pyworkon/\n[pypi-platforms]:           https://img.shields.io/pypi/pyversions/pyworkon\n[pypi-version]:             https://badge.fury.io/py/pyworkon.svg\n",
    'author': 'Christian Assing',
    'author_email': 'chris@ca-net.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/chassing/pyworkon',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10.0,<4.0.0',
}


setup(**setup_kwargs)
