# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gsheets_unify_adapter',
 'gsheets_unify_adapter.tests',
 'unify',
 'unify.rest_specs',
 'unify.tests',
 'unify_kernel']

package_data = \
{'': ['*'],
 'unify.rest_specs': ['beta/*', 'tests/*'],
 'unify.tests': ['files/*']}

install_requires = \
['altair-viewer>=0.4.0,<0.5.0',
 'altair>=4.2.0,<5.0.0',
 'clickhouse-driver>=0.2.5,<0.3.0',
 'clickhouse-sqlalchemy>=0.2.3,<0.3.0',
 'duckdb-engine>=0.6.8,<0.7.0',
 'duckdb>=0.6.1,<0.7.0',
 'google-api-python-client>=2.70.0,<3.0.0',
 'google-auth-httplib2>=0.1.0,<0.2.0',
 'google-auth-oauthlib>=0.8.0,<0.9.0',
 'ipykernel>=6.19.4,<7.0.0',
 'ipynbname>=2021.3.2,<2022.0.0',
 'jsonpath-ng>=1.5.3,<2.0.0',
 'lark>=1.1.5,<2.0.0',
 'nb2mail-unify>=0.6,<0.7',
 'pandas>=1.5.2,<2.0.0',
 'prompt-toolkit>=3.0.36,<4.0.0',
 'pyaml>=21.10.1,<22.0.0',
 'pyarrow>=10.0.1,<11.0.0',
 'pytest>=7.2.0,<8.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'pyzmq>=24.0.1,<25.0.0',
 'redmail>=0.4.2,<0.5.0',
 'requests-aws4auth>=1.1.2,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'signaling>=1.0.0,<2.0.0',
 'sqlalchemy>=1.4.45,<2.0.0',
 'sqlglot>=10.3.2,<11.0.0']

entry_points = \
{'console_scripts': ['unify = unify.__main__:main']}

setup_kwargs = {
    'name': 'unifydb',
    'version': '0.2.3',
    'description': 'Your personal data warehouse',
    'long_description': '# Unify\n\nUnify is an experiment in building a "personal data warehouse". It integrates Extract-Transform-Load,\nplus analysis, into a single app and database which runs on your local machine.\n\nThe primary interface to Unify is a command interface which mixes [standard SQL and\nmeta](./docs/SQL_LANGUAGE.md) commands. Use `select` to query data, but you also have commands available for\neasily importing and exporting data, sending email, and drawing charts.\n\nUnify includes a set of *connectors* to popular SaaS systems, and allows you to easily\ncreate new connectors to systems with REST APIs via a simple configuation file. Connectors \nautomatically flatten JSON responses into relational tables that are easy to query with SQL. \n\nUnify offers a columnar store \'database backend\' (either DuckDB or Clickouse) which can\nefficiently store and analyze tens of millions of rows of data.\n\nUnify **should** be the easiest way to pull data from a REST API and materialize\nit into a database suitable for SQL analysis.\n\n## Example\n\nEstablish a connection to the Github API:\n\n    > connect\n    1: aws_costs\n    2: coda\n    3: datadog\n    4: github\n    Pick a connector: 4\n    Ok! Let\'s setup a new github connection.\n    Specify the schema name (github):\n    Please provide the configuration parameters:\n    username (Github user email): johnsmith@example.com\n    password (Github personal access token): ghp_Jik22xkF88wmzzj8xxks2x2jz\n    Testing connection...\n    New github connection created in schema github\n    The following tables are available, use peek or select to load data:\n    8 rows\n    table_name table_schema                                            comment materialized\n        pulls       github                                               None            ☐\n        repos       github                                               None            ☐\n        users       github                                               None            ☐\n    >\n\nAfter creating the connection, you can query your list of repos:\n\n    > select id, name, owner_login, open_issues_count from github.repos;\n    Loading data for table: github.repos\n    ...\n    id                                  name owner_login      open_issues_count\n    51189180                     dep-checker linuxfoundation             74\n    51713527                    code-janitor linuxfoundation              0\n    63492894                    foss-barcode linuxfoundation             30\n\n## Getting started\n\nInstall Unify:\n\n    $ pip install unifydb\n\nAnd run:\n\n    $ unify\n\nWhen you first run you need to choose your database backend. DuckDB is simpler to get started with\n(and supported on Windows), but it doesn\'t handle access from multiple processes well. \nClickhouse is a little more work to setup, but works a lot better with other tools like BI tools.\nIf you are running on Windows, you can get a cloud Clickhouse instance at [clickhouse.com](https://clickhouse.com).\n\nAll configuration data is stored into `$HOME/unify`. Set `UNIFY_HOME` in your environment\nif you want to store config data somewhere else.\n\n**Checkout the [tutorial](docs/TUTORIAL.md) to get an overview of using Unify to work with your data.**\n\n## Learning more\n\n* Read about the list of [current connectors](docs/CONNECTORS.md).\n* Learn about [building](docs/BUILDING_CONNECTORS.md) new connectors.\n* Get an overview of [all commands](docs/SQL_LANGUAGE.md).\n\n## Limitations\n\n* This is **alpha** software. Use at your own risk! Good news is that API connectors only read data.\nIf you want to examine the code which interacts with your systems, checkout the [RESTConnector](https://github.com/scottpersinger/unify/blob/main/unify/rest_connector.py).\n* The schema and table layout are not stable yet, so upgrading Unify may change the database layout.\n* Test coverage is poor and bugs are numerous.\n\n## Developing\n\nTests use `pytest` and the project overall uses `poetry`. \n',
    'author': 'Scott Persinger',
    'author_email': 'scottpersinger@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/scottpersinger/unify',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
