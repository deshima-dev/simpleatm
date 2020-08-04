# simpleatm
Lightweight Python package for calculating the atmospheric transmission

## Overview

[simpleatm] is a Python package which calculates (sub)millimeter atmospheric transmission as a function of precipitable water vapor (PWV) and frequency.
The package includes pre-calculated transmission datasets at various observation sites by the [ATM model] (Pardo et al. 2001).
Moreover, since a dataset is loaded as the [xarray]'s DataArray format, interpolation, plotting, and saving features are provided by default.
Therefore, [simpleatm] would be useful in fast and approximate sensitivity calculation of a telescope instrument.

## Requirements

- **Python:** 3.6, 3.7, or 3.8 (tested by the authors)
- **Dependencies:** See [pyproject.toml](https://github.com/deshima-dev/simpleatm/blob/master/pyproject.toml)

## Installation

```shell
$ pip install simpleatm
```

## Usage

To be updated after the release of [v0.1.0](https://github.com/deshima-dev/simpleatm/milestone/2).

## For developers

```shell
$ git clone https://github.com/deshima-dev/simpleatm.git
$ cd simpleatm
$ etc/configure
```

## References

- [ATM model]: pre-calculated table was obtained here
- [xarray]: N-D labeled arrays and datasets in Python

[simpleatm]: https://pypi.org/project/simpleatm/
[ALMA]: https://almascience.nao.ac.jp/
[ATM model]: https://almascience.nao.ac.jp/about-alma/atmosphere-model/
[Poetry]: https://python-poetry.org/
[xarray]: https://xarray.pydata.org/en/stable/
