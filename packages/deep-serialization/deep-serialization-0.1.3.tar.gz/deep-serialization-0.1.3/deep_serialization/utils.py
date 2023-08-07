from typing import NewType

PythonId = NewType('PythonId', str)


def check_comparability(py_object: object, deserialized_py_object: object) -> bool:
    return py_object == deserialized_py_object


def get_type(py_object: object) -> str:
    if py_object is None:
        return 'types.NoneType'
    module = type(py_object).__module__
    return '{module}.{name}'.format(
        module=module,
        name=type(py_object).__name__,
    )


def get_type_name(type_: object) -> str:
    if type_ is None:
        return 'types.NoneType'
    return '{module}.{name}'.format(
        module=type_.__module__,
        name=type_.__name__,
    )


def has_reduce(py_object: object) -> bool:
    if getattr(py_object, '__reduce__', None) is None:
        return False
    try:
        py_object.__reduce__()
        return True
    except TypeError:
        return False


def get_repr(py_object: object) -> str:
    if isinstance(py_object, type):
        return get_type_name(py_object)
    return repr(py_object)

