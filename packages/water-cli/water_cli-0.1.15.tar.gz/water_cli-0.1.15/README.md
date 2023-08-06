# Water

[![codecov](https://codecov.io/gh/davidventura/water/branch/master/graph/badge.svg?token=m5obuvwZ0I)](https://codecov.io/gh/davidventura/water)

Like [fire](https://github.com/google/python-fire)

This python library parses classes so that they can be executed as commands.  
In contrast with fire, there is no "automatic" type casting -- the type casting is 100% based on type hints.

## Type casting

When calling `execute_command` the values passed in the command get casted to the annotated types on the function
signature.

Supported types:

* int, float
* bool: the strings `['true', '1', 't', 'y']` are considered true.
* lists, tuples: input is split by comma (`,`) and each element is casted independently.
* enum
* Union[]: gets casted to all options in order, first success is returned.
  * `Optional[type]` is `Union[type, NoneType]`
* `water.Flag`: flag, only denotes the switch was present.
* `water.Repeated[T]`: Effectively the same as `List[T]` but allows flags to be repeated and values will be concatenated

## Utilities

* `exclusive_flags` forbids certain flag combinations to be used at the same time.
  * If `--a` and `--b` are exclusive, executing `command --a --b` causes an error.
* `required_together` requires certain flag combinations to be used at the same time.
  * If `--a` and `--b` are required together, executing `command --a` or `command --b` causes an error.

# Examples

## Type casting

```python
class Math1:

    def add_list(self, items: Optional[List[int]] = None):
        if not items:
            return 0
        return sum(items)

    def add_numbers(self, number: Repeated[int]):
        return sum(number)

# `items` casted to a list of `int`
res = execute_command(Math1, 'add_list --items 1,2,3')
assert res == 6

# `items` casted to a list of `int`, even though there is only one entry
res = execute_command(Math1, 'add_list --items 1')
assert res == 1

# `number` casted to a list of `int`, even though there is only one entry
res = execute_command(Math1, 'add_numbers --number 1')
assert res == 1

# `number` casted to a list of `int`, even though there is only one entry
res = execute_command(Math1, 'add_numbers --number 1 --number 2')
assert res == 3
```

## Nested commands

```python
class NestedObj:
    class Inside1:
        def fn1(self, number: int):
            return number

res = execute_command(NestedObj, 'Inside1 fn1 --number 1')
assert res == 1
```


# Testing

Python3.9, 3.11:
```
docker build -f dockerfiles/3.9-Dockerfile .
docker build -f dockerfiles/3.11-Dockerfile .
```

Development
```
poetry run pytest
```

# Releasing

```
poetry publish --build --username $PYPI_USERNAME --password $PYPI_PASSWORD
```
