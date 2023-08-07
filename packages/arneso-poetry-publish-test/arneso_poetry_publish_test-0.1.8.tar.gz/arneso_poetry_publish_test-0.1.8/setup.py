# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['arneso_poetry_publish_test']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3']

entry_points = \
{'console_scripts': ['arneso-poetry-publish-test = '
                     'arneso_poetry_publish_test.__main__:main']}

setup_kwargs = {
    'name': 'arneso-poetry-publish-test',
    'version': '0.1.8',
    'description': 'Arneso Poetry Publish Test',
    'long_description': "# Arneso Poetry Publish Test\n\n[![PyPI](https://img.shields.io/pypi/v/arneso-poetry-publish-test.svg)][pypi_]\n[![Status](https://img.shields.io/pypi/status/arneso-poetry-publish-test.svg)][status]\n[![Python Version](https://img.shields.io/pypi/pyversions/arneso-poetry-publish-test)][python version]\n[![License](https://img.shields.io/pypi/l/arneso-poetry-publish-test)][license]\n\n[![Read the documentation at https://arneso-poetry-publish-test.readthedocs.io/](https://img.shields.io/readthedocs/arneso-poetry-publish-test/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/arneso-ssb/arneso-poetry-publish-test/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/arneso-ssb/arneso-poetry-publish-test/branch/main/graph/badge.svg)][codecov]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi_]: https://pypi.org/project/arneso-poetry-publish-test/\n[status]: https://pypi.org/project/arneso-poetry-publish-test/\n[python version]: https://pypi.org/project/arneso-poetry-publish-test\n[read the docs]: https://arneso-poetry-publish-test.readthedocs.io/\n[tests]: https://github.com/arneso-ssb/arneso-poetry-publish-test/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/arneso-ssb/arneso-poetry-publish-test\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\n## Features\n\n- TODO\n\n## Requirements\n\n- TODO\n\n## Installation\n\nYou can install _Arneso Poetry Publish Test_ via [pip] from [PyPI]:\n\n```console\n$ pip install arneso-poetry-publish-test\n```\n\n## Usage\n\nPlease see the [Command-line Reference] for details.\n\n## Contributing\n\nContributions are very welcome.\nTo learn more, see the [Contributor Guide].\n\n## License\n\nDistributed under the terms of the [MIT license][license],\n_Arneso Poetry Publish Test_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n## Credits\n\nThis project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/arneso-ssb/arneso-poetry-publish-test/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/arneso-ssb/arneso-poetry-publish-test/blob/main/LICENSE\n[contributor guide]: https://github.com/arneso-ssb/arneso-poetry-publish-test/blob/main/CONTRIBUTING.md\n[command-line reference]: https://arneso-poetry-publish-test.readthedocs.io/en/latest/usage.html\n",
    'author': 'Arne Sørli',
    'author_email': '81353974+arneso-ssb@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/arneso-ssb/arneso-poetry-publish-test',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
