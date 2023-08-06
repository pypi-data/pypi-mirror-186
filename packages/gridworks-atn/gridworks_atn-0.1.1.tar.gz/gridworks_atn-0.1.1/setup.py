# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['gwatn',
 'gwatn.csv_makers',
 'gwatn.data_classes',
 'gwatn.dev_utils',
 'gwatn.enums',
 'gwatn.types']

package_data = \
{'': ['*'], 'gwatn': ['dispatch_contract_artifacts/*']}

install_requires = \
['boto3>=1.26.3,<2.0.0',
 'gridworks-protocol>=0.1.5,<0.2.0',
 'gridworks>=0.0.15,<0.0.16',
 'numpy>=1.23.4,<2.0.0',
 'paho-mqtt>=1.6.1,<2.0.0',
 'types-requests>=2.28.11.2,<3.0.0.0']

entry_points = \
{'console_scripts': ['gridworks-atn = gwatn.__main__:main']}

setup_kwargs = {
    'name': 'gridworks-atn',
    'version': '0.1.1',
    'description': 'Gridworks Atn Spaceheat',
    'long_description': "# Gridworks Atn\n\n[![PyPI](https://img.shields.io/pypi/v/gridworks-atn.svg)][pypi_]\n[![Status](https://img.shields.io/pypi/status/gridworks-atn.svg)][status]\n[![Python Version](https://img.shields.io/pypi/pyversions/gridworks-atn)][python version]\n[![License](https://img.shields.io/pypi/l/gridworks-atn)][license]\n\n[![Read the documentation at https://gridworks-atn.readthedocs.io/](https://img.shields.io/readthedocs/gridworks/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/thegridelectric/gridworks-atn/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/thegridelectric/gridworks-atn/branch/main/graph/badge.svg)][codecov]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi_]: https://pypi.org/project/gridworks-atn/\n[status]: https://pypi.org/project/gridworks-atn/\n[python version]: https://pypi.org/project/gridworks-atn\n[read the docs]: https://gridworks-atn.readthedocs.io/\n[tests]: https://github.com/thegridelectric/gridworks-atn/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/thegridelectric/gridworks-atn\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\nThis is the [GridWorks](https://gridworks.readthedocs.io/) Python SDK for building Atomic Transactive Nodes, or\n[AtomicTNodes](https://gridworks.readthedocs.io/en/latest/atomic-t-node.html>).\n\nAtomicTNodes are the most fun and interesting GridWorks actors to design and build. They are what make electrical devices\n_transactive_. More specifically, each AtomicTNode is dedicated to the job of operating its very own\n[Transactive Device](https://gridworks.readthedocs.io/en/latest/transactive-device.html), and simultaneously bidding on its behalf into electricity markets.\n\nTo learn about using this SDK, visit the [Gridworks Atn docs](https://gridworks-atn.readthedocs.io/en/latest/). To explore the rest of GridWorks, visit the [GridWorks docs](https://gridworks.readthedocs.io/en/latest/).\n\n## License\n\nDistributed under the terms of the [MIT license][license],\n**Gridworks Atn** is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n## Credits\n\nThis project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/thegridelectric/gridworks-atn/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/thegridelectric/gridworks-atn/blob/main/LICENSE\n[contributor guide]: https://github.com/thegridelectric/gridworks-atn/blob/main/CONTRIBUTING.md\n[command-line reference]: https://gridworks-atn.readthedocs.io/en/latest/usage.html\n",
    'author': 'Jessica Millar',
    'author_email': 'jmillar@gridworks-consulting.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/thegridelectric/gridworks-atn',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
