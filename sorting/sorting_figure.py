#!/usr/bin/env python
# -*- coding: utf-8 -*-

from plot_bar import create_data
from plot_animation import dynamic_sorting_figure

from bubble_sort.bubble_sort import bubble_sort_iter

def bubble_sort_figure():
    data = create_data(l=20, min_v=1, max_v=100)
    dynamic_sorting_figure(data, bubble_sort_iter)

if __name__ == '__main__':
    bubble_sort_figure()
