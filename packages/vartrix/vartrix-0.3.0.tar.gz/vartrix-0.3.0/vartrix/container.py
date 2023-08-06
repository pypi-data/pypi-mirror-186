# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:52:22 2019

@author: Reuben

This module includes the Container class upon which all of vartrix is built.

The idea of a container is to contain all of the key-value pairs for some
set of variables or parameters. Keys have an implied heirarchy using a
dot-format. For example, 'A.b' means that 'b' is a subkey of 'A'. All keys
are stored in a simple flat dictionary format, but some extra methods
allow the heirarchy to be used to simplify usage.

"""

from contextlib import contextmanager

from . import utils


class Container(dict):
    """A dictionary-like class that updates observers

    Args:
        dct (dict): A dictionary (possibly nested) of key-value pairs to use.

    Note:
        A `dotkey` is a dictionary key in the Container. It's called a dotkey
        simply because it's designed to have dots in it to represent a
        heirarchy.
    """

    def __init__(self, dct=None):
        self._backup = {}
        self._locks = set()
        if dct is not None:
            self.load(dct)

    def set(self, key, val, safe=False):
        """Set the value of a key

        Args:
            key (str): The key value
            val: The value to set. It can be a numpy array.
            safe (bool): Optional boolean. If true, the dotkey must already
            exist in the Container instance.
        """
        if safe:
            if key not in self:
                raise KeyError(
                    "In safe mode, key '" + key + "' must be present."
                )
            if key in self._locks:
                raise ValueError(
                    "Key '" + key + "' was locked while setting "
                    "in safe mode."
                )
        v = utils.denumpify(val)
        self[key] = v  # Set the value

    def dset(self, dct, safe=False, update_backup=False):
        """Set multiple values specified in a dictionary

        Args:
            dct (dict): The dictionary of key-value pairs.
            safe (bool): Optional boolean. If true, the key must already
                exist in the Container instance.
            update_backup (bool): If true, update the internal backup values
                that reset() restores.
        """
        for key, val in dct.items():
            try:
                self.set(key, val, safe=safe)
            except KeyError as e:
                if not safe:
                    raise e
                else:
                    unmatched = [k for k in dct.keys() if k not in self]
                    raise KeyError(
                        "Only values for existing keys are allowed. "
                        + "The following keys are not valid: "
                        + ", ".join(unmatched)
                    )
        if update_backup:
            self._backup.update(dct)

    def lock(self, key):
        self._locks.add(key)

    def unlock(self, key):
        self._locks.remove(key)

    def load(self, dct):
        """Set the container data using a dictionary"""
        self.clear()
        self._backup.clear()
        self._locks.clear()
        self.add(dct)

    def reset(self):
        self.load(self._backup.copy())

    def add(self, dct):
        """Add another set of data to the container"""
        self.update(dct)
        self._backup.update(dct)

    @classmethod
    def merge(cls, containers):
        """Combine a list of containers"""
        c = cls()
        for container in containers:
            c.update(container)
        return c

    @contextmanager
    def context(self, dct, safe=True):
        """A context manager for temporary changes in values

        Args:
            dct (dict): A dictionary of dotkey-value pairs.
            safe (bool): [Optional] set to false to ignore locks. Keys
                must already exist in the container.

        """
        try:
            originals = {k: self[k] for k in dct.keys()}
        except KeyError:
            for k in dct.keys():
                if k not in self:
                    raise KeyError(
                        "Key '"
                        + k
                        + "' was missing. "
                        + "Keys must already exist to use context."
                    )
        self.dset(dct, safe=safe)
        yield self
        self.dset(originals, safe=safe)

    def copy(self):
        new = Container(dct=self)
        new._backup = self._backup.copy()
        new._locks = self._locks.copy()
        return new

    def to_dict(self):
        return dict(self)
