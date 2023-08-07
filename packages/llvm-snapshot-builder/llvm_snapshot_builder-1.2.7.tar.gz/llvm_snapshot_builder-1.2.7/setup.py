# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['llvm_snapshot_builder',
 'llvm_snapshot_builder.actions',
 'llvm_snapshot_builder.mixins']

package_data = \
{'': ['*']}

install_requires = \
['copr>=1.124,<2.0']

setup_kwargs = {
    'name': 'llvm-snapshot-builder',
    'version': '1.2.7',
    'description': 'Builds LLVM snapshots on Copr',
    'long_description': '# llvm_snapshot_builder\n\nBuilds LLVM snapshots on Copr\n\n## Status\n\n[![Documentation Status](https://readthedocs.org/projects/llvm_snapshot_builder/badge/?version=latest)](https://llvm_snapshot_builder.readthedocs.io/en/latest/?badge=latest)\n[![CodeQL](https://github.com/kwk/llvm_snapshot_builder/actions/workflows/codeql.yml/badge.svg)](https://github.com/kwk/llvm_snapshot_builder/actions/workflows/codeql.yml)\n[![ci-cd](https://github.com/kwk/llvm_snapshot_builder/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/kwk/llvm_snapshot_builder/actions/workflows/ci-cd.yml)\n[![codecov](https://codecov.io/gh/kwk/llvm_snapshot_builder/branch/main/graph/badge.svg?token=ASSPTOL3JU)](https://codecov.io/gh/kwk/llvm_snapshot_builder)\n[![release](https://img.shields.io/github/release/kwk/llvm_snapshot_builder.svg)](https://github.com/kwk/llvm_snapshot_builder/releases)\n\n## Installation\n\n```bash\n$ pip install llvm_snapshot_builder\n```\n\n## Usage\n\nFor a more in-depth example, take a look at [the example in the documentation](https://llvm_snapshot_builder.readthedocs.io/en/latest/example.html).\n\nAfter installing you can explore the CLI program with:\n\n```bash\npython -m llvm_snapshot_builder.cli --help\n```\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n### Commit message conventions and semantic versioniong (semver)\n\nWe use semantic versioning and [these commit message conventions](https://www.conventionalcommits.org/en/v1.0.0/)\ncan be used to automatically bump the version number and generate the changelog.\n\n## License\n\n`llvm_snapshot_builder` was created by Konrad Kleine <kkleine@redhat.com>. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`llvm_snapshot_builder` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'Konrad Kleine',
    'author_email': 'kkleine@redhat.com',
    'maintainer': 'Konrad Kleine',
    'maintainer_email': 'kkleine@redhat.com',
    'url': 'https://pypi.org/project/llvm_snapshot_builder/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4',
}


setup(**setup_kwargs)
