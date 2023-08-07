# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['nem_bidding_dashboard']

package_data = \
{'': ['*'], 'nem_bidding_dashboard': ['assets/*']}

install_requires = \
['dash-bootstrap-components>=1.2.1,<2.0.0',
 'dash-loading-spinners>=1.0.0,<2.0.0',
 'dash>=2.6.1,<3.0.0',
 'gunicorn>=20.1.0,<21.0.0',
 'nemosis>=3.1.0,<4.0.0',
 'numpy>=1.23.3,<2.0.0',
 'openpyxl>=3.0.10,<4.0.0',
 'pandas>=1.2,<2.0',
 'plotly>=5.10.0,<6.0.0',
 'psycopg[binary]>=3.1.4,<4.0.0',
 'pytest-mock>=3.10.0,<4.0.0',
 'supabase>=0.7.1,<0.8.0']

setup_kwargs = {
    'name': 'nem-bidding-dashboard',
    'version': '0.10.0',
    'description': 'A dashboard for visualising bidding data for the National Energy Market',
    'long_description': '## Introduction\n\nnem-bidding-dashboard is a web app and python package for collating, processing and visualising data relevant to\nunderstanding participant behaviour in the Australian National Electricity Market wholesale spot market.\n\nThe web app is intended to make reviewing the bidding behaviour of market participants as easy as possible. Aggregate\nbehaviour can be visualised at a whole of market, regional, or technology level. Alternatively, the non-aggregated\nbids of dispatch units, and stations can be visualised.\n\nWe have additionally published the code required to run the web app as a python package, so that it can be used to help\nvisualise and analyse bidding behaviour in alternative or more sophisticated ways than allowed by the web app.\n\nThe development of nem-bidding-dashboard was funded by the [Digital Grid Futures Institute](https://www.dgfi.unsw.\nedu.au/)\n\n## Status\n\nUnderdevelopment and not recommended for use yet, check back here in early 2023 to see if a production version has been\nlaunched.\n\n## Web app\n\nnem-bidding-dashboard is hosted as a web app here: [http://nembiddingdashboard.org](http://nembiddingdashboard.org)\n\n## Python package / API\n\nThe python api can be used to:\n- run the web app interface locally\n- download publicly available bidding and operational data from the Australian Energy Market Operator\n- process and aggregate bidding and operational data into the format used in the web app\n- build and populate a PostgresSQL database for efficiently querying and aggregating bidding and operational data\n\n### Installation\n\n`pip install nem_bidding_dashboard`\n\n### Quick examples\n\nBelow are some quick examples that provide a taste of the api capabilities, see the full set of examples and api\ndocumentation for a complete guide.\n\n#### Get raw data\nTo get the raw data used by nem-bidding-dashboard before preprocessing use functions in the `fetch_data` module, e.g.\n`get_volume_bids`.\n\n```python\nfrom nem_bidding_dashboard import fetch_data\n\nvolume_bids = fetch_data.get_volume_bids(\n    start_time=\'2022/01/01 00:00:00\',\n    end_time=\'2022/01/01 00:05:00\',\n    raw_data_cache=\'D:/nemosis_data_cache\')\n\nprint(volume_bids.head(5))\n#        SETTLEMENTDATE     DUID  ... PASAAVAILABILITY   INTERVAL_DATETIME\n# 309360     2021-12-31  ADPBA1G  ...              6.0 2022-01-01 00:05:00\n# 309361     2021-12-31  ADPBA1G  ...              NaN 2022-01-01 00:05:00\n# 309362     2021-12-31  ADPBA1G  ...              NaN 2022-01-01 00:05:00\n# 309363     2021-12-31  ADPBA1G  ...              NaN 2022-01-01 00:05:00\n# 309364     2021-12-31  ADPBA1G  ...              NaN 2022-01-01 00:05:00\n#\n# [5 rows x 18 columns]\n```\n\n#### Get processed data\nTo get data in the format stored by nem-bidding-dashboard in the PostgresSQL database use functions in the module\n`fetch_and_preprocess`, e.g. `bid_data`.\n\n```python\nfrom nem_bidding_dashboard import fetch_and_preprocess\n\nbids = fetch_and_preprocess.bid_data(\n    start_time=\'2022/01/01 00:00:00\',\n    end_time=\'2022/01/01 00:05:00\',\n    raw_data_cache=\'D:/nemosis_data_cache\')\n\nprint(bids.head(5))\n#        INTERVAL_DATETIME     DUID  BIDBAND  BIDVOLUME  BIDVOLUMEADJUSTED  BIDPRICE  ONHOUR\n# 0    2022-01-01 00:05:00  ADPBA1G        8          6                0.0    998.00   False\n# 462  2022-01-01 00:05:00   REECE1        2         45               45.0    -55.03   False\n# 463  2022-01-01 00:05:00   REECE1        4         74               74.0     -0.85   False\n# 464  2022-01-01 00:05:00   REECE2        2         35               35.0    -54.77   False\n# 465  2022-01-01 00:05:00   REECE2        4         84               84.0     -0.86   False\n```\n\n#### Setup a PostgresSQL database\n\nCreate tables for storing processed data and functions, then populate the database with historical data.\n\n```python\nfrom nem_bidding_dashboard import postgres_helpers, populate_postgres_db\n\ncon_string = postgres_helpers.build_connection_string(\n    hostname=\'localhost\',\n    dbname=\'bidding_dashboard_db\',\n    username=\'bidding_dashboard_maintainer\',\n    password=\'1234abcd\',\n    port=5433)\n\nraw_data_cache = "D:/nemosis_cache"\nstart = "2022/01/01 00:00:00"\nend = "2022/02/01 00:00:00"\n\npopulate_postgres_db.duid_info(con_string, raw_data_cache)\npopulate_postgres_db.bid_data(con_string, raw_data_cache, start, end)\npopulate_postgres_db.region_data(con_string, raw_data_cache, start, end)\npopulate_postgres_db.unit_dispatch(con_string, raw_data_cache, start, end)\n```\n\n#### Query and aggregate bidding data from PostgresSQL database\n\nFilter bids by time and region, and then aggregate into price bands. Other functions in the module `query_postgres_db`\nprovide querying and aggregation and for each table in the db.\n\n```python\nfrom nem_bidding_dashboard import postgres_helpers, query_postgres_db\n\ncon_string = postgres_helpers.build_connection_string(\n    hostname=\'localhost\',\n    dbname=\'bidding_dashboard_db\',\n    username=\'bidding_dashboard_maintainer\',\n    password=\'1234abcd\',\n    port=5433)\n\nagg_bids = query_postgres_db.aggregate_bids(connection_string=con_string,\n                                            start_time="2022/01/01 00:00:00",\n                                            end_time="2022/01/01 01:00:00",\n                                            regions=[\'QLD\', \'NSW\', \'SA\'],\n                                            dispatch_type=\'Generator\',\n                                            tech_types=[],\n                                            resolution=\'hourly\',\n                                            adjusted=\'adjusted\')\n\nprint(agg_bids)\n#       INTERVAL_DATETIME        BIN_NAME   BIDVOLUME\n# 0   2022-01-01 01:00:00   [-1000, -100)  9673.93400\n# 1   2022-01-01 01:00:00       [-100, 0)   366.70236\n# 2   2022-01-01 01:00:00         [0, 50)  1527.00000\n# 3   2022-01-01 01:00:00       [50, 100)  1290.00000\n# 4   2022-01-01 01:00:00      [100, 200)   908.00000\n# 5   2022-01-01 01:00:00      [200, 300)  1217.00000\n# 6   2022-01-01 01:00:00      [300, 500)   943.00000\n# 7   2022-01-01 01:00:00     [500, 1000)   240.00000\n# 8   2022-01-01 01:00:00    [1000, 5000)   210.00000\n# 9   2022-01-01 01:00:00   [5000, 10000)   125.00000\n# 10  2022-01-01 01:00:00  [10000, 15500)  6766.00000\n```\n\n## Contributing\n\nInterested in contributing? Check out the [contributing guidelines](https://github.com/UNSW-CEEM/nem-bidding-dashboard/blob/master/CONTRIBUTING.md).\n\nPlease note that this project is released with a [Code of Conduct](https://github.com/UNSW-CEEM/nem-bidding-dashboard/blob/master/CONDUCT.md). By contributing to this project, you\nagree to abide by its terms.\n\n## License and Disclaimer\n\n`nem-bidding-dashboard` was created by `Nicholas Gorman` and `Patrick Chambers`. It is licensed under the terms of the\n[`BSD-3-Clause license`](https://github.com/UNSW-CEEM/nem-bidding-dashboard/blob/master/LICENSE). Please, also read the\ndisclaimer accompanying the licence\n',
    'author': 'Patrick Chambers',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
