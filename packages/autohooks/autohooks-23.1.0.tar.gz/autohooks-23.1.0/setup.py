# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['autohooks',
 'autohooks.api',
 'autohooks.cli',
 'autohooks.precommit',
 'tests',
 'tests.api',
 'tests.api.git',
 'tests.cli',
 'tests.precommit']

package_data = \
{'': ['*']}

modules = \
['CHANGELOG', 'poetry']
install_requires = \
['pontos>=22.8.0', 'rich>=12.5.1', 'tomlkit>=0.5.11']

entry_points = \
{'console_scripts': ['autohooks = autohooks.cli:main']}

setup_kwargs = {
    'name': 'autohooks',
    'version': '23.1.0',
    'description': 'Library for managing git hooks',
    'long_description': '![Greenbone Logo](https://www.greenbone.net/wp-content/uploads/gb_new-logo_horizontal_rgb_small.png)\n# Autohooks <!-- omit in toc -->\n\n[![PyPI release](https://img.shields.io/pypi/v/autohooks.svg)](https://pypi.org/project/autohooks/)\n[![Build and test Python package](https://github.com/greenbone/autohooks/actions/workflows/ci-python.yml/badge.svg)](https://github.com/greenbone/autohooks/actions/workflows/ci-python.yml)\n[![codecov](https://codecov.io/gh/greenbone/autohooks/branch/main/graph/badge.svg?token=9IX7ucaFwj)](https://codecov.io/gh/greenbone/autohooks)\n\nLibrary for managing and writing [git hooks](https://git-scm.com/docs/githooks)\nin Python.\n\nLooking for automatic formatting or linting, e.g., with [black] and [pylint],\nwhile creating a git commit using a pure Python implementation?\nWelcome to **autohooks**!\n\n- [Why?](#why)\n- [Solution](#solution)\n- [Requirements](#requirements)\n- [Plugins](#plugins)\n- [Installing autohooks](#installing-autohooks)\n- [Maintainer](#maintainer)\n- [Contributing](#contributing)\n- [License](#license)\n\n## Why?\n\nSeveral outstanding libraries for managing and executing git hooks exist already.\nTo name a few: [husky](https://github.com/typicode/husky),\n[lint-staged](https://github.com/okonet/lint-staged),\n[precise-commits](https://github.com/nrwl/precise-commits) or\n[pre-commit](https://github.com/pre-commit/pre-commit).\n\nHowever, they either need another interpreter besides python (like husky) or are\ntoo ambiguous (like pre-commit). pre-commit is written in python but has support\nhooks written in all kind of languages. Additionally, it maintains the dependencies by\nitself and does not install them in the current environment.\n\n## Solution\n\nautohooks is a pure python library that installs a minimal\n[executable git hook](https://github.com/greenbone/autohooks/blob/main/autohooks/precommit/template).\nIt allows the decision of how to maintain the hook dependencies\nby supporting different modes.\n\n![Autohooks](https://raw.githubusercontent.com/greenbone/autohooks/main/autohooks.gif)\n\n## Requirements\n\nPython 3.7+ is required for autohooks.\n\n## Plugins\n\n* Python code formatting via [black](https://github.com/greenbone/autohooks-plugin-black)\n\n* Python code formatting via [autopep8](https://github.com/LeoIV/autohooks-plugin-autopep8)\n\n* Python code linting via [pylint](https://github.com/greenbone/autohooks-plugin-pylint)\n\n* Python code linting via [flake8](https://github.com/greenbone/autohooks-plugin-flake8)\n\n* Python import sorting via [isort](https://github.com/greenbone/autohooks-plugin-isort)\n\n* Running tests via [pytest](https://github.com/greenbone/autohooks-plugin-pytest/)\n\n## Installing autohooks\n\nQuick installation of [pylint] and [black] plugins using [poetry]:\n\n```shell\npoetry add --dev autohooks autohooks-plugin-black autohooks-plugin-pylint\npoetry run autohooks activate --mode poetry\npoetry run autohooks plugins add autohooks.plugins.black autohooks.plugins.pylint\n```\n\nThe output of `autohooks activate` should be similar to\n```\n ✓ autohooks pre-commit hook installed at /autohooks-test/.git/hooks/pre-commit using poetry mode.\n```\n\nAutohooks has an extensible plugin model. Each plugin provides different\nfunctionality which often requires to install additional dependencies.\n\nFor managing these dependencies currently three modes are supported by\nautohooks:\n\n* `pythonpath` for dependency management via [pip]\n* `poetry` for dependency management via [poetry] (recommended)\n* `pipenv` for dependency management via [pipenv]\n\nThese modes handle how autohooks, the plugins and their dependencies are loaded\nduring git hook execution.\n\nIf no mode is specified in the [`pyproject.toml` config file](#configure-mode-and-plugins-to-be-run)\nand no mode is set during [activation](#activating-the-git-hooks), autohooks\nwill use the [pythonpath mode](#pythonpath-mode) by default.\n\nFor more details on using [pip], [poetry] or [pipenv] in conjunction with these\nmodes see the [documentation](https://greenbone.github.io/autohooks).\n\n## Maintainer\n\nThis project is maintained by [Greenbone Networks GmbH](https://www.greenbone.net/).\n\n## Contributing\n\nYour contributions are highly appreciated. Please\n[create a pull request](https://github.com/greenbone/autohooks/pulls)\non GitHub. Bigger changes need to be discussed with the development team via the\n[issues section at GitHub](https://github.com/greenbone/autohooks/issues)\nfirst.\n\n## License\n\nCopyright (C) 2019 - 2022 [Greenbone Networks GmbH](https://www.greenbone.net/)\n\nLicensed under the [GNU General Public License v3.0 or later](LICENSE).\n\n[black]: https://black.readthedocs.io/en/stable/\n[pip]: https://pip.pypa.io/en/stable/\n[pipenv]: https://pipenv.readthedocs.io/en/latest/\n[poetry]: https://python-poetry.org/\n[pylint]: https://pylint.readthedocs.io/en/latest/\n',
    'author': 'Greenbone Networks GmbH',
    'author_email': 'info@greenbone.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/greenbone/autohooks/',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
