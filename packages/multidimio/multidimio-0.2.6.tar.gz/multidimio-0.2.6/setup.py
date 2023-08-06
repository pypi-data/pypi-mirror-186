# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['mdio',
 'mdio.api',
 'mdio.commands',
 'mdio.converters',
 'mdio.core',
 'mdio.segy']

package_data = \
{'': ['*']}

install_requires = \
['click-params>=0.3.0,<0.4.0',
 'click>=8.1.3,<9.0.0',
 'dask>=2022.11.0',
 'numba>=0.55.2,<1.0.0',
 'psutil>=5.9.1,<6.0.0',
 'segyio>=1.9.3,<2.0.0',
 'tqdm>=4.64.0,<5.0.0',
 'zarr>=2.12.0,<3.0.0']

extras_require = \
{'cloud': ['s3fs>=2022.7.0,<2023.0.0',
           'gcsfs>=2022.7.0,<2023.0.0',
           'adlfs>=2022.7.0,<2023.0.0'],
 'distributed': ['distributed>=2022.11.0', 'bokeh>=2.4.3,<3.0.0'],
 'lossy': ['zfpy>=1.0.0,<2.0.0']}

entry_points = \
{'console_scripts': ['mdio = mdio.__main__:main']}

setup_kwargs = {
    'name': 'multidimio',
    'version': '0.2.6',
    'description': 'Cloud-native, scalable, and user-friendly multi dimensional energy data!',
    'long_description': '<div>\n  <img\n      class="logo"\n      src="https://raw.githubusercontent.com/TGSAI/mdio.github.io/gh-pages/assets/images/mdio.png"\n      alt="MDIO"\n      width=200\n      height=auto\n      style="margin-top:10px;margin-bottom:10px"\n  />\n</div>\n\n[![PyPI](https://img.shields.io/pypi/v/multidimio.svg)][install_pip]\n[![Conda](https://img.shields.io/conda/vn/conda-forge/multidimio)][install_conda]\n[![Python Version](https://img.shields.io/pypi/pyversions/multidimio)][python version]\n[![Status](https://img.shields.io/pypi/status/multidimio.svg)][status]\n[![License](https://img.shields.io/pypi/l/multidimio)][license]\n\n[![Tests](https://github.com/TGSAI/mdio-python/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/TGSAI/mdio-python/branch/main/graph/badge.svg)][codecov]\n[![Read the documentation at https://mdio-python.readthedocs.io/](https://img.shields.io/readthedocs/mdio-python/latest.svg?label=Read%20the%20Docs)][read the docs]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[![PyPI Downloads](https://static.pepy.tech/personalized-badge/multidimio?period=total&units=international_system&left_color=grey&right_color=blue&left_text=PyPI%20downloads)][pypi_]\n[![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/multidimio?label=Conda%20downloads&style=flat)][conda-forge_]\n\n[pypi_]: https://pypi.org/project/multidimio/\n[conda-forge_]: https://anaconda.org/conda-forge/multidimio\n[status]: https://pypi.org/project/multidimio/\n[python version]: https://pypi.org/project/multidimio\n[read the docs]: https://mdio-python.readthedocs.io/\n[tests]: https://github.com/TGSAI/mdio-python/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/TGSAI/mdio-python\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n[install_pip]: https://mdio-python.readthedocs.io/en/latest/installation.html#using-pip-and-virtualenv\n[install_conda]: https://mdio-python.readthedocs.io/en/latest/installation.html#using-conda\n\n**_"MDIO"_** is a library to work with large multidimensional energy datasets.\nThe primary motivation behind **MDIO** is to represent multidimensional\ntime series data in a format that makes it easier to use in resource assessment,\nmachine learning, and data processing workflows.\n\nSee the [documentation][read the docs] for more information.\n\n# Features\n\n**Shared Features**\n\n- Abstractions for common energy data types (see below).\n- Cloud native chunked storage based on [Zarr][zarr] and [fsspec][fsspec].\n- Lossy and lossless data compression using [Blosc][blosc] and [ZFP][zfp].\n- Distributed reads and writes using [Dask][dask].\n- Powerful command-line-interface (CLI) based on [Click][click]\n\n**Domain Specific Features**\n\n- Oil & Gas Data\n  - Import and export 2D - 5D seismic data types stored in SEG-Y.\n  - Import seismic interpretation, horizon, data. **FUTURE**\n  - Optimized chunking logic for various seismic types. **FUTURE**\n- Wind Resource Assessment\n  - Numerical weather prediction models with arbitrary metadata. **FUTURE**\n  - Optimized chunking logic for time-series analysis and mapping. **FUTURE**\n  - [Xarray][xarray] interface. **FUTURE**\n\nThe features marked as **FUTURE** will be open-sourced at a later date.\n\n# Installing MDIO\n\nSimplest way to install _MDIO_ via [pip] from [PyPI]:\n\n```shell\n$ pip install multidimio\n```\n\nor install _MDIO_ via [conda] from [conda-forge]:\n\n```shell\n$ conda install -c conda-forge multidimio\n```\n\n> Extras must be installed separately on `Conda` environments.\n\nFor details, please see the [installation instructions][install]\nin the documentation.\n\n# Using MDIO\n\nPlease see the [Command-line Reference][usage] for details.\n\nFor Python API please see the [API Reference][reference] for details.\n\n# Requirements\n\n## Minimal\n\nChunked storage and parallelization: `zarr`, `dask`, `numba`, and `psutil`.\\\nSEG-Y Parsing: `segyio`\\\nCLI and Progress Bars: `click`, `click-params`, and `tqdm`.\n\n## Optional\n\nDistributed computing `[distributed]`: `distributed` and `bokeh`.\\\nCloud Object Store I/O `[cloud]`: `s3fs`, `gcsfs`, and `adlfs`.\\\nLossy Compression `[lossy]`: `zfpy`\n\n# Contributing to MDIO\n\nContributions are very welcome.\nTo learn more, see the [Contributor Guide].\n\n# Licensing\n\nDistributed under the terms of the [Apache 2.0 license][license],\n_MDIO_ is free and open source software.\n\n# Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n# Credits\n\nThis project was established at [TGS](https://www.tgs.com/). Original authors\nand current maintainers are [Altay Sansal](https://github.com/tasansal) and\n[Sri Kainkaryam](https://github.com/srib); with the support of many more great\ncolleagues.\n\nThis project template is based on [@cjolowicz]\'s [Hypermodern Python Cookiecutter]\ntemplate.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[conda-forge]: https://conda-forge.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/TGSAI/mdio-python/issues\n[pip]: https://pip.pypa.io/\n[conda]: https://docs.conda.io/\n[dask]: https://www.dask.org/\n[zarr]: https://zarr.dev/\n[fsspec]: https://filesystem-spec.readthedocs.io/en/latest/\n[s3fs]: https://s3fs.readthedocs.io/\n[gcsfs]: https://gcsfs.readthedocs.io/\n[adlfs]: https://github.com/fsspec/adlfs\n[blosc]: https://www.blosc.org/\n[zfp]: https://computing.llnl.gov/projects/zfp\n[xarray]: https://xarray.dev/\n[click]: https://palletsprojects.com/p/click/\n\n<!-- github-only -->\n\n[license]: https://github.com/TGSAI/mdio-python/blob/main/LICENSE\n[contributor guide]: https://github.com/TGSAI/mdio-python/blob/main/CONTRIBUTING.md\n[usage]: https://mdio-python.readthedocs.io/en/latest/usage.html\n[reference]: https://mdio-python.readthedocs.io/en/latest/reference.html\n[install]: https://mdio-python.readthedocs.io/en/latest/installation.html\n',
    'author': 'TGS',
    'author_email': 'sys-opensource@tgs.com',
    'maintainer': 'Altay Sansal',
    'maintainer_email': 'altay.sansal@tgs.com',
    'url': 'https://mdio.dev',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
