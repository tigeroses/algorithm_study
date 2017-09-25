#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import pygorithm.sorting
import random

def quick_sort(l):
    """
    it = quick_sort_iter(l, 0, len(l)-1)
    while True:
        try:
            it.next()
        except StopIteration:
            print l
            return l
    """
    # return quick_sort_pythonic(l)
    quick_sort_iter(l, 0, len(l)-1)

    # print l
    return l

def quick_sort_iter(l, start, end):
    if start >= end:
        return

    pivot = end
    i = start
    j = end

    while True:
        while l[i]<=l[pivot] and i < j:
            i += 1
        while l[j]>=l[pivot] and i < j:
            j -=1
        if i < j:
            l[i], l[j] = l[j], l[i]
        else:
            l[i], l[pivot] = l[pivot], l[i]
            break

    quick_sort_iter(l, start, i-1)
    quick_sort_iter(l, i+1, end)

def quick_sort_pythonic(l):
    length = len(l)
    if length <= 1:
        return l

    pivot = random.choice(l)
    left_part = [x for x in l if x < pivot]
    median = [x for x in l if x == pivot]
    right_part = [x for x in l if x > pivot]

    return quick_sort_pythonic(left_part) + median + quick_sort_pythonic(right_part)

    

class QuickSortTestCase(unittest.TestCase):
    def setUp(self):
        self.raw_list = [1,3,2,6,5]

    def test_my(self):
        assert quick_sort(self.raw_list) == [1,2,3,5,6]

    def test_lib(self):
        assert pygorithm.sorting.quick_sort.sort(self.raw_list) == [1,2,3,5,6]



if __name__ == '__main__':
    unittest.main()

