# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:14:59 2019

@author: Reuben
"""

from .container import Container


class Name_Space(dict):
    def __init__(self, obj_cls=Container):
        self.i = 0
        self.obj_cls = obj_cls
        self._active_container = None

    def __missing__(self, key):
        return self.create(key)

    def create(self, key, dct=None):
        new = self.obj_cls(dct=dct)
        self[key] = new
        return new

    def get(self, key=None, dct=None):
        if key is None:
            key = self.i
            self.i += 1
        if key not in self:
            return self.create(key, dct)
        return self[key]

    def set_active(self, key):
        if key in self or key is None:
            self._active_container = key
        else:
            raise KeyError(key + " not found in name space.")

    def active_container(self):
        return self[self._active_container]

    def duplicate(self, key, new_key):
        self[new_key] = self[key].copy()
        return self[new_key]


default = Name_Space()


def get_container(name=None):
    return default.get(name)
