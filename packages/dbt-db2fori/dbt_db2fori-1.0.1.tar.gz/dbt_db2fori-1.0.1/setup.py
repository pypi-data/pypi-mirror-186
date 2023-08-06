# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dbt', 'dbt.adapters.db2_for_i', 'dbt.include.db2_for_i']

package_data = \
{'': ['*'],
 'dbt.include.db2_for_i': ['macros/*',
                           'macros/materializations/incremental/*',
                           'macros/materializations/seed/*',
                           'macros/materializations/snapshot/*',
                           'macros/materializations/tests/*']}

install_requires = \
['dbt-core>=1.3.2,<2.0.0', 'pyodbc>=4.0.35,<5.0.0']

setup_kwargs = {
    'name': 'dbt-db2fori',
    'version': '1.0.1',
    'description': 'dbt adapter for IBM db2 for i',
    'long_description': "# dbt-db2fori\n\nA [dbt](https://www.getdbt.com/) adapter for IBM's DB2 for i v7.2+. The connection to the warehouse is through `ODBC` and requires that `pyodbc` is installed. All credits to [dbt-sqlserver adapter](https://github.com/dbt-msft/dbt-sqlserver) and [dbt-ibmdb2](https://github.com/aurany/dbt-ibmdb2) projects that heavily inspired this adapter.\n\n## Why this adapter?\nA similar adapter [dbt-ibmdb2](https://github.com/aurany/dbt-ibmdb2) exists, however, [dbt-ibmdb2](https://github.com/aurany/dbt-ibmdb2) uses the `ibm_db` Python package to connect to IBM DB2. This adapter connects to the warehouse using `pyodbc`\n\n## Features\nThe following materializations are supported:\n\n- Incremental\n- Snapshot\n- View\n- Table\n\nEphemeral models have not been tested yet. \n\n\n## Installation\nUse pip to install:\n```bash\npip install dbt-db2fori\n```\nAn example `profiles.yml` is:\n```bash\ndefault:\n    outputs:\n        dev:\n            type: db2_for_i\n            threads: 4\n            driver: IBM i Access ODBC Driver\n            system: system\n            username: username\n            password: password\n            database: db\n            schema: schema\n\n    target: dev\n```\n\nTo report a bug or request a feature, open an [issue](https://github.com/kaysef/dbt-db2fori/issues/new)\n",
    'author': 'Seth O',
    'author_email': 'sdowusu@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kaysef/dbt-db2fori',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
