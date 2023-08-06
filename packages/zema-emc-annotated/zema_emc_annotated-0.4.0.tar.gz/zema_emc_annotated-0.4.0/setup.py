# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['zema_emc_annotated']

package_data = \
{'': ['*'], 'zema_emc_annotated': ['examples/*']}

install_requires = \
['h5py>=3.7.0,<4.0.0',
 'numpy>=1.24.1,<2.0.0',
 'pooch>=1.6.0,<2.0.0',
 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'zema-emc-annotated',
    'version': '0.4.0',
    'description': 'API to the annotated ZeMA dataset about an electro-mechanical cylinder',
    'long_description': '# zema_emc_annotated\n\n[![pipeline status](https://gitlab1.ptb.de/m4d/zema_emc_annotated/badges/main/pipeline.svg)](https://gitlab1.ptb.de/m4d/zema_emc_annotated/-/commits/main)\n[![coverage report](https://gitlab1.ptb.de/m4d/zema_emc_annotated/badges/main/coverage.svg)](https://gitlab1.ptb.de/m4d/zema_emc_annotated/-/commits/main)\n[![Latest Release](https://gitlab1.ptb.de/m4d/zema_emc_annotated/-/badges/release.svg)](https://gitlab1.ptb.de/m4d/zema_emc_annotated/-/releases)\n\nThis software provides a convenient API to access the annotated ZeMA dataset about \nremaining useful life of an electro-mechanical cylinder on Zenodo (\n[![DOI 10.5281/zenodo.5185953\n](https://zenodo.org/badge/DOI/10.5281/zenodo.5185953.svg)\n](https://doi.org/10.5281/zenodo.5185953)) The code was written for _Python 3.10_.\n\n## Getting started\n\nThe [INSTALL guide](INSTALL.md) assists in installing the required packages.\n\n## Documentation\n\nTo locally build the HTML or pdf documentation first the required dependencies need \nto be installed into your virtual environment (check the [INSTALL guide](INSTALL.md) \nfirst and upon completion execute the following):\n\n```shell\n(venv) $ python -m poetry install --with docs\n(venv) $ sphinx-build docs/ docs/_build\nsphinx-build docs/ docs/_build\nRunning Sphinx v5.3.0\nloading pickled environment... done\n[...]\nThe HTML pages are in docs/_build.\n```\n\nAfter that the documentation can be viewed by opening the file\n_docs/\\_build/index.html_ in any browser.\n\nIn the near future the documentation will be available on ReadTheDocs.\n',
    'author': 'Bjoern Ludwig',
    'author_email': 'bjoern.ludwig@ptb.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
