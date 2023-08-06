# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poem_plugins',
 'poem_plugins.config',
 'poem_plugins.dispatchers',
 'poem_plugins.general',
 'poem_plugins.general.version',
 'poem_plugins.general.version.drivers',
 'poem_plugins.plugins']

package_data = \
{'': ['*']}

install_requires = \
['poetry>=1.2,<2.0']

entry_points = \
{'poetry.application.plugin': ['poem-version-plugin = '
                               'poem_plugins.plugins:VersionPlugin']}

setup_kwargs = {
    'name': 'poem-plugins',
    'version': '0.15.17',
    'description': 'Some set of poetry plugins',
    'long_description': '# Poem Plugins\n\n[![Pypi](https://img.shields.io/pypi/v/poem-plugins?color=%2334D058&label=pypi%20package)](https://pypi.org/project/poem-plugins)\n[![Coverage Status](https://coveralls.io/repos/github/Alviner/poem-plugins/badge.svg?branch=main)](https://coveralls.io/github/Alviner/poem-plugins?branch=main)\n\nA set of plugins for [**Poetry**](https://python-poetry.org/).\n\n## How to use\nMake sure you have Poetry version `1.2.0` or above. Read below for instructions to install it if you haven\'t.\n\n### Install Poem Plugins\n\nInstall this plugin to your Poetry:\n\n```console\n$ poetry self add poem-plugins\n```\n\n### Version Plugin\n\nThe poetry plugin for project versioning allows users to specify\nthe version of their project via the provider other than the default `pyproject.toml` file.\nThis can be useful for users who prefer to set the project version based on a git tag, for example.\n\nPlugin can be configured via a section in the `pyproject.toml` file.\nTo use the plugin, you will need to add a section to your `pyproject.toml`\nfile that specifies the provider.\n\nHere\'s an example of how you might configure the plugin in your `pyproject.toml` file:\n```toml\n[tool.poem-plugins.version]\nprovider = "git"\n```\nLikewise, you can specify a number of optional arguments to control the plugin\nbehavior. Here are some of the arguments that you can use:\n| Name  | description |  Default |\n|-------|-------------|---------|\n| `update_pyproject`   | plugin will not only use version from provider for building, but save it in `pyproject.toml` | `false` |\n| `write_version_file` | plugin will create a file `version.py` inside a module, with version information             | `false` |\n\n\nYou can specify provider-specific settings in your configuration.\nTo specify provider-specific settings, you can use the `tool.poem-plugins.version.{provider}` section.\nHere are some of the arguments that you can use for `git` provider:\n| Name  | description | Default |\n|-------|-------------|---------|\n| `version_prefix`    | filter tags only starts with this prefix  | `v` |\n| `format`            | plugin will use commit hash (long) or not (short) to build a project version | `short` |\n\nExample:\n\n```toml\n[tool.poem-plugins.version.git]\nversion_prefix = "v"\nformat = "short"\n```\n\nTo build your project, run the `poetry build` command.\nThe plugin will build the version via provider and use it to set the version for the project.\n```console\n$ git tag -a v0.1 -m \'tag description\'\n$ poetry build\npoem-plugins: Setting version to: 0.1.0\nBuilding awesome_package (0.1.0)\n  - Building sdist\n  - Built awesome_package-0.1.0.tar.gz\n  - Building wheel\n  - Built awesome_package-0.1.0-py3-none-any.whl```\n```\n\n## How to develop\nBefore getting started with development, you\'ll need to have poetry installed.\n\n\nOnce you have poetry installed, you can create a virtual environment for the project by running:\n```(bash)\npoetry install\n```\nThis will also install all the dependencies required for the project.\n\n### Pre-commit hooks\nThis project uses pre-commit to automatically run\nsimple formatter `gray` before committing changes.\nTo set up the pre-commit hooks, run the following\ncommand in the project root:\n```(bash)\npoetry run pre-commit install\n```\n\n### Type checking\nThis project uses `mypy` for type checking.\nYou can run the type checker\nwith the following command:\n```(bash)\npoetry run mypy poem_plugins\n```\n\n### Linting\nThis project uses `pylama` for linting.\nYou can run the linter\nwith the following command:\n```(bash)\npoetry run pylama poem_plugins\n```\n\n### Tests\nWe use `pytest` for running tests.\nYou can run the tests\nwith the following command:\n```(bash)\npoetry run pytest\n```\n\nPlease make sure that all tests pass and linter and type checker does not\nreport any issues before submitting a pull request.\n',
    'author': 'Ivan Sitkin',
    'author_email': 'alvinera@yandex.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://pypi.org/project/poem-plugins',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
