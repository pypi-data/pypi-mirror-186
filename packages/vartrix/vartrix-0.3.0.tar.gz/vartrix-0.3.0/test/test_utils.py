# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 20:39:58 2019

@author: Reuben
"""

import unittest

from vartrix import utils


class Test_Utils(unittest.TestCase):
    def test_nest(self):
        ret = utils._nest(["a", "b", "c", "d"], 5)
        expected = {"a": {"b": {"c": {"d": 5}}}}
        self.assertDictEqual(ret, expected)

    def test_nested(self):
        dct = {"a.b": 5, "b.c": 7}
        ret = utils.nested(dct)
        expected = {"a": {"b": 5}, "b": {"c": 7}}
        self.assertDictEqual(ret, expected)
