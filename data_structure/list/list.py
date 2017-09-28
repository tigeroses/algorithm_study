#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import random

class Node(object):
    def __init__(self, v):
        self.v = v
        self.p = None

class List(object):
    def __init__(self):
        self.size = 0
        self.head = Node(None)

    def __str__(self):
        node = self.head
        l = []
        while node.p is not None:
            l.append(node.p.v)
            node = node.p
        return ' '.join(map(str,l))

    # insert element before index
    # l = [1,2,3]
    # normal index   l.insert(0, 0) -> l = [0,1,2,3]
    # negative index l.insert(-1, 4) -> l = [0,1,2,4,3]
    # overflow index l.insert(100,5) -> l = [0,1,2,4,3,5]
    def insert(self, index, v):
        if self.size == 0 or index >= self.size:
            self.append(v)
        else:
            node = self.head
            new_node = Node(v)
            # make sure the index is positive
            if index < 0:
                index = self.size + index
            if index < 0:
                index = 0

            idx = 0
            while node.p is not None:
                if index == idx:
                    new_node.p = node.p
                    node.p = new_node
                    self.size += 1
                    break
                idx += 1
                node = node.p

    # insert element in the tail of list
    def append(self, v):
        node = self.head
        while node.p is not None:
            node = node.p

        new_node = Node(v)
        node.p = new_node
        self.size += 1

    # calc the occurrences of number
    def count(self, v):
        node = self.head
        count = 0
        while node.p is not None:
            if node.v == v:
                count += 1
            node = node.p

        return count

    # append a list
    def extend(self, lst):
        node = lst.head
        while node.p is not None:
            self.append(node.p.v)
            node = node.p

    # return the index of element
    # if not exists, raise a exception
    def index(self, v, start=0, end=-1):
        node = self.head
        idx = 0
        if end < 0:
            end = self.size+end
        while node.p is not None:
            if idx >= start and idx <= end:
                if node.p.v == v:
                    break
            idx += 1
            node = node.p

        if idx == self.size:
            raise ValueError("%s is not in list" % v)
        return idx

    # remove and return the item at index(default last)
    # raise IndexError if list is empty or index is out of range
    def pop(self, index=-1):
        if index < 0:
            index = self.size + index
        if index >= self.size or index < 0:
            raise IndexError("pop index out of range")

        node = self.head
        idx = 0
        pop_v = None
        while node.p is not None:
            if idx == index:
                pop_v = node.p.v
                node.p = node.p.p
                self.size -= 1
                break
            idx += 1
            node = node.p

        return pop_v

    # remove first occurrence of value
    # raise ValueError if the value is not present
    def remove(self, v):
        node = self.head
        is_exists = False
        while node.p is not None:
            if node.p.v == v:
                node.p = node.p.p
                self.size -= 1
                is_exists = True
                break
            node = node.p

        if not is_exists:
            raise ValueError("%s not in list" % v)
    
    # reverse "In place"
    def reverse(self):
        if self.size <= 1:
            return

        head = self.head
        current = head.p
        while current.p is not None:
            pnext = current.p
            # A.p = B.p means A point to B.p
            current.p = pnext.p
            pnext.p = head.p
            head.p = pnext


class ListTestCase(unittest.TestCase):
    
    @unittest.skip('append')
    def test_append(self):
        lst = List()
        lst.append(1)
        lst.append(2)
        lst.append(3)
        print lst

    @unittest.skip('insert')
    def test_insert_element(self):
        lst = List()
        lst.insert(0, 5)
        lst.insert(0, 7)
        lst.insert(0, 8)
        lst.insert(1, 1)
        lst.insert(-1, 20)
        lst.insert(-100, 0)
        lst.insert(100, 100)
        print lst

    @unittest.skip('count')
    def test_count(self):
        lst = List()
        for i in xrange(20):
            lst.append(random.randint(0,10))

        print 'lst is:',lst
        print 'how many 3:', lst.count(3)

    @unittest.skip('extend')
    def test_extend(self):
        lst1 = List()
        for i in xrange(10):
            lst1.append(random.randint(0,10))
        lst2 = List()
        for i in xrange(10):
            lst2.append(random.randint(0,10))

        print 'lst1:',lst1
        print 'lst2:',lst2
        lst1.extend(lst2)
        print 'after extend lst1:',lst1

    @unittest.skip('index')
    def test_index(self):
        lst = List()
        for i in xrange(10):
            lst.append(random.randint(0,10))
        print 'lst:',lst
        print 'index of 3:'
        print lst.index(3)
        print 'index of 3, range(3,7):'
        print lst.index(3, 3, 7)
        print 'index of 11:'
        print lst.index(11)

    @unittest.skip('pop')
    def test_pop(self):
        lst = List()
        lst.append(1)
        lst.append(2)
        lst.append(3)
        print 'before pop:', lst
        print 'pop,', lst.pop(0)
        print 'after pop:', lst
        
        lst = List()
        lst.append(1)
        lst.append(2)
        lst.append(3)
        print 'before pop:', lst
        print 'pop,', lst.pop()
        print 'after pop:', lst

        print 'pop,', lst.pop()
        print 'after pop:', lst

        print 'pop,', lst.pop()
        print 'after pop:', lst

        print 'pop,', lst.pop()
        print 'after pop:', lst

    @unittest.skip('remove')
    def test_remove(self):
        lst = List()
        lst.append(1)
        lst.append(2)
        lst.append(3)

        print 'before remove:', lst
        print 'remove 3,'
        lst.remove(3)
        print 'after remove:', lst

        print 'remove 1,'
        lst.remove(1)
        print 'after remove:', lst
        
        print 'remove 11,'
        lst.remove(11)
        print 'after remove:', lst

    def test_reverse(self):
        lst = List()
        lst.append(1)
        lst.append(2)
        lst.append(3)
    
        print 'before reverse:', lst
        lst.reverse()
        print 'after reverse:', lst


if __name__ == '__main__':
    unittest.main()




