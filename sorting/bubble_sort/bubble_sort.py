#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import pygorithm.sorting

def bubble_sort(l):
    while True:
        try:
            l = bubble_sort_iter(l).next()
        except StopIteration:
            return l

def bubble_sort_iter(l):
    length = len(l)
    if length <= 1:
        yield l

    for i in xrange(length):
        for j in xrange(i+1, length):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
                yield l

class BubbleSortTestCase(unittest.TestCase):
    def setUp(self):
        self.raw_list = [1,3,2,6,5]

    def test_my(self):
        assert bubble_sort(self.raw_list) == [1,2,3,5,6]

    def test_lib(self):
        assert pygorithm.sorting.bubble_sort.sort(self.raw_list) == [1,2,3,5,6]



if __name__ == '__main__':
    unittest.main()

