# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lintrunner_adapters',
 'lintrunner_adapters._common',
 'lintrunner_adapters.adapters',
 'lintrunner_adapters.tools']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0']

entry_points = \
{'console_scripts': ['lintrunner_adapters = lintrunner_adapters.__main__:cli']}

setup_kwargs = {
    'name': 'lintrunner-adapters',
    'version': '0.4.0',
    'description': 'Adapters and tools for lintrunner',
    'long_description': '# lintrunner-adapters\n\n[![CI](https://github.com/justinchuby/lintrunner-adapters/actions/workflows/ci.yml/badge.svg)](https://github.com/justinchuby/lintrunner-adapters/actions/workflows/ci.yml)\n[![PyPI version](https://badge.fury.io/py/lintrunner-adapters.svg)](https://badge.fury.io/py/lintrunner-adapters)\n\nAdapters for [lintrunner](https://github.com/suo/lintrunner)\n\n## Install\n\n```sh\npip install lintrunner-adapters\n```\n\n## Usage\n\n```text\nUsage: python -m lintrunner_adapters [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  --help  Show this message and exit.\n\nCommands:\n  run       Run an adapter.\n  to-sarif  Convert the output of lintrunner json (INPUT) to SARIF (OUTPUT).\n```\n\nUse `lintrunner_adapters run` to see a list of adapters available.\n\n## How to\n\n### Write lint config in `.lintrunner.toml`\n\nhttps://docs.rs/lintrunner/latest/lintrunner/lint_config/struct.LintConfig.html\n\n### Create a new adapter\n\nUse [`lintrunner_adapters/adapters/pylint_linter.py`](https://github.com/justinchuby/lintrunner-adapters/blob/main/lintrunner_adapters/adapters/pylint_linter.py) as an example.\n',
    'author': 'Justin Chu',
    'author_email': 'justinchu@microsoft.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/justinchuby/lintrunner-adapters',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
