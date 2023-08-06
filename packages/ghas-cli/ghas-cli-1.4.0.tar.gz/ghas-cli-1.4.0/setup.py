# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ghas_cli', 'ghas_cli.utils']

package_data = \
{'': ['*']}

install_requires = \
['click>=8',
 'colorama',
 'configparser',
 'python-magic',
 'requests',
 'urllib3>=1.26.12,<2.0.0']

entry_points = \
{'console_scripts': ['ghas-cli = src.cli:main']}

setup_kwargs = {
    'name': 'ghas-cli',
    'version': '1.4.0',
    'description': 'Command line interface to interact with GitHub Advanced Security.',
    'long_description': '# Security-ghas-cli\n\n[![CodeQL](https://github.com/Malwarebytes/Security-ghas-cli/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Malwarebytes/Security-ghas-cli/actions/workflows/codeql-analysis.yml)\n\nCLI utility to interact with [GitHub Advanced Security](https://docs.github.com/en/enterprise-cloud@latest/get-started/learning-about-github/about-github-advanced-security) (_"GHAS"_).\n\nIt allows to deploy GHAS features individually or at scale, while taking into account each repository configuration.\n\nMore specifically, it automates the following:\n\n* Ensure GitHub Actions are properly enabled for the repository (required for CodeQL),\n* Enable [Secret Scanner](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/about-secret-scanning), and create an informative issue\n* Enable [Push Protection](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/protecting-pushes-with-secret-scanning), and create an informative issue\n* Enable [Dependabot](https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/working-with-dependabot) and create an informative issue\n* Enable the [Dependency Reviewer](https://docs.github.com/en/enterprise-cloud@latest/code-security/supply-chain-security/about-dependency-review) and create an informative issue\n* Open a PR to deploy [Code Scanning](https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/about-code-scanning) with a custom configuration tuned for each repository\'s languages and _non-main default branch_ (e.g `main` or `master` are not hardcoded, it determines the proper default branch automatically),\n* Cleanup legacy Mend issues on each repository\n\n\nEach of these actions can also open an issue explaining each feature, how to use them, and what to eventually do before they are fully enabled.\nSee `./templates` to get an overview of these issues!\n\nTo follow your deployment, `ghas-cli` outputs results in a csv file indicating the deployment status of each feature for each repository.\n\nYou can work on a single repository or on thousands of them. In that case, `ghas-cli` does its best to overcome [GitHub\'s rate limits](https://docs.github.com/en/enterprise-cloud@latest/rest/rate-limit)...\n\n\n## Installation\n\nBuilds are available in the [`Releases`](https://github.com/Malwarebytes/Security-ghas-cli/releases) tab.\n\n* Pypi:\n\n```bash\npip install ghas-cli\n```\n\n* Manually:\n\n```bash\npython -m pip install /full/path/to/ghas-cli-xxx.whl\n\n# e.g: python3 -m pip install Downloads/ghas-cli-0.5.0-none-any.whl\n```\n\n## Usage\n\n`ghas-cli -h` or see the [wiki](https://github.com/Malwarebytes/Security-ghas-cli/wiki).\n\n\n## Development\n\n### Build\n\n[Install Poetry](https://python-poetry.org/docs/#installation) first, then:\n\n```bash\nmake dev\n```\n\n### Bump the version number\n\n* Bump the version number: `poetry version x.x.x`\n* Update the `__version__` field in `src/cli.py` accordingly.\n\n### Publish a new version\n\n**Requires `syft` to be installed to generate the sbom.**\n\n1. Bump the version number as described above\n2. `make deps` to update the dependencies\n3. `make release` to build the packages\n4. `git commit -a -S Bump to version 1.1.2` and `git tag -s v1.1.2 -m "1.1.2"`\n5. Upload `dist/*`, `checksums.sha512` and `checksums.sha512.asc` to a new release in GitHub.\n6. Upload to [PyPi](https://pypi.org/project/ghas-cli/): `poetry publish`.\n\n\n## Why not use `ghas-enablement`?\n\nGitHub suggests using [ghas-enablement](https://github.com/NickLiffen/ghas-enablement) to deploy GHAS at scale. Unfortunately, it has many limitations that make it a non viable tool as you understood if you read the beginning of this README, including:\n\n* Only support for one default branch name: If you repositories are mixing `master`, `main`, `dev`, `test`... as the repository default branch, you will end up creating the CodeQL config to another branch than the default\'s.\n    - `ghas-cli` uses the correct default branch for each repo.\n* Non per-language CodeQL workflow configuration: You can only automate the PR creation for a single CodeQL workflow config file. Your repositories are likely a mix of many languages combinations, so pushing a single workflow configuration accross an organization is not efficient.\n    - `ghas-cli` adjusts the CodeQL configuration to each repository languages.\n* Doesn\'t check if Actions are properly enabled on your organization repositories: Running `ghas-enablement` when Actions are disabled will fail.\n    - `ghas-cli` makes sure Actions are enabled before doing anything else. If they\'re not, it enables them.\n* More broadly, `ghas-cli` creates more educative issues on each repositories. It also provides more flexibility with an extensive CLI to pipe in/out data.\n\n\n\n# Miscellaneous\n\nThis repository is provided as-is and isn\'t bound to Malwarebytes\' SLA.\n',
    'author': 'jboursier',
    'author_email': 'jboursier@malwarebytes.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Malwarebytes/ghas-cli',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
