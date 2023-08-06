# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pytest_parametrize_suite']

package_data = \
{'': ['*']}

install_requires = \
['pytest']

extras_require = \
{':python_version < "3.10"': ['typing-extensions>=4.4.0,<5.0.0']}

entry_points = \
{'pytest11': ['suite = pytest_parametrize_suite.plugin']}

setup_kwargs = {
    'name': 'pytest-parametrize-suite',
    'version': '23.1.1',
    'description': 'A simple pytest extension for creating a named test suite.',
    'long_description': '# Pytest (Parametrize) Suite\n\n[![image](https://img.shields.io/pypi/v/pytest-parametrize-suite.svg)](https://pypi.org/project/pytest-parametrize-suite/)\n[![image](https://img.shields.io/pypi/l/pytest-parametrize-suite.svg)](https://pypi.org/project/pytest-parametrize-suite/)\n[![image](https://img.shields.io/pypi/pyversions/pytest-parametrize-suite.svg)](https://pypi.org/project/pytest-parametrize-suite/)\n[![image](https://img.shields.io/github/languages/code-size/seandstewart/pytest-parametrize-suite.svg?style=flat)](https://github.com/seandstewart/pytest-parametrize-suite)\n[![Test & Lint](https://github.com/seandstewart/pytest-parametrize-suite/workflows/Test/badge.svg)](https://github.com/seandstewart/pytest-parametrize-suite/actions)\n[![Coverage](https://codecov.io/gh/seandstewart/pytest-parametrize-suite/branch/main/graph/badge.svg)](https://codecov.io/gh/seandstewart/pytest-parametrize-suite)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n\nA tiny plugin for writing clean, easy-to-read, parametrized tests in pytest.\n\n## Why?\n\nPytest\'s `parametrize` is a powerful way to write input-output testing to rapidly \nexpand your test coverage while minimizing the number of test assertions you must \nwrite. Unfortunately, as the complexity of your test suite grows, it can become \ndifficult to keep track of individual test cases.\n\nOne way to get cleaner test output is by assigning descriptive `ids` and `argnames` to \neach parametrized case. However, the current methodologies available result in either \nvery verbose setup, or difficult-to-track ids and names.\n\nEnter `pytest-parametrize-suite`. With this marker, you define your test ids and \nnames in-line with the values you intend to pass into your test, keeping your \nidentifiers tightly coupled to your test cases and encouraging a delightful testing \nexperience as a result.\n\n## Quickstart\n\n### Install With PIP\n\n```shell\npip install -U pytest-parametrize-suite\n```\n\n### Install With Poetry\n\n```shell\npoetry add --group=test pytest-parametrize-suite\n```\n\n## Using the plugin\n\nThe plugin provides a single entrypoint in a pytest marker called `suite`. \n\nThe `suite`\nmarker takes any number of keyword arguments. Each entry in should be a Mapping of \n`argname->argvalue` and all entries should be the same exact shape.\n\nThis gives developers the ability to \n\n#### Example\n\n**Given the following module:**\n\n```python\n# iso8601.py\n\nfrom __future__ import annotations\n\nimport datetime\n\n\ndef iso8601(\n    date_obj: datetime.date | datetime.datetime | datetime.time | datetime.timedelta\n) -> str:\n    """Format a Python date/time object into an ISO8601 string."""\n\n    if isinstance(date_obj, (datetime.date, datetime.time)):\n        return date_obj.isoformat()\n    if isinstance(date_obj, datetime.timedelta):\n        return timedelta_isoformat(date_obj)\n    raise ValueError(\n        f"Unrecognized value of type: {date_obj.__class__.__name__}: {date_obj}"\n    )\n\n\ndef timedelta_isoformat(delta: datetime.timedelta) -> str:\n    """Why isn\'t this part of the stdlib?"""\n    usecs = abs(\n        (delta.days * 24 * 60 * 60 + delta.seconds) * 1000000 + delta.microseconds\n    )\n    seconds, usecs = divmod(usecs, 1000000)\n    minutes, seconds = divmod(seconds, 60)\n    hours, minutes = divmod(minutes, 60)\n    days, hours = divmod(hours, 24)\n    fmt = f"P{days}DT{hours}H{minutes}M{seconds}.{usecs:06}S"\n    return fmt\n\n```\n\n**Writing With pytest-parametrize-suite:**\n\n```python\n# test_iso8601.py\n\nfrom __future__ import annotations\n\nimport datetime\n\nimport pytest\n\nfrom example.iso8601 import iso8601\n\n\n@pytest.mark.suite(\n    datetime=dict(\n        given_date_obj=datetime.datetime(1970, 1, 1),\n        expected_date_str="1970-01-01T00:00:00",\n    ),\n    date=dict(\n        given_date_obj=datetime.date(1970, 1, 1),\n        expected_date_str="1970-01-01",\n    ),\n    time=dict(\n        given_date_obj=datetime.time(),\n        expected_date_str="00:00:00",\n    ),\n    timedelta=dict(\n        given_date_obj=datetime.timedelta(1, 1, 1),\n        expected_date_str="P1DT1.000001S",\n    )\n)\ndef test_iso8601(given_date_obj, expected_date_str):\n    # When\n    date_str = iso8601(given_date_obj)\n    # Then\n    assert date_str == expected_date_str\n\n```\n\n**Writing Without pytest-parametrize-suite:**\n\n```python\n# test_iso8601.py\n\nfrom __future__ import annotations\n\nimport datetime\n\nimport pytest\n\nfrom example.iso8601 import iso8601\n\n\n@pytest.mark.parametrize(\n    argnames=("given_date_obj", "expected_date_str"),\n    argvalues=[\n        (datetime.datetime(1970, 1, 1), "1970-01-01T00:00:00"),\n        (datetime.date(1970, 1, 1), "1970-01-01"),\n        (datetime.time(), "00:00:00"),\n        (datetime.timedelta(1, 1, 1), "P1DT1.000001S")\n    ],\n    ids=["datetime", "date", "time", "timedelta"]\n)\ndef test_iso8601(given_date_obj, expected_date_str):\n    # When\n    date_str = iso8601(given_date_obj)\n    # Then\n    assert date_str == expected_date_str\n\n```\n\nRunning the test defined in the example outputs the following:\n\n```shell\n❯ pytest test_iso8601.py -v\n=============================== test session starts ===============================\nplatform darwin -- Python 3.11.0, pytest-7.2.1, pluggy-1.0.0 -- /Users/god/Library/Caches/pypoetry/virtualenvs/pytest-parametrize-suite-TGMGi3Zp-py3.11/bin/python\ncachedir: .pytest_cache\nrootdir: /Users/god/PycharmProjects/pytest-parametrize-suite\nplugins: parametrize-suite-23.1.0, cov-4.0.0\ncollected 4 items                                                                 \n\nsrc/pytest_parametrize_suite/example.py::test_iso8601[datetime] PASSED      [ 25%]\nsrc/pytest_parametrize_suite/example.py::test_iso8601[date] PASSED          [ 50%]\nsrc/pytest_parametrize_suite/example.py::test_iso8601[time] PASSED          [ 75%]\nsrc/pytest_parametrize_suite/example.py::test_iso8601[timedelta] PASSED     [100%]\n\n================================ 4 passed in 0.02s ================================\n```\n\nAs you can see, we get a developer-friendly output for our parametrized tests while \nminimizing the amount of cognitive overhead it takes to understand and develop our test \ncases.\n\nHappy testing! :white_check_mark:\n',
    'author': 'Sean Stewart',
    'author_email': 'sean_stewart@me.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8.1,<4.0',
}


setup(**setup_kwargs)
