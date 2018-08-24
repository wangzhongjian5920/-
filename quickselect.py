# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 21:38:50 2018

@author: Administrator
"""

def one_quicksort(array, left, right):
    std = array[left]
    left_point = left
    right_point = right
    while(left_point < right_point):
        while(left_point < right_point and array[right_point] >= std):
            right_point -= 1
        if left_point < right_point:
            array[left_point] = array[right_point]
            left_point += 1
        while(right_point > left_point and array[left_point] < std):
            left_point += 1
        if left_point < right_point:
            array[right_point] = array[left_point]
            right_point -= 1
    array[left_point] = std
    return left_point, array

def quick_select_min_kth(array, k):
    index = k - 1 
    if index < 0:
        print("invalid")
        return
    m, array = one_quicksort(array, 0, len(array) - 1)
    if m == index:
        print("%d"%(array[m]))
    elif m < index:
        array = array[m+1:]
        quick_select_min_kth(array, index - m)
    else:
        array = array[:m]
        quick_select_min_kth(array, k)
        
array = [1,2,4,6,2,1,3]
quick_select_min_kth(array, 7)    