# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 22:12:43 2019

@author: Reuben
"""

import os
import pandas as pd

from . import settings
from .aliases import Aliases
from . import persist

root = os.path.dirname(os.path.abspath(__file__))


def set_root(new):
    """This shouldn't be done"""
    global root
    root = new


def safe_call(method_name, obj, *args, **kwargs):
    try:
        method = getattr(obj, method_name)
        method(*args, **kwargs)
    except AttributeError:
        pass


class Vector:
    """Subclass for different entry formats"""

    def __init__(self, name, data=None):
        self.name = name
        self.i = 0
        self.child = None
        if data is not None:
            self.initialise(data)

    def initialise(self, data):
        self.labels, self.data = self.setup(data)
        self.n = len(self.labels)

    def setup(self, data):
        raise NotImplementedError

    def values(self, typ="values"):
        if typ == "values":
            return self.data
        elif typ == "labels":
            return [{self.name: label} for label in self.labels]
        else:
            raise KeyError("Key must be 'keys' or 'labels'.")

    def get_label_lst(self):
        return self.values(typ="labels")


class Value_Lists(Vector):
    def transpose_dict(self, dct):
        n = len(list(dct.values())[0])
        out = [{} for i in range(n)]
        for i in range(n):
            for k, v in dct.items():
                out[i][k] = v[i]
        return out

    def setup(self, data):
        def default_labels(d):
            for v in dct.values():
                if len(d) == 1:
                    return v
                else:
                    n = len(v)
                    return [i for i in range(n)]

        dct = data.copy()
        labels = dct.pop("labels", default_labels(dct))
        return labels, self.transpose_dict(dct)


class Value_Dictionaries(Vector):
    def setup(self, data):
        labels = []
        d = []
        for k, dct in data.items():
            labels.append(k)
            d.append(dct)
        return labels, d


class Constant(Vector):
    def setup(self, data):
        if len(data) == 1:
            k, v = data.copy().popitem()
            labels = [v]
        else:
            labels = [True]
        d = [data.copy()]
        return labels, d


class Csv_File(Vector):
    def setup(self, data):
        d = []
        full_filename = os.path.join(root, data["filename"])
        try:
            df = pd.read_csv(full_filename, index_col=0)
        except FileNotFoundError:
            raise FileNotFoundError(
                "File '" + full_filename + "' does not "
                "exist. To set the root directory, use "
                + "vt.automate.set_root(path)"
            )
        labels = list(df.index)
        for index, row in df.iterrows():
            d.append(row.to_dict())
        return labels, d


class Vectors:
    def __init__(self):
        self._styles = {
            "value_lists": Value_Lists,
            "value_dictionaries": Value_Dictionaries,
            "csv": Csv_File,
            "constant": Constant,
        }
        self._vectors = {}

    def __getitem__(self, key):
        return self._vectors[key]

    def get_vector(self, key):
        return self._vectors[key]

    def set_vector(self, key, vector):
        self._vectors[key] = vector

    def set_style(self, key, style):
        self._styles[key] = style

    def clear(self):
        self._vectors.clear()

    def _get_style(self, data):
        objs = []
        if "style" in data:
            return self._styles[data["style"]]
        if isinstance(data, dict):
            for k, v in data.items():
                if k != "labels":
                    objs.append(v)
            if all([isinstance(v, list) for v in objs]):
                return Value_Lists
            elif all([isinstance(v, dict) for v in objs]):
                return Value_Dictionaries
            elif len(data) == 1:
                return Constant
            else:
                return Constant

    def build_one(self, data, name):
        vec_cls = self._get_style(data)
        v = vec_cls(name)
        d = data.copy()
        try:
            d.pop("style")
        except KeyError:
            pass
        v.initialise(d)
        return v

    def build(self, data):
        self.clear()
        for vector_name, vec_data in data.items():
            vector = self.build_one(vec_data, vector_name)
            self.set_vector(vector_name, vector)


class Method:
    def __init__(self, name, vectors=None):
        self._name = name
        self.set_vectors(vectors)

    @property
    def name(self):
        return self._name

    def set_vectors(self, vectors):
        vectors = [] if vectors is None else vectors
        self._vectors = vectors

    def add(self, vector):
        self._vectors.append(vector)

    def build(self, data, vectors):
        if not isinstance(data, list):
            print("===")
            print(self._name)
            print(data)
            raise TypeError("data must be a list of vector names")
        for vector_name in data:
            self.add(vectors[vector_name])

    def get_lst(self, vectors=None, typ="values"):
        vectors = self._vectors if vectors is None else vectors
        if len(vectors) > 1:
            lst = self.get_lst(vectors=vectors[1:], typ=typ)
        else:
            lst = [{}]
        vector = vectors[0]
        out_lst = []
        for value in vector.values(typ=typ):
            for d in lst:
                dct = value.copy()
                dct.update(d)
                out_lst.append(dct)
        return out_lst

    def execute(self, container, obj, aliases=None, info=None):
        info = {} if info is None else info
        info["method"] = self._name
        safe_call("prepare_method", obj, self._name)
        method = getattr(obj, self._name)
        val_list = self.get_lst(typ="values")
        label_lst = self.get_lst(typ="labels")
        n = len(val_list)
        if aliases is not None:
            val_list = [aliases.translate(d) for d in val_list]
        with container.context(val_list[0]):
            i = 0
            for val_dct, label_dct in zip(val_list, label_lst):
                i += 1
                container.dset(val_dct)
                if settings.PRINT_UPDATES:
                    self.show(info, label_dct, i / n)
                method(info["sequence"], val_dct, label_dct)
        safe_call("finish_method", obj, self._name)

    def show(self, info, label_dct, complete=None):
        if complete is not None:
            s = "{:0.2f}% ".format(complete * 100)
        else:
            s = ""
        print(
            s
            + 'Executing "'
            + info.get("method", "unnamed")
            + '" method in "'
            + info.get("sequence", "unnamed")
            + '" sequence in "'
            + info.get("set", "unnamed")
            + '" set with:'
        )
        for vec_name, item_name in label_dct.items():
            print("   " + (vec_name + ": ").ljust(25) + str(item_name))


class Sequence:
    def __init__(self, name, methods=None):
        self._name = name
        self.set_methods(methods)

    @property
    def name(self):
        return self._name

    def __getitem__(self, key):
        return self.methods[key]

    @property
    def methods(self):
        return {m.name: m for m in self._methods}

    def set_methods(self, methods=None):
        methods = [] if methods is None else methods
        self._methods = methods

    def add(self, method):
        self._methods.append(method)

    def build(self, data, vectors):
        if not isinstance(data, dict):
            raise TypeError(
                "data must be a dictionary of method "
                + "name - [vector names] pairs"
            )
        for method_name, meth_data in data.items():
            method = Method(name=method_name)
            method.build(meth_data, vectors)
            self.add(method)

    def execute(self, container, obj, aliases=None, info=None):
        info = {} if info is None else info
        info["sequence"] = self._name
        safe_call("prepare_sequence", obj, self._name)
        for method in self._methods:
            method.execute(container, obj, aliases, info=info)
        safe_call("finish_sequence", obj, self._name)


class Automation_Set:
    def __init__(self, name, sequences=None):
        self._name = name
        self.set_sequences(sequences)

    def set_sequences(self, sequences):
        sequences = [] if sequences is None else sequences
        self._sequences = sequences

    def __getitem__(self, key):
        return self.sequences[key]

    @property
    def sequences(self):
        return {s.name: s for s in self._sequences}

    def add(self, sequence):
        self._sequences.append(sequence)

    def clear(self):
        self._sequences.clear()

    def build(self, data):
        if not isinstance(data, dict):
            raise TypeError("data must be a dictionary")
        vector_data = {}
        if "constants" in data:
            vector_data.update(data["constants"])
        if "vectors" in data:
            vector_data.update(data["vectors"])
        vectors = Vectors()
        vectors.build(vector_data)
        for sequence_name, seq_data in data["sequences"].items():
            s = Sequence(name=sequence_name)
            s.build(seq_data, vectors)
            self.add(s)

    @property
    def sequence_names(self):
        return list([s.name for s in self.sequences])

    def all_sequences(self):
        out = {}
        for seq_name in self.sequence_names:
            seq_dct = self.sequence(seq_name)
            out[seq_name] = seq_dct
        return out

    def run(self, container, obj, seq_name=None, aliases=None):
        """Run an automation set

        Args:
            set_name (str): The name of the set to run
            obj (object): The automated class instance.
            seq_name (str): [Optional] A specific sequence within the set
                to run exclusively.
        """
        safe_call("prepare", obj)
        for sequence in self._sequences:
            if seq_name is not None:
                if sequence.name is not seq_name:
                    continue
            sequence.execute(
                container, obj, aliases=aliases, info={"set": self._name}
            )
        safe_call("finish", obj)


class Automator:
    def __init__(self, container, fname=None, data=None, aliases=None):
        self._sets = {}
        self.set_aliases(aliases)
        self.container = container
        if data is not None:
            self.build(data)
        elif fname is not None:
            data = persist.load(fname)
            self.build(data)

    def set_automation_set(self, set_name, automation_set):
        self._sets[set_name] = automation_set

    def set_aliases(self, aliases):
        aliases = {} if aliases is None else aliases
        self._aliases = aliases

    def build(self, data):
        d = data.copy()
        try:
            alias_data = d.pop("aliases")
        except KeyError:
            alias_data = self._aliases
        aliases = Aliases(alias_data)
        self.set_aliases(aliases)
        for set_name, set_data in d.items():
            automation_set = Automation_Set(name=set_name)
            automation_set.build(set_data)
            self.set_automation_set(set_name, automation_set)

    def run(self, set_name, obj, seq_name=None):
        automation_set = self._sets[set_name]
        automation_set.run(
            container=self.container,
            obj=obj,
            seq_name=seq_name,
            aliases=self._aliases,
        )
