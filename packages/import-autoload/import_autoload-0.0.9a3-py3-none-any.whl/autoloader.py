####
##
#   autoloader
#

__version__ = "0.0.9-alpha"

import os, sys, importlib, importlib.util
from fnmatch import fnmatch
from pprint import pprint

# from pathlib import Path

# почему не __main__ != "__main__" ?
if not hasattr(sys.modules["__main__"], "__file__"):
    raise RuntimeWarning("`autoload` not works by direct call or interactive mode")

modules = sys.modules
ROOT = os.path.dirname(sys.modules["__main__"].__file__)
PATTERN = "*.py"


def autoload(module_name=None, pattern=None):
    _all_ = set()

    if "__name__" in sys._getframe(1).f_locals:
        #   вызов из модуля
        _current_ = sys._getframe(1).f_locals["__name__"]
    else:
        _current_ = ROOT

    #   нельзя просто так узнать количество аргументов функции
    if module_name is None and pattern is None:
        pattern = PATTERN
        module_name = _current_

    elif module_name is not None and pattern is None:
        pattern = module_name + PATTERN
        module_name = _current_

    elif module_name is None and pattern is not None:
        pattern = pattern + ("" if ".py" == pattern[-3::] else PATTERN)
        module_name = _current_

    elif module_name is not None and pattern is not None:
        pattern = pattern + ("" if ".py" == pattern[-3::] else PATTERN)

    else:
        pass

    spec = importlib.util.find_spec(module_name)
    path = spec.submodule_search_locations[0]

    # (root, dirs, files) = list(os.walk(os.path.dirname(_file_)))[0]
    (root, dirs, files) = list(os.walk(path))[0]

    for fn in files:
        if not fnmatch(fn, "__init__.py") and fnmatch(fn, pattern):
            _subname_ = os.path.splitext(fn)[0]

            # print("file:>>>", fn)
            # print('import', module_name, _subname_)

            # importlib.import_module(
            #    _name_ + "." + _subname_ if _name_ != "__main__" else _subname_
            # )
            _mod_ = importlib.import_module(module_name + "." + _subname_)
            # _mod_ = importlib.import_module(module_name, _subname_)
            # print(_mod_)

            # importlib.__import__(module_name, globals(), locals(), [_subname_], 0)
            """different scopes (module's visibility)"""

            _all_.add(_subname_)

    return tuple(_all_)


__all__ = ("autoload", "modules", "PATTERN", "ROOT")
