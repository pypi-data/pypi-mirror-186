# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['task_script_utils',
 'task_script_utils.datetime_parser',
 'task_script_utils.datetime_parser.utils']

package_data = \
{'': ['*'], 'task_script_utils.datetime_parser': ['flowcharts/*']}

install_requires = \
['arrow>=1.2.2,<2.0.0',
 'dateparser>=1.1.1,<2.0.0',
 'pendulum>=2.1.2,<3.0.0',
 'pydash>=5.1.0,<6.0.0',
 'python-dateutil>=2.8.2,<3.0.0']

setup_kwargs = {
    'name': 'ts-task-script-utils',
    'version': '1.4.0',
    'description': 'Python utility for Tetra Task Scripts',
    'long_description': '# ts-task-script-utils <!-- omit in toc -->\n\n[![Build Status](https://travis-ci.com/tetrascience/ts-task-script-utils.svg?branch=master)](https://travis-ci.com/tetrascience/ts-task-script-utils)\n\n## Version <!-- omit in toc -->\n\nv1.4.0\n\n## Table of Contents <!-- omit in toc -->\n\n- [Installation](#installation)\n- [Usage](#usage)\n- [Datetime Parser](#datetime-parser)\n  - [`parse` Usage](#parse-usage)\n- [Changelog](#changelog)\n  - [v1.4.0](#v140)\n  - [v1.3.1](#v131)\n  - [v1.3.0](#v130)\n  - [v1.2.0](#v120)\n  - [v1.1.1](#v111)\n  - [v1.1.0](#v110)\n\n## Summary\n\nUtility functions for Tetra Task Scripts\n\n## Installation\n\n`pip install ts-task-script-utils`\n\n## Usage\n\n```python\nfrom task_script_utils.parse import to_int\n\nstring_value = \'1.0\'\nint_value = to_int(string_value)\n\n# `int_value` now has the parsed value of the string\nassert isinstance(int_value, int)\nassert int_value == 1\n\n# it returns `None` if the value is unparseable\nstring_value = \'not an int\'\nint_value = to_int(string_value)\n\nassert int_value is None\n```\n\n## Datetime Parser\n\n**DEPRECATION WARNING!**\n\n- Do not use the old datetime parser:\n  `convert_datetime_to_ts_format` (from `task_script_utils.convert_datetime_to_ts_format`)\n- Instead, use the newer `parse` from `task_script_utils.datetime_parser`\n\n### `parse` Usage\n\n```python\nfrom task_script_utils.datetime_parser import parse\n\nparse("2004-12-23T12:30 AM +05:30")\nparse("2004-12-23T12:30 AM +05:30", <format_list>)\nparse("2004-12-23T12:30 AM +05:30", <format_list>, <datetime_config>)\n```\n\n`prase()` returns a `TSDatetime` Object. You can use `TSDatetime.tsformat()` and\n`TSDatetime.isoformat()` to get datetime string. You can also use\n`TSDatetime.datetime()` to access python datetime object.\n\nYou can read more about the datetime parser [here](task_script_utils/datetime_parser/README.md).\n\n## Changelog\n\n### v1.4.0\n\n- Add `extract-to-decorate` functions\n\n### v1.3.1\n\n- Update datetime parser usage in README.md\n\n### v1.3.0\n\n- Added string parsing functions\n\n### v1.2.0\n\n- Add boolean config parameter `require_unambiguous_formats` to `DatetimeConfig`\n- Add logic to `parser._parse_with_formats` to be used when `DatetimeConfig.require_unambiguous_formats` is set to `True`\n  - `AmbiguousDatetimeFormatsError` is raised if mutually ambiguous formats are detected and differing datetimes are parsed\n- Add parameter typing throughout repository\n- Refactor `datetime_parser` package\n- Add base class `DateTimeInfo`\n- Segregate parsing logic into `ShortDateTimeInfo` and `LongDateTimeInfo`\n\n### v1.1.1\n\n- Remove `convert_to_ts_iso8601()` method\n\n### v1.1.0\n\n- Add `datetime_parser` package\n',
    'author': 'Tetrascience',
    'author_email': 'developers@tetrascience.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
