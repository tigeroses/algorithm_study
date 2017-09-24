#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

import random
import time

def plot_bar(array,title="sorting",xlabel="pos",ylabel="value"):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    #ax.hist(array)
    #plt.bar(array[0], array[1])
    plt.bar(array[0], array[1])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    #plt.ion()

def create_data(l=50, min_v=1, max_v=999):
    lst = []
    for i in xrange(l):
        lst.append(random.randint(min_v, max_v))
    return lst

if __name__ == '__main__':
    lst = create_data(l=20, min_v=1,max_v=100)
    array = [range(1,len(lst)+1),lst]

    plot_bar(array)
