# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['cognite',
 'cognite.client',
 'cognite.client._api',
 'cognite.client._api.transformations',
 'cognite.client._proto',
 'cognite.client._proto_legacy',
 'cognite.client.data_classes',
 'cognite.client.data_classes.annotation_types',
 'cognite.client.data_classes.transformations',
 'cognite.client.utils']

package_data = \
{'': ['*']}

install_requires = \
['msal>=1,<2',
 'protobuf>=3.16.0',
 'requests>=2,<3',
 'requests_oauthlib>=1,<2',
 'sortedcontainers>=2.2,<3.0']

extras_require = \
{'all': ['sympy',
         'pandas>=1.4,<2.0',
         'geopandas>=0.10.0',
         'shapely>=1.7.0',
         'pip>=20.0.0'],
 'functions': ['pip>=20.0.0'],
 'geo': ['geopandas>=0.10.0', 'shapely>=1.7.0'],
 'numpy': ['numpy>=1.20,<2.0'],
 'pandas': ['pandas>=1.4,<2.0'],
 'sympy': ['sympy']}

setup_kwargs = {
    'name': 'cognite-sdk',
    'version': '5.2.0',
    'description': 'Cognite Python SDK',
    'long_description': '<a href="https://cognite.com/">\n    <img src="https://github.com/cognitedata/cognite-python-docs/blob/master/img/cognite_logo.png" alt="Cognite logo" title="Cognite" align="right" height="80" />\n</a>\n\nCognite Python SDK\n==========================\n[![build](https://github.com/cognitedata/cognite-sdk-python/workflows/release/badge.svg)](https://github.com/cognitedata/cognite-sdk-python/actions?query=workflow:release)\n[![Downloads](https://img.shields.io/pypi/dm/cognite-sdk)](https://pypistats.org/packages/cognite-sdk)\n[![GitHub](https://img.shields.io/github/license/cognitedata/cognite-sdk-python)](https://github.com/cognitedata/cognite-sdk-python/blob/master/LICENSE)\n[![codecov](https://codecov.io/gh/cognitedata/cognite-sdk-python/branch/master/graph/badge.svg)](https://codecov.io/gh/cognitedata/cognite-sdk-python)\n[![Documentation Status](https://readthedocs.com/projects/cognite-sdk-python/badge/?version=latest)](https://cognite-sdk-python.readthedocs-hosted.com/en/latest/)\n[![PyPI version](https://badge.fury.io/py/cognite-sdk.svg)](https://pypi.org/project/cognite-sdk/)\n[![mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n\nThis is the Cognite Python SDK for developers and data scientists working with Cognite Data Fusion (CDF).\nThe package is tightly integrated with pandas, and helps you work easily and efficiently with data in Cognite Data Fusion (CDF).\n\n## Refererence documentation\n* [SDK Documentation](https://cognite-sdk-python.readthedocs-hosted.com/en/latest/)\n* [CDF API Documentation](https://doc.cognitedata.com/)\n* [Cognite Developer Documentation](https://docs.cognite.com/dev/)\n\n## Installation\n\n### Without any optional dependencies\n\nTo install this package without pandas and geopandas support:\n```bash\n$ pip install cognite-sdk\n```\n\n### With optional dependencies\nA number of optional dependencies may be specified in order to support a wider set of features.\nThe available extras (along with the libraries they include) are:\n- numpy `[numpy]`\n- pandas `[pandas]`\n- geo `[geopandas, shapely]`\n- sympy `[sympy]`\n- functions `[pip]`\n- all `[numpy, pandas, geopandas, shapely, sympy, pip]`\n\nTo include optional dependencies, specify them like this with pip:\n\n```bash\n$ pip install cognite-sdk[pandas, geo]\n```\n\nor like this if you are using poetry:\n```bash\n$ poetry add cognite-sdk -E pandas -E geo\n```\n\n### Performance notes\nIf you regularly need to fetch large amounts of datapoints, consider installing with `numpy`\n(or with `pandas`, as it depends on `numpy`) for best performance, then use the `retrieve_arrays` (or `retrieve_dataframe`) endpoint(s). This avoids building large pure Python data structures, and instead reads data directly into memory-efficient `numpy.ndarrays`.\n\n### Windows specific\n\nOn Windows, it is recommended to install `geopandas` and its dependencies using `conda` package manager, see [geopandas installation page](https://geopandas.org/en/stable/getting_started/install.html#installation).\nThe following commands create a new environment, install `geopandas` and `cognite-sdk`.\n\n```bash\nconda create -n geo_env\nconda activate geo_env\nconda install --channel conda-forge geopandas\npip install cognite-sdk\n```\n\n## Changelog\nWondering about upcoming or previous changes to the SDK? Take a look at the [CHANGELOG](https://github.com/cognitedata/cognite-sdk-python/blob/master/CHANGELOG.md).\n\n## Migration Guide\nTo help you upgrade your code(base) quickly and safely to a newer major version of the SDK, check out our migration guide. It is a more focused guide based on the detailed change log. [MIGRATION GUIDE](https://github.com/cognitedata/cognite-sdk-python/blob/master/MIGRATION_GUIDE.md).\n\n## Contributing\nWant to contribute? Check out [CONTRIBUTING](https://github.com/cognitedata/cognite-sdk-python/blob/master/CONTRIBUTING.md).\n',
    'author': 'Erlend Vollset',
    'author_email': 'erlend.vollset@cognite.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
