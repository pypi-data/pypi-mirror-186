# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['casparser_isin']

package_data = \
{'': ['*']}

install_requires = \
['packaging>=20.9', 'rapidfuzz>=2.0.0,<3.0.0']

entry_points = \
{'console_scripts': ['casparser-isin = casparser_isin.cli:main']}

setup_kwargs = {
    'name': 'casparser-isin',
    'version': '2023.1.16',
    'description': 'ISIN database for casparser',
    'long_description': '# CASParser-ISIN\n\n[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![GitHub](https://img.shields.io/github/license/codereverser/casparser)](https://github.com/codereverser/casparser/blob/main/LICENSE)\n![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/codereverser/casparser-isin/run-pytest.yml?branch=main)\n[![codecov](https://codecov.io/gh/codereverser/casparser-isin/branch/main/graph/badge.svg?token=MQ8ZEVTG1B)](https://codecov.io/gh/codereverser/casparser-isin)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/casparser-isin)\n\nISIN Database for [casparser](https://github.com/codereverser/casparser).\n\n## Installation\n```bash\npip install -U casparser-isin\n``` \n\n## Usage\n\n\n```python\nfrom casparser_isin import MFISINDb\nwith MFISINDb() as db:\n    scheme_data = db.isin_lookup("Axis Long Term Equity Fund - Growth",  # scheme name\n                                 "KFINTECH", # RTA\n                                 "128TSDGG", # Scheme RTA code\n                                 )\nprint(scheme_data)\n```\n```\nSchemeData(name="axis long term equity fund - direct growth", \n           isin="INF846K01EW2", \n           amfi_code="120503", \n           score=100.0)\n```\n\nThe database also contains NAV values on 31-Jan-2018 for all funds, which can be used for \ntaxable LTCG computation for units purchased before the same date.  \n\n```\nfrom casparser_isin import MFISINDb\nwith MFISINDb() as db:\n    nav = db.nav_lookup("INF846K01EW2")\nprint(nav)\n```\n```\nDecimal(\'44.8938\')\n```\n\n\n## Notes\n\n- casparser-isin is shipped with a local database which may get obsolete over time. The local \ndatabase can be updated via the cli tool \n\n```shell\ncasparser-isin --update\n```\n\n- casparser-isin will try to use the file provided by `CASPARSER_ISIN_DB` environment variable; if present, and the file exists\n',
    'author': 'Sandeep Somasekharan',
    'author_email': 'codereverser@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/codereverser/casparser-isin',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
