#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import pygorithm.sorting

def insertion_sort(l):
    it = insertion_sort_iter(l)
    while True:
        try:
            l = it.next()
        except StopIteration:
            return l

def insertion_sort_iter(l):
    length = len(l)
    if length <= 1:
        yield l

    for j in xrange(1, length):
        i = j-1
        temp = l[j]
        while (i >= 0 and temp < l[i]):
            l[i+1] = l[i]
            i -= 1
            yield l
        l[i+1] = temp
        yield l


class InsertionSortTestCase(unittest.TestCase):
    def setUp(self):
        self.raw_list = [6,5,4,3,2,1]

    def test_my(self):
        assert insertion_sort(self.raw_list) == [1,2,3,4,5,6]

    def test_lib(self):
        assert pygorithm.sorting.insertion_sort.sort(self.raw_list) == [1,2,3,4,5,6]



if __name__ == '__main__':
    unittest.main()

