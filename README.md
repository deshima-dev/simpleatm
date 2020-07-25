# alma-atm
Lightweight Python package for calculating the atmospheric transmission at the ALMA site

## Overview

[alma-atm] is a Python package which calculates the (sub)millimeter atmospheric transmission at the [ALMA] site as a function of precipitable water vapor (PWV) and frequency.
The package includes a pre-calculated transmission table by the [ATM model] (Pardo et al. 2001).
Moreover, since the table is loaded as the [xarray]'s DataArray format, interpolation, plotting, and saving features are provided by default.
Therefore, [alma-atm] would be useful in fast and approximate sensitivity calculation of a telescope instrument.

## Requirements

- **Python:** 3.6, 3.7, or 3.8 (tested by the authors)
- **Dependencies:** See [pyproject.toml](https://github.com/deshima-dev/alma-atm/blob/master/pyproject.toml)

## Installation

```shell
$ pip install alma-atm
```

## Usage

To be updated after the release of v0.1.0.

## For developers

```shell
$ git clone https://github.com/deshima-dev/alma-atm.git
$ cd alma-atm
$ etc/configure
```

## References

- [ATM model] (pre-calculated table was obtained here)
- [xarray]: N-D labeled arrays and datasets in Python

[alma-atm]: https://pypi.org/project/alma-atm/
[ALMA]: https://almascience.nao.ac.jp/
[ATM model]: https://almascience.nao.ac.jp/about-alma/atmosphere-model
[Poetry]: https://python-poetry.org/
[xarray]: https://xarray.pydata.org/en/stable/
