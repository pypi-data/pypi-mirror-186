# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_rql']

package_data = \
{'': ['*']}

install_requires = \
['cachetools>=4.2.4', 'lark-parser==0.11.0', 'python-dateutil>=2.8.2']

setup_kwargs = {
    'name': 'lib-rql',
    'version': '1.1.6',
    'description': 'Python RQL Filtering',
    'long_description': '# Python RQL\n\n\n[![pyversions](https://img.shields.io/pypi/pyversions/lib-rql.svg)](https://pypi.org/project/lib-rql/)\n[![PyPi Status](https://img.shields.io/pypi/v/lib-rql.svg)](https://pypi.org/project/lib-rql/)\n[![PyPI status](https://img.shields.io/pypi/status/lib-rql.svg)](https://pypi.org/project/lib-rql/)\n[![PyPI Downloads](https://img.shields.io/pypi/dm/lib-rql)](https://pypi.org/project/lib-rql/)\n[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=lib-rql&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=lib-rql)\n[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=lib-rql&metric=coverage)](https://sonarcloud.io/summary/new_code?id=lib-rql)\n\n\n\n## Introduction\n\nRQL (Resource query language) is designed for modern application development. It is built for the web, ready for NoSQL, and highly extensible with simple syntax.\nThis is a query language fast and convenient database interaction. RQL was designed for use in URLs to request object-style data structures.\n\n[RQL Reference](https://connect.cloudblue.com/community/api/rql/)\n\n## Install\n\n`Python RQL` can be installed from [pypi.org](https://pypi.org/project/lib-rql/) using pip:\n\n```\n$ pip install lib-rql\n```\n\n## Documentation\n\n[`Python RQL` documentation](https://lib-rql.readthedocs.io/en/latest/) is hosted on the _Read the Docs_ service.\n\n\n## Projects using Python RQL\n\n`Django RQL` is the Django app, that adds RQL filtering to your application.\n\nVisit the [Django RQL](https://github.com/cloudblue/django-rql) project repository for more informations.\n\n\n## Notes\n\nParsing is done with [Lark](https://github.com/lark-parser/lark) ([cheatsheet](https://lark-parser.readthedocs.io/en/latest/lark_cheatsheet.pdf)).\nThe current parsing algorithm is [LALR(1)](https://www.wikiwand.com/en/LALR_parser) with standard lexer.\n\n0. Values with whitespaces or special characters, like \',\' need to have "" or \'\'\n1. Supported date format is ISO8601: 2019-02-12\n2. Supported datetime format is ISO8601: 2019-02-12T10:02:00 / 2019-02-12T10:02Z / 2019-02-12T10:02:00+03:00\n\n\n## Supported operators\n\n1. Comparison (eq, ne, gt, ge, lt, le, like, ilike, search)\n2. List (in, out)\n3. Logical (and, or, not)\n4. Constants (null(), empty())\n5. Ordering (ordering)\n6. Select (select)\n7. Tuple (t)\n\n\n## Examples\n\n### Parsing a RQL query\n\n\n```python\nfrom py_rql import parse\nfrom py_rql.exceptions import RQLFilterError\n\ntry:\n    tree = parse(\'eq(key,value)\')\nexcept RQLFilterError:\n    pass\n```\n\n\n### Filter a list of dictionaries\n\n```python\nfrom py_rql.constants import FilterTypes\nfrom py_rql.filter_cls import FilterClass\n\n\nclass BookFilter(FilterClass):\n    FILTERS = [\n        {\n            \'filter\': \'title\',\n        },\n        {\n            \'filter\': \'author.name\',\n        },\n        {\n            \'filter\': \'status\',\n        },\n        {\n            \'filter\': \'pages\',\n            \'type\': FilterTypes.INT,\n        },\n        {\n            \'filter\': \'featured\',\n            \'type\': FilterTypes.BOOLEAN,\n        },\n        {\n            \'filter\': \'publish_date\',\n            \'type\': FilterTypes.DATETIME,\n        },\n    ]\n\nfilters = BookFilter()\n\nquery = \'eq(title,Practical Modern JavaScript)\'\nresults = list(filters.filter(query, DATA))\n\nprint(results)\n\nquery = \'or(eq(pages,472),lt(pages,400))\'\nresults = list(filters.filter(query, DATA))\n\nprint(results)\n```\n\n\n## Development\n\n\n1. Python 3.7+\n0. Install dependencies `pip install poetry && poetry install`\n\n## Testing\n\n1. Python 3.7+\n0. Install dependencies `pip install poetry && poetry install`\n\nCheck code style: `poetry run flake8`\nRun tests: `poetry run pytest`\n\nTests reports are generated in `tests/reports`.\n* `out.xml` - JUnit test results\n* `coverage.xml` - Coverage xml results\n\nTo generate HTML coverage reports use:\n`--cov-report html:tests/reports/cov_html`\n\n## License\n\n`Python RQL` is released under the [Apache License Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).\n',
    'author': 'CloudBlue LLC',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://connect.cloudblue.com/community/api/rql/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
