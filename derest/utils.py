import inspect
import six


def dict_from_args(func, *args):
    """
    Convert function arguments to a dictionary
    """
    result = {}
    args_names = []

    if six.PY2:
        args_names = inspect.getargspec(func)[0]
    else:
        args_names = list(inspect.signature(func).parameters.keys())

    for i in range(len(args)):
        result[args_names[i]] = args[i]

    return result


def merge_dicts(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result
