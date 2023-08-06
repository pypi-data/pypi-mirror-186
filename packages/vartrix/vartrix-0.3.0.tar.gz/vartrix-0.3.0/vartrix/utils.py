# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 11:36:50 2019

@author: Reuben

This module contains helper classes and functions. 

"""

import inspect, sys
import numpy as np


class Factory:
    """Instantiate module classes based on container key

    Args:
        name (str): The module name (often `__name__`)
        container (Container): The container instance
        dotkey (str): The dotkey of the class name.
        build_function (func): OPTIONAL: A function that takes the new
        instance object. If provided, the return value of the Factory is
        the return value of the function.
        class_method (str): OPTIONAL: The name of a class method called
        to instantiate the object.
        default (str): OPTIONAL: An optional default value if the dotkey
        is not present.

    Note:
        The class name pointed to by the dotkey must exist in the module,
        or a KeyError will be raised.
    """

    def __init__(
        self,
        name,
        container,
        dotkey,
        build_function=None,
        class_method=None,
        default=None,
    ):
        self.container = container
        self.name = name
        self.dotkey = dotkey
        self.build_function = build_function
        self._class_method = class_method
        self._default = default

    def new(self, *args, **kwargs):
        """Create a new instance based on the current dotkey value"""
        if self.dotkey in self.container:
            cls_name = self.container[self.dotkey]
        elif self._default is not None:
            cls_name = self._default
        else:
            raise KeyError("Class name not provided by dotkey or default.")
        clsmembers = inspect.getmembers(sys.modules[self.name], inspect.isclass)
        clsdct = {t[0]: t[1] for t in clsmembers}
        try:
            c = clsdct[cls_name]
        except KeyError:
            raise KeyError(
                "Class " + str(cls_name) + " not found in module " + str(self.name)
            )
        if self.build_function is not None:
            obj = c(*args, **kwargs)
            return self.build_function(obj)
        elif self._class_method is not None:
            method = getattr(c, self._class_method)
            return method(*args, **kwargs)
        else:
            return c(*args, **kwargs)


class Simple_Factory:
    def __init__(self, name, build_function=None, class_method=None):
        self.name = name
        self.build_function = build_function
        self._class_method = class_method

    def new(self, cls_name, *args, **kwargs):
        clsmembers = inspect.getmembers(sys.modules[self.name], inspect.isclass)
        clsdct = {t[0]: t[1] for t in clsmembers}
        try:
            c = clsdct[cls_name]
        except KeyError:
            raise KeyError(
                "Class " + str(cls_name) + " not found in module " + str(self.name)
            )
        if self.build_function is not None:
            obj = c(*args, **kwargs)
            return self.build_function(obj)
        elif self._class_method is not None:
            method = getattr(c, self._class_method)
            return method(*args, **kwargs)
        else:
            return c(*args, **kwargs)


class Attrdict(dict):
    def __new__(cls, *args, **kwargs):
        d = super(Attr_Dict, cls).__new__(cls, *args, **kwargs)
        d.__dict__ = d
        return d


def _nest(key_list, val, dct=None):
    dct = {} if dct is None else dct
    if len(key_list) == 1:
        dct[key_list[0]] = val
    else:
        if key_list[0] not in dct:
            dct[key_list[0]] = {}
        _nest(key_list[1:], val, dct[key_list[0]])
    return dct


def nested(dct):
    """Create a nested dictionary representation of a dotkey flat dictionary"""
    out_dct = {}
    for dotkey, val in dct.items():
        key_list = dotkey.split(".")
        _nest(key_list, val, out_dct)
    return out_dct


def flat(dct, base=""):
    """Create a flat dictionary representation of nested dictionary"""
    out_dct = {}
    for k, v in dct.items():
        dotkey = base + "." + k
        if isinstance(v, dict):
            out_dct[dotkey] = flat(v, base=dotkey)
        else:
            out_dct[dotkey] = v
    return out_dct


def numpify(obj):
    if isinstance(obj, list):
        return np.array(obj)
    if isinstance(obj, dict):
        return {k: numpify(v) for k, v in obj.items()}
    else:
        return obj


def denumpify(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, dict):
        return {k: denumpify(v) for k, v in obj.items()}
    else:
        return obj
