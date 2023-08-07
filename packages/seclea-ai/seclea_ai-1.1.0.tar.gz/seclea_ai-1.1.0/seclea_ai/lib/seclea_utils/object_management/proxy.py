from __future__ import annotations

import inspect
import os
import re
from shutil import rmtree
from typing import TypeVar

from decorator import decorate
from wrapt.wrappers import ObjectProxy

from .factory import load_object_manager_from_class_name
from .factory import load_object_manager_from_obj
from .object_manager import ObjectManager
from .utils import ensure_path_exists

R = TypeVar("R")  # the variable return type

DEF = re.compile(r"\s*def\s*([_\w][_\w\d]*)\s*\(")
POS = inspect.Parameter.POSITIONAL_OR_KEYWORD
EMPTY = inspect.Parameter.empty


class Tracked(ObjectProxy):
    _object_manager: ObjectManager = None

    def __init__(self, wrapped, type_hint=None, cleanup: bool = True):
        # Initialise the object proxy and assign variables for object.
        super(Tracked, self).__init__(wrapped)
        self._cleanup = cleanup

    @property
    def object_manager(self) -> ObjectManager:
        if self._object_manager is None:
            try:
                om = load_object_manager_from_obj(self)
            except Exception as e:
                print(f"failed to load proxy: {e}")
                raise
            self._object_manager = om
        return self._object_manager

    @staticmethod
    def load_tracked(path, file_name, cleanup: bool = True) -> Tracked:
        """
        Load routine for tracked object
        @param path:
        @param file_name:
        @return:
        """
        # use generic object manager to load the file (fil compressed etc.
        generic_object_manager = ObjectManager(file_name=file_name, path=path)
        generic_object_manager.load_file()
        #  get the specific object manager for the saved object
        object_manager = load_object_manager_from_class_name(
            generic_object_manager.metadata.get(generic_object_manager.object_manager_key)
        )
        object_manager.metadata.update(generic_object_manager.metadata)
        object_manager.full_path = generic_object_manager.path, generic_object_manager.file_name
        # load the tracked object
        obj = object_manager.load_object()
        # wrap object, and assign previously loaded object_manager.
        tracked_obj = Tracked(obj, cleanup=cleanup)
        tracked_obj._object_manager = object_manager
        return tracked_obj

    def save_tracked(self, path=None) -> (str, str):
        """
        Save routine for tracked object, path: directory to save object to
        @return: save_path, file_name
        """
        ensure_path_exists(os.path.join(self.object_manager.full_path))
        self.object_manager.save_object(self)
        args = self.object_manager.save_file(path=path)
        # For now as the object is now saved to a zip, we remove the file created by the tracked object.
        return args

    def __del__(self):
        # for now clean up as file management is not consistent in use.
        if not self._cleanup:
            return
        try:
            rmtree(self.object_manager.full_path)
        except FileNotFoundError:
            pass

    def __call__(self, *args, **kwargs):
        # entry
        try:
            return self.__wrapped__(*args, **kwargs)
        finally:
            # exit
            pass

    def __reduce_ex__(self, protocol):
        return self.__wrapped__.__reduce_ex__(protocol)

    def __copy__(self):
        return self.__wrapped__.__copy__()

    def __deepcopy__(self, memo):
        return self.__wrapped__.__deepcopy__()

    def __reduce__(self):
        return self.__wrapped__.__reduce__()

    def __hash__(self):
        return self.object_manager.hash_object(self.__wrapped__)


def tracked_decorator(caller, _func=None, kwsyntax=False):
    """
    decorator(caller) converts a caller function into a decorator
    """
    if _func is not None:  # return a decorated function
        # this is obsolete behavior; you should use decorate instead
        return decorate(_func, caller, (), kwsyntax)
    # else return a decorator function
    sig = inspect.signature(caller)
    dec_params = [p for p in sig.parameters.values() if p.kind is POS]

    def dec(func=None, *args, **kw):
        na = len(args) + 1
        extras = args + tuple(
            kw.get(p.name, p.default) for p in dec_params[na:] if p.default is not EMPTY
        )
        if func is None:
            return lambda func: decorate(func, caller, extras, kwsyntax)
        else:
            return decorate(func, caller, extras, kwsyntax)

    dec.__signature__ = sig.replace(parameters=dec_params)
    dec.__name__ = caller.__name__
    dec.__doc__ = caller.__doc__
    dec.__wrapped__ = caller
    dec.__qualname__ = caller.__qualname__
    dec.__kwdefaults__ = getattr(caller, "__kwdefaults__", None)
    dec.__dict__.update(caller.__dict__)

    # TODO make this generic for multiple types of functions this is a hacky workarount.
    #  Assume all functions using this are generic dataset transformation functions as soon as we need specific types
    #  this needs taking out and refactoring
    @dec
    def ret(f, *args, **kwargs):
        # here we can upload dataset transformation
        return f(args, kwargs)

    return Tracked(ret)
