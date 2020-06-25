# -*- coding: utf-8 -*-

import numpy as np

from utils import zigzag

def test_zizag_1():
    a = np.array([[1, 4],[2, 5]])
    res = np.array([1, 4, 2, 5])
    assert np.all(zigzag(a) == res) == True

def test_zigzag_2():
    a = np.arange(9).reshape((3, 3))
    print(a)
    res = np.array([0, 1, 3, 6, 4, 2, 5, 7, 8])
    assert np.all(zigzag(a) == res) == True

def test_zigzag_3():
    a = np.arange(16).reshape((4, 4))
    print(a)
    res = np.array([0, 1, 4, 8, 5, 2, 3, 6, 9, 12, 13, 10, 7, 11, 14, 15])
    assert np.all(zigzag(a) == res) == True
