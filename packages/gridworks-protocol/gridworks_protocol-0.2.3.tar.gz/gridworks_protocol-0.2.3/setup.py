# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['gwproto',
 'gwproto.enums',
 'gwproto.enums.telemetry_name',
 'gwproto.gs',
 'gwproto.gt',
 'gwproto.gt.gt_dispatch_boolean',
 'gwproto.gt.gt_dispatch_boolean_local',
 'gwproto.gt.gt_driver_booleanactuator_cmd',
 'gwproto.gt.gt_sh_booleanactuator_cmd_status',
 'gwproto.gt.gt_sh_cli_atn_cmd',
 'gwproto.gt.gt_sh_multipurpose_telemetry_status',
 'gwproto.gt.gt_sh_simple_telemetry_status',
 'gwproto.gt.gt_sh_status',
 'gwproto.gt.gt_sh_telemetry_from_multipurpose_sensor',
 'gwproto.gt.gt_telemetry',
 'gwproto.gt.snapshot_spaceheat',
 'gwproto.gt.telemetry_snapshot_spaceheat',
 'gwproto.messages']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.1', 'pendulum>=2.1.2,<3.0.0', 'pydantic>=1.10.2,<2.0.0']

entry_points = \
{'console_scripts': ['gridworks-protocol = gwproto.__main__:main']}

setup_kwargs = {
    'name': 'gridworks-protocol',
    'version': '0.2.3',
    'description': 'Gridworks Protocol',
    'long_description': "# Gridworks Protocol\n\n[![PyPI](https://img.shields.io/pypi/v/gridworks-protocol.svg)][pypi_]\n[![Status](https://img.shields.io/pypi/status/gridworks-protocol.svg)][status]\n[![Python Version](https://img.shields.io/pypi/pyversions/gridworks-protocol)][python version]\n[![License](https://img.shields.io/pypi/l/gridworks-protocol)][license]\n\n[![Read the documentation at https://gridworks-protocol.readthedocs.io/](https://img.shields.io/readthedocs/gridworks-protocol/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/thegridelectric/gridworks-protocol/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/thegridelectric/gridworks-protocol/branch/main/graph/badge.svg)][codecov]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi_]: https://pypi.org/project/gridworks-protocol/\n[status]: https://pypi.org/project/gridworks-protocol/\n[python version]: https://pypi.org/project/gridworks-protocol\n[read the docs]: https://gridworks-protocol.readthedocs.io/\n[tests]: https://github.com/thegridelectric/gridworks-protocol/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/thegridelectric/gridworks-protocol\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\n## Features\n\n- TODO\n\n## Requirements\n\n- TODO\n\n## Installation\n\nYou can install _Gridworks Protocol_ via [pip] from [PyPI]:\n\n```console\n$ pip install gridworks-protocol\n```\n\n## Usage\n\nPlease see the [Command-line Reference] for details.\n\n## Contributing\n\nContributions are very welcome.\nTo learn more, see the [Contributor Guide].\n\n## License\n\nDistributed under the terms of the [MIT license][license],\n_Gridworks Protocol_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n## Credits\n\nThis project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/thegridelectric/gridworks-protocol/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/thegridelectric/gridworks-protocol/blob/main/LICENSE\n[contributor guide]: https://github.com/thegridelectric/gridworks-protocol/blob/main/CONTRIBUTING.md\n[command-line reference]: https://gridworks-protocol.readthedocs.io/en/latest/usage.html\n",
    'author': 'Jessica Millar',
    'author_email': 'jmillar@gridworks-consulting.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/thegridelectric/gridworks-protocol',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
