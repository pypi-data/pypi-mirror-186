import enum
import inspect
import re
import shlex

from dataclasses import dataclass
from water_cli.exceptions import (BadArguments, BadSubcommand, UnexpectedParameters, MissingParameters,
                                  ConsecutiveValues, UnexpectedValue, MissingValues,
                                  )
from typing import List, Callable, Any, Tuple, Optional, Union, Dict, TypeVar

T = TypeVar('T')

class Repeated(List[T]):
    pass

class Flag:
    def __init__(self, checked: bool) -> None:
        self.checked = checked

    def __bool__(self) -> bool:
        return self.checked

def typing_get_args(a: Any) -> List[Any]:
    return getattr(a, '__args__', [])

def typing_get_origin(a: Any) -> Any:
    return getattr(a, '__origin__', a)


@dataclass
class MCallable:
    name: str
    args: List[inspect.Parameter]
    fn: Callable[..., Any]
    parent: Optional['Namespace']

    @staticmethod
    def from_callable(callable_root: Callable[..., Any], name: str, parent: Optional['Namespace']) -> 'MCallable':
        s = inspect.signature(callable_root)
        return MCallable(name=name,
                         args=list(s.parameters.values()),
                         fn=callable_root,
                         parent=parent)


@dataclass
class Namespace:
    name: str
    members: List['Namespace']
    callables: List[MCallable]
    parent: Optional['Namespace'] = None

    @staticmethod
    def from_callable(callable_root: Callable[..., Any], name: Optional[str]=None, parent: Optional['Namespace']=None) -> 'Namespace':
        if not name:
            name = callable_root.__name__
        if inspect.isclass(callable_root):
            callable_root = callable_root()

        _is_mod = inspect.ismodule(callable_root)

        _members = inspect.getmembers(callable_root, lambda x: inspect.isclass(x) or (not _is_mod and inspect.ismodule(x)))
        _methods = inspect.getmembers(callable_root, lambda x: inspect.ismethod(x) or inspect.isfunction(x))

        ns = Namespace(name=name, members=[], callables=[], parent=parent)

        members = [Namespace.from_callable(_type, name, parent=ns) for name, _type in _members if not name.startswith('_')]
        methods = [MCallable.from_callable(_type, name, parent=ns) for name, _type in _methods]

        ns.members = members
        ns.callables = methods

        return ns


def args_to_kwargs(args: List[str]) -> List[Tuple[str, Any]]:
    kwargs: List[Tuple[str, Optional[str]]] = []

    i = 0
    last_key = None
    last_value = None
    current_key = None
    while i < len(args):
        arg = args[i]
        if not arg.startswith('--') and current_key is None:
            if last_key and last_value:
                raise ConsecutiveValues(last_key, last_value, arg)
            raise UnexpectedValue(arg)

        with_equal = re.match(r'(?P<flag>--[a-z0-9-_]+)=(?P<value>.+)', arg)
        if with_equal:
            k = str(with_equal.group('flag'))
            v = str(with_equal.group('value'))
            k = k[2:]  # '--a' -> 'a'
            k = k.replace('-', '_')  # '--a-thing' -> 'a_thing'
            kwargs.append((k, v))
            last_key = k
            last_value = v
        elif arg.startswith('--'):
            k = arg
            k = k[2:]  # '--a' -> 'a'
            k = k.replace('-', '_')  # '--a-thing' -> 'a_thing'
            kwargs.append((k, None))  # This enables 'flags' with no value
            current_key = k
            last_key = k
        else:
            for idx, (_key, _) in reversed(list(enumerate(kwargs))):
                if _key == current_key:
                    kwargs[idx] = (_key, arg)
                    last_key = _key
                    last_value = arg
                    current_key = None
                    break
            assert current_key is None, "Somehow could not find what key to assign"
        i += 1
    return kwargs


def _parse(ns: Namespace, input_tokens: List[str]) -> Tuple[MCallable, Dict[str, Any]]:
    if len(input_tokens) == 0:
        raise BadArguments("Received no arguments")
    command, *args = input_tokens

    _members = {m.name: m for m in ns.members}
    if command in _members:
        return _parse(_members[command], args)

    _callables = {c.name: c for c in ns.callables}
    if command not in _callables:
        hierarchy: List[str] = []
        parent = ns.parent
        while parent:
            hierarchy.insert(0, parent.name)
            parent = parent.parent

        raise BadSubcommand(hierarchy + [ns.name], command, list(_callables))

    _callable = _callables[command]
    kwargs = args_to_kwargs(args)
    rcvd_params = {key for key, _ in kwargs}

    for a in _callable.args:
        origin = typing_get_origin(a.annotation)
        if a.annotation == Flag:
            if a.name not in rcvd_params:
                kwargs.append((a.name, Flag(False)))
                continue

            for idx, (k, _) in enumerate(kwargs):
                if k == a.name:
                    kwargs[idx] = (k, Flag(True))
        elif origin == Repeated:
            kwargs = _merge(kwargs, a.name)

    missing_values = [k for k, v in kwargs if v is None]
    if missing_values:
        raise MissingValues(list(sorted(missing_values)))

    all_params = {a.name for a in _callable.args}
    rcvd_params = {key for key, _ in kwargs}  # updated with flags
    needed_params = {a.name for a in _callable.args if a.default is inspect.Parameter.empty}

    missing_params = needed_params - rcvd_params
    extra_params = rcvd_params - all_params
    if missing_params:
        raise MissingParameters(list(sorted(missing_params)))
    elif extra_params:
        raise UnexpectedParameters(list(sorted(extra_params)))

    return _callable, dict(kwargs)

def _merge(kwargs: List[Tuple[str, Any]], key: str) -> List[Tuple[str, Any]]:
    """
    Merge key-value pairs which have a key matching `key`.

    >>> _merge([('a', 1), ('b', 2), ('a', 3)])
    [('b', 2), ('a', [1, 3])]
    """
    _buf = []
    _ret = []
    for k, v in kwargs:
        if k != key:
            _ret.append((k, v))
            continue
        _buf.append(v)

    if _buf:
        _ret.append((key, _buf))

    return _ret

def parse(ns: Namespace, input_command: str) -> Tuple[MCallable, Dict[str, Any]]:
    return _parse(ns, shlex.split(input_command))


def apply_args(c: MCallable, kwargs: Dict[str, Any]) -> Any:
    casted = {}
    args_by_name = {a.name: a for a in c.args}
    for k, v in kwargs.items():
        casted[k] = cast(v, args_by_name[k].annotation)

    return c.fn(**casted)

def cast(value: Any, annotation: Any) -> Any:
    origin = typing_get_origin(annotation)
    args = typing_get_args(annotation)
    if origin == Union:
        for arg in args:
            try:
                value = cast(value, arg)
                break
            except Exception:
                continue
    elif origin in [list, tuple, List, Tuple]:
        value = value.split(',')
        if len(args):
            value = [cast(i, args[0]) for i in value]
    elif origin == Repeated:
        value = [cast(i, args[0]) for i in value]
    elif annotation in [int, float]:
        value = annotation(value)
    elif annotation is bool:
        value = value.lower() in ['true', '1', 't', 'y', 'yes']
    elif issubclass(annotation, enum.Enum):
        value = annotation[value]
    return value

def execute_command(c: Callable[..., Any], input_command: str) -> Any:
    parsed, kwargs = parse(Namespace.from_callable(c), input_command)
    return apply_args(parsed, kwargs)
