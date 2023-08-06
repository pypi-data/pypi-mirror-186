import sys
from functools import wraps
from typing import List, Any, Tuple, Dict, Iterable, Callable, TypeVar, Any
if sys.version_info < (3, 10):
    from typing_extensions import ParamSpec
else:
    from typing import ParamSpec
from water_cli.parser import Flag, MCallable
from water_cli.exceptions import ExclusiveFlags, MissingRequiredCombination

R = TypeVar('R')
P = ParamSpec('P')

def _check_kwargs_together(kwargs: Dict[str, Any], flags_list: List[Tuple[str, ...]]) -> None:
    provided_keys = set()
    for k, v in kwargs.items():
        if not isinstance(v, Flag):
            provided_keys.add(k)
            continue

        if isinstance(v, Flag) and v.checked:
            provided_keys.add(k)
            continue

    for required_pairs in flags_list:
        _inc = set(required_pairs)
        missing = _inc - provided_keys
        present = provided_keys.intersection(_inc)
        if missing and present:
            raise MissingRequiredCombination(tuple(present), tuple(missing))
    return


def _check_kwargs_exclusive(kwargs: Dict[str, Any], flags_list: List[Tuple[str, ...]]) -> None:
    provided_keys = set()
    for k, v in kwargs.items():
        if not isinstance(v, Flag):
            provided_keys.add(k)
            continue

        if isinstance(v, Flag) and v.checked:
            provided_keys.add(k)
            continue

    for incompatible_pairs in flags_list:
        _inc = set(incompatible_pairs)
        if provided_keys.intersection(_inc) == _inc:
            raise ExclusiveFlags(incompatible_pairs)
    return


def exclusive_flags(_flags_list: List[Tuple[str, ...]]) -> Any:

    def wrapper(f: Callable[P, R]) -> Callable[P, R]:
        for _pairs in _flags_list:
            validate_argument_for_callable(_pairs, f)

        @wraps(f)
        def wrapped(*args: P.args, **kwargs: P.kwargs) -> R:
            _check_kwargs_exclusive(kwargs, _flags_list)
            return f(*args, **kwargs)
        return wrapped

    return wrapper


def validate_argument_for_callable(provided_args: Iterable[str], _callable: Callable[..., Any]) -> None:
    c = MCallable.from_callable(_callable, _callable.__name__, parent=None)
    callable_args = {a.name for a in c.args}
    _bad = set(provided_args) - callable_args
    if _bad:
        _bad_args = tuple(p for p in provided_args if p in _bad)
        raise ValueError(f"Received arguments: {_bad_args} for decorator, "
                         f"which are not accepted by '{_callable.__name__}'.")

def required_together(_flags_list: List[Tuple[str, ...]]) -> Any:
    def wrapper(f: Callable[P, R]) -> Callable[P, R]:
        for _pairs in _flags_list:
            validate_argument_for_callable(_pairs, f)

        @wraps(f)
        def wrapped(*args: P.args, **kwargs: P.kwargs) -> R:
            _check_kwargs_together(kwargs, _flags_list)
            return f(*args, **kwargs)
        return wrapped

    return wrapper
