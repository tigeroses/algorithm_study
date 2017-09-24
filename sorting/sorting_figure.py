#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plot_bar import create_data
from plot_animation import dynamic_sorting_figure

from bubble_sort.bubble_sort import bubble_sort_iter
from insertion_sort.insertion_sort import insertion_sort_iter

def bubble_sort_figure(data):
    dynamic_sorting_figure(data, bubble_sort_iter(data))

def insertion_sort_figure(data):
    dynamic_sorting_figure(data, insertion_sort_iter(data))

if __name__ == '__main__':
    data = create_data(l=20, min_v=1, max_v=100)
    print data
    # 1 bubble sort
    # bubble_sort_figure(data)

    # 2 insertion sort
    insertion_sort_figure(data)
