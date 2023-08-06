# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['gwmm', 'gwmm.data_classes', 'gwmm.enums', 'gwmm.types']

package_data = \
{'': ['*']}

install_requires = \
['gridworks>=0.1.0,<0.2.0']

entry_points = \
{'console_scripts': ['gridworks-marketmaker = gwmm.__main__:main']}

setup_kwargs = {
    'name': 'gridworks-marketmaker',
    'version': '0.0.3',
    'description': 'Gridworks Marketmaker',
    'long_description': "# Gridworks Marketmaker\n\nThis is the Python SDK for building \n[MarketMakers](https://gridworks.readthedocs.io/en/latest/market-maker.html) for GridWorks.   GridWorks uses distributed actors to balance the electric grid, and MarketMakers are the actors brokering this grid balancing via the markets they run for energy and balancing services.\n\nThis SDK is available as the [gridworks-marketmaker](https://pypi.org/project/gridworks-marketmaker/) pypi package. Documentation\nspecific to using this SDK is available [here](https://gridworks-marketmaker.readthedocs.io/). If this is your first time\nwith GridWorks code, please start with the [main GridWorks doc](https://gridworks.readthedocs.io/).\n\n\n\nMarketMakers support grid balancing by running markets. They are geared to serve millions of coordinated and intelligent\n[Transactive Devices](https://gridworks.readthedocs.io/en/latest/transactive-device.html), represented in their\nmarkets by  [AtomicTNodes](https://gridworks.readthedocs.io/en/latest/atomic-t-node.html). The veracity of the\nex-poste energy and power data provided by AtomicTNodes to the MarketMaker is backed up via a series of GridWorks Certificates\nglobally visible on the Algorand blockchain.  These include the foundational\n[TaDeeds](https://gridworks.readthedocs.io/en/latest/ta-deed.html) that establish ownership of the underlying\nTransactive Device, and the [TaTradingrights](https://gridworks.readthedocs.io/en/latest/ta-trading-rights.html) that\ngive the AtomicTNode authority to represent the Transactive Device in its MarketMaker's markets.\n\n\n## Millinocket MarketMaker directions\n\nThese are directions for running this code as the MarketMaker in the [Millinocket tutorial](https://gridworks.readthedocs.io/en/latest/millinocket-tutorial.html).  These directions assume you have **already started docker sandbox and the GridWorks dev rabbit broker**, as described in the [Demo prep](https://gridworks.readthedocs.io/en/latest/millinocket-tutorial.html#demo-prep).\n\n1. Clone this repo\n\n2. Using python 3.10.\\* or greater, create virtual env inside this repo\n\n   ```\n   python -m venv venv\n   source venv/bin/activate\n   pip install -e .\n   ```\n3.Run the FastAPI half of the MarketMaker:\n\n```\nuvicorn gwmm.rest_api:app --host localhost --port 7997 --workers 5\n```\n\n    - http://localhost:7997/ shows market maker information\n    - http://localhost:7997/get-time/ shows the current time of the simulation\n\n4. Run the rabbit half of the MarketMaker:\n\n```\npython demo.py\n```\n\nNOTE: This requires a TimeCoordinator and at least one AtomicTNode in order\nfor time to move forward. \n\n\n## Contributing\n\nContributions are very welcome.\nTo learn more, see the [Contributor Guide].\n\n## License\n\nDistributed under the terms of the [MIT license][license],\n_Gridworks Marketmaker_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n[![PyPI](https://img.shields.io/pypi/v/gridworks-marketmaker.svg)][pypi_]\n[![Status](https://img.shields.io/pypi/status/gridworks-marketmaker.svg)][status]\n[![Python Version](https://img.shields.io/pypi/pyversions/gridworks-marketmaker)][python version]\n[![License](https://img.shields.io/pypi/l/gridworks-marketmaker)][license]\n\n[![Read the documentation at https://gridworks-marketmaker.readthedocs.io/](https://img.shields.io/readthedocs/gridworks-marketmaker/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/thegridelectric/gridworks-marketmaker/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/thegridelectric/gridworks-marketmaker/branch/main/graph/badge.svg)][codecov]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi_]: https://pypi.org/project/gridworks-marketmaker/\n[status]: https://pypi.org/project/gridworks-marketmaker/\n[python version]: https://pypi.org/project/gridworks-marketmaker\n[read the docs]: https://gridworks-marketmaker.readthedocs.io/\n[tests]: https://github.com/thegridelectric/gridworks-marketmaker/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/thegridelectric/gridworks-marketmaker\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\n## Credits\n\nThis project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/thegridelectric/gridworks-marketmaker/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/thegridelectric/gridworks-marketmaker/blob/main/LICENSE\n[contributor guide]: https://github.com/thegridelectric/gridworks-marketmaker/blob/main/CONTRIBUTING.md\n[command-line reference]: https://gridworks-marketmaker.readthedocs.io/en/latest/usage.html\n",
    'author': 'Jessica Millar',
    'author_email': 'jmillar@gridworks-consulting.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/thegridelectric/gridworks-marketmaker',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
