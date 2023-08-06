# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:31:41 2019

@author: Reuben
"""


import unittest

from vartrix.container import Container


def get_c():
    c = Container()
    c.set("a.b", 5)
    c.set("b.c", 7)
    return c


def get_c2():
    d = {
        "a.b": 1,
        "a.c": 2,
        "d.e": 3,
        "d.f": 4,
        "d.g.h": 5,
        "d.g.i": 6,
    }
    c = Container(d)
    return c


class Test_Container(unittest.TestCase):
    def test_instantiate(self):
        c = Container()
        self.assertTrue(isinstance(c, dict))

    def test_load_on_init(self):
        dct = {"a.b": 6}
        c = Container(dct)
        self.assertDictEqual(dct, c)

    def test_dict_set_item(self):
        c = Container()
        c["a"] = 6

    def test_dict_get_item(self):
        c = Container()
        c["a"] = 6
        self.assertEqual(c["a"], 6)

    def test_set(self):
        c = Container()
        c.set("a.b", 6)
        self.assertEqual(c["a.b"], 6)

    def test_get(self):
        c = Container()
        c.set("a.b", 6)
        self.assertEqual(c.get("a.b"), 6)

    def test_dset(self):
        c = Container()
        dct = {"a.b": 6}
        c.dset(dct)
        self.assertDictEqual(c, dct)

    def test_load(self):
        c = Container()
        dct = {"a.b": 6}
        c.load(dct)
        self.assertDictEqual(dct, c)

    def test_merge(self):
        d1 = {"a.b": 5}
        d2 = {"c.d": 7}
        c1 = Container(d1)
        c2 = Container(d2)
        c = Container.merge([c1, c2])
        expected = {"a.b": 5, "c.d": 7}
        self.assertEqual(c, expected)

    def test_context(self):
        dct = {"a.b": 6, "a.c": 7}
        c = Container(dct)
        new1 = {"a.b": 66}
        new2 = {"a.c": 77}
        with c.context(new1):
            expected1 = {"a.b": 66, "a.c": 7}
            self.assertDictEqual(c, expected1)
            with c.context(new2):
                expected2 = {"a.b": 66, "a.c": 77}
                self.assertDictEqual(c, expected2)
            self.assertDictEqual(c, expected1)
        self.assertDictEqual(dct, c)

    def test_reset(self):
        c = get_c2()
        c.set("z.c", 7)
        c.set("d.f", 234)
        c.reset()
        dct = {"a.b": 1, "a.c": 2, "d.e": 3, "d.f": 4, "d.g.h": 5, "d.g.i": 6}
        self.assertDictEqual(dct, c)
