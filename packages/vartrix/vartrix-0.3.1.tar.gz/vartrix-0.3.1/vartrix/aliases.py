# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 20:38:43 2022

@author: Reuben
"""


import pandas as pd


def check_csv(fname, key="key", alias="alias"):
    df = pd.read_csv(fname, usecols=[key, alias])
    inds = df.duplicated(subset=["alias"])
    if any(inds):
        df2 = df.loc[inds]
        raise KeyError("Duplate aliases: ", df2["alias"])


def canonical(aliases):
    """Return an Aliases with only last keys for duplicate values"""
    uniques_inv = {v: k for k, v in aliases.items()}
    uniques = {v: k for k, v in uniques_inv.items()}
    return Aliases(uniques)


class Aliases(dict):
    def translate(self, dct):
        out = {}
        for k, v in dct.items():
            if k in self:
                out[self[k]] = v
            else:
                out[k] = v
        return out

    def copy(self):
        return Aliases(self)

    def add_csv(self, fname, key="key", alias="alias", **kwargs):
        df = pd.read_csv(fname, usecols=[key, alias])
        dct = {r[alias]: r[key] for i, r in df.iterrows()}
        self.update(dct)

    def __missing__(self, key):
        return key
