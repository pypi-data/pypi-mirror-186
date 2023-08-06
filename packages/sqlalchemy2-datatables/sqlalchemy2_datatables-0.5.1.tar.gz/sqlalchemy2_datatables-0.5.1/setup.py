# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['datatables']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.4,<2.0.0', 'sqlalchemy>=2.0.0rc2,<3.0.0']

setup_kwargs = {
    'name': 'sqlalchemy2-datatables',
    'version': '0.5.1',
    'description': 'Python Sqlalchemy 2.0 based serverside processing for jQuery datatables.',
    'long_description': '# sqlalchemy2-datatables\n\n[![versions](https://img.shields.io/pypi/pyversions/sqlalchemy2-datatables.svg)](https://github.com/hniedner/sqlalchemy2-datatables)\n[![license](https://img.shields.io/github/license/pydantic/pydantic.svg)](https://github.com/pydantic/pydantic/blob/main/LICENSE)\n[![Python package](https://github.com/coding-doc/sqlalchemy2-datatables/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/coding-doc/sqlalchemy2-datatables/actions/workflows/python-package.yml)\n---\n\n**Source Code**: [https://github.com/coding-doc/sqlalchemy2-datatables](https://github.com/coding-doc/sqlalchemy2-datatables)\n\n---\n### Summary\nsqlalchemy2-datatables is a framework agnostic library providing an SQLAlchemy integration of\njQuery DataTables >= 1.10, and helping you manage server side requests in your application.\n\n### Inspiration\nThis project was inspired by [sqlalchemyw-datatables](https://github.com/Pegase745/sqlalchemy-datatables)\ndeveloped by Michel Nemnom aka [Pegase745](https://github.com/Pegase745).\n\n### Motivation\nGiven the sunstantial changes with SQLAlchemy 2.0 most of not all of the SQLAlchemy based datatables serverside\n solution will be outdated soon (labeit currently still supported in SQLAlchemy 1.4). Specifically deprecation of\n sqlalchemy.orm.Query will render those packages obsolete.\n[SQLAlchemy2.0](https://docs.sqlalchemy.org/en/20/).\n\n### Installation\n```shell\npip install sqlalchemy2-datatables\n```\n\n### Examples\nGeneric CRUD style function:\n```python\nfrom typing import Any\nfrom sqlalchemy import Engine\nfrom sqlalchemy import FromClause\n\nfrom datatables import DataTable\nfrom datatables.base import DTDataCallbacks\n\ndef get_datatable_result(\n    params: dict[str, Any],\n    table: FromClause,\n    column_names: list[str],\n    engine: Engine,\n    callbacks: DTDataCallbacks | None,\n) -> dict[str, Any]:\n    """\n    Get database results specifically formatted for a display via jQuery datatables.\n    :param params: dict - request parameters\n    :param table: FromClause - the sqlalchemy from clause\n    :param column_names - List of column names reflecting the table columns in the desired order\n    :param engine: Engine -  the sqlalchemy engine\n    :param callbacks - datatables callbacks to populate jQuery datatables DT_* attributes\n    :return dict with DataTable output for the jQuery datatables in the frontend view\n    """\n    datatable: DataTable = DataTable(\n        request_params=params, table=table, column_names=column_names, engine=engine, callbacks=callbacks\n    )\n    return datatable.output_result()\n```\nthis will produce the dictionary that can be serialized and returned to jQuery datatables.\n```python\n{\n    "start": 0,\n    "length": 5,\n    "draw": 1,\n    "recordsTotal": 1341,\n    "recordsFiltered": 1341,\n    "data": [\n        {\n            "id": 1,\n            "col1": "value",\n            "col2": "value",\n            "col3": "value",\n            "col4": "value",\n        },\n        {\n            "id": 2,\n            "col1": "value",\n            "col2": "value",\n            "col3": "value",\n            "col4": "value",\n        },\n        {\n            "id": 3,\n            "col1": "value",\n            "col2": "value",\n            "col3": "value",\n            "col4": "value",\n        },\n        {\n            "id": 4,\n            "col1": "value",\n            "col2": "value",\n            "col3": "value",\n            "col4": "value",\n        },\n        {\n            "id": 5,\n            "col1": "value",\n            "col2": "value",\n            "col3": "value",\n            "col4": "value",\n        },\n    ],\n}\n```\n',
    'author': 'R. Hannes Niedner',
    'author_email': 'hniedner@gmail.com',
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
