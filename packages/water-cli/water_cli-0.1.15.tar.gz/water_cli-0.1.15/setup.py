# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['water_cli']

package_data = \
{'': ['*']}

extras_require = \
{':python_version < "3.10"': ['typing-extensions>=4.0.0,<5.0.0']}

setup_kwargs = {
    'name': 'water-cli',
    'version': '0.1.15',
    'description': '',
    'long_description': '# Water\n\n[![codecov](https://codecov.io/gh/davidventura/water/branch/master/graph/badge.svg?token=m5obuvwZ0I)](https://codecov.io/gh/davidventura/water)\n\nLike [fire](https://github.com/google/python-fire)\n\nThis python library parses classes so that they can be executed as commands.  \nIn contrast with fire, there is no "automatic" type casting -- the type casting is 100% based on type hints.\n\n## Type casting\n\nWhen calling `execute_command` the values passed in the command get casted to the annotated types on the function\nsignature.\n\nSupported types:\n\n* int, float\n* bool: the strings `[\'true\', \'1\', \'t\', \'y\']` are considered true.\n* lists, tuples: input is split by comma (`,`) and each element is casted independently.\n* enum\n* Union[]: gets casted to all options in order, first success is returned.\n  * `Optional[type]` is `Union[type, NoneType]`\n* `water.Flag`: flag, only denotes the switch was present.\n* `water.Repeated[T]`: Effectively the same as `List[T]` but allows flags to be repeated and values will be concatenated\n\n## Utilities\n\n* `exclusive_flags` forbids certain flag combinations to be used at the same time.\n  * If `--a` and `--b` are exclusive, executing `command --a --b` causes an error.\n* `required_together` requires certain flag combinations to be used at the same time.\n  * If `--a` and `--b` are required together, executing `command --a` or `command --b` causes an error.\n\n# Examples\n\n## Type casting\n\n```python\nclass Math1:\n\n    def add_list(self, items: Optional[List[int]] = None):\n        if not items:\n            return 0\n        return sum(items)\n\n    def add_numbers(self, number: Repeated[int]):\n        return sum(number)\n\n# `items` casted to a list of `int`\nres = execute_command(Math1, \'add_list --items 1,2,3\')\nassert res == 6\n\n# `items` casted to a list of `int`, even though there is only one entry\nres = execute_command(Math1, \'add_list --items 1\')\nassert res == 1\n\n# `number` casted to a list of `int`, even though there is only one entry\nres = execute_command(Math1, \'add_numbers --number 1\')\nassert res == 1\n\n# `number` casted to a list of `int`, even though there is only one entry\nres = execute_command(Math1, \'add_numbers --number 1 --number 2\')\nassert res == 3\n```\n\n## Nested commands\n\n```python\nclass NestedObj:\n    class Inside1:\n        def fn1(self, number: int):\n            return number\n\nres = execute_command(NestedObj, \'Inside1 fn1 --number 1\')\nassert res == 1\n```\n\n\n# Testing\n\nPython3.9, 3.11:\n```\ndocker build -f dockerfiles/3.9-Dockerfile .\ndocker build -f dockerfiles/3.11-Dockerfile .\n```\n\nDevelopment\n```\npoetry run pytest\n```\n\n# Releasing\n\n```\npoetry publish --build --username $PYPI_USERNAME --password $PYPI_PASSWORD\n```\n',
    'author': 'david',
    'author_email': 'davidventura27@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/DavidVentura/water',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
