# zema_emc_annotated

[![pipeline status](https://gitlab1.ptb.de/m4d/zema_emc_annotated/badges/main/pipeline.svg)](https://gitlab1.ptb.de/m4d/zema_emc_annotated/-/commits/main)
[![coverage report](https://gitlab1.ptb.de/m4d/zema_emc_annotated/badges/main/coverage.svg)](https://gitlab1.ptb.de/m4d/zema_emc_annotated/-/commits/main)
[![Latest Release](https://gitlab1.ptb.de/m4d/zema_emc_annotated/-/badges/release.svg)](https://gitlab1.ptb.de/m4d/zema_emc_annotated/-/releases)

This software provides a convenient API to access the annotated ZeMA dataset about 
remaining useful life of an electro-mechanical cylinder on Zenodo (
[![DOI 10.5281/zenodo.5185953
](https://zenodo.org/badge/DOI/10.5281/zenodo.5185953.svg)
](https://doi.org/10.5281/zenodo.5185953)) The code was written for _Python 3.10_.

## Getting started

The [INSTALL guide](INSTALL.md) assists in installing the required packages.

## Documentation

To locally build the HTML or pdf documentation first the required dependencies need 
to be installed into your virtual environment (check the [INSTALL guide](INSTALL.md) 
first and upon completion execute the following):

```shell
(venv) $ python -m poetry install --with docs
(venv) $ sphinx-build docs/ docs/_build
sphinx-build docs/ docs/_build
Running Sphinx v5.3.0
loading pickled environment... done
[...]
The HTML pages are in docs/_build.
```

After that the documentation can be viewed by opening the file
_docs/\_build/index.html_ in any browser.

In the near future the documentation will be available on ReadTheDocs.
