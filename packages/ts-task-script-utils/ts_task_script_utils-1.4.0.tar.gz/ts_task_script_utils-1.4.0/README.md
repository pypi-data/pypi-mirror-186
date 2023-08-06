# ts-task-script-utils <!-- omit in toc -->

[![Build Status](https://travis-ci.com/tetrascience/ts-task-script-utils.svg?branch=master)](https://travis-ci.com/tetrascience/ts-task-script-utils)

## Version <!-- omit in toc -->

v1.4.0

## Table of Contents <!-- omit in toc -->

- [Installation](#installation)
- [Usage](#usage)
- [Datetime Parser](#datetime-parser)
  - [`parse` Usage](#parse-usage)
- [Changelog](#changelog)
  - [v1.4.0](#v140)
  - [v1.3.1](#v131)
  - [v1.3.0](#v130)
  - [v1.2.0](#v120)
  - [v1.1.1](#v111)
  - [v1.1.0](#v110)

## Summary

Utility functions for Tetra Task Scripts

## Installation

`pip install ts-task-script-utils`

## Usage

```python
from task_script_utils.parse import to_int

string_value = '1.0'
int_value = to_int(string_value)

# `int_value` now has the parsed value of the string
assert isinstance(int_value, int)
assert int_value == 1

# it returns `None` if the value is unparseable
string_value = 'not an int'
int_value = to_int(string_value)

assert int_value is None
```

## Datetime Parser

**DEPRECATION WARNING!**

- Do not use the old datetime parser:
  `convert_datetime_to_ts_format` (from `task_script_utils.convert_datetime_to_ts_format`)
- Instead, use the newer `parse` from `task_script_utils.datetime_parser`

### `parse` Usage

```python
from task_script_utils.datetime_parser import parse

parse("2004-12-23T12:30 AM +05:30")
parse("2004-12-23T12:30 AM +05:30", <format_list>)
parse("2004-12-23T12:30 AM +05:30", <format_list>, <datetime_config>)
```

`prase()` returns a `TSDatetime` Object. You can use `TSDatetime.tsformat()` and
`TSDatetime.isoformat()` to get datetime string. You can also use
`TSDatetime.datetime()` to access python datetime object.

You can read more about the datetime parser [here](task_script_utils/datetime_parser/README.md).

## Changelog

### v1.4.0

- Add `extract-to-decorate` functions

### v1.3.1

- Update datetime parser usage in README.md

### v1.3.0

- Added string parsing functions

### v1.2.0

- Add boolean config parameter `require_unambiguous_formats` to `DatetimeConfig`
- Add logic to `parser._parse_with_formats` to be used when `DatetimeConfig.require_unambiguous_formats` is set to `True`
  - `AmbiguousDatetimeFormatsError` is raised if mutually ambiguous formats are detected and differing datetimes are parsed
- Add parameter typing throughout repository
- Refactor `datetime_parser` package
- Add base class `DateTimeInfo`
- Segregate parsing logic into `ShortDateTimeInfo` and `LongDateTimeInfo`

### v1.1.1

- Remove `convert_to_ts_iso8601()` method

### v1.1.0

- Add `datetime_parser` package
