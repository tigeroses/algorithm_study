#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import pygorithm.sorting

def shell_sort(l):
    it = shell_sort_iter(l)
    while True:
        try:
            l = it.next()
        except StopIteration:
            return l

def shell_sort_iter(l):
    length = len(l)
    if length <= 1:
        yield l

    gap = length / 2
    while gap > 0:
        for j in xrange(gap, length):
            i = j-gap
            temp = l[j]
            while (i >= 0 and temp < l[i]):
                l[i+gap] = l[i]
                i -= gap
                yield l
            l[i+gap] = temp
            yield l
        gap = gap / 2


class ShellSortTestCase(unittest.TestCase):
    def setUp(self):
        self.raw_list = [6,5,4,3,2,1]

    def test_my(self):
        assert shell_sort(self.raw_list) == [1,2,3,4,5,6]

    def test_lib(self):
        assert pygorithm.sorting.shell_sort.sort(self.raw_list) == [1,2,3,4,5,6]



if __name__ == '__main__':
    unittest.main()

