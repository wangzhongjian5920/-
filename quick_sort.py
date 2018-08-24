# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 20:27:13 2018

@author: Administrator
"""

def quicksort(array, left, right):
    if left < right:
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
        quicksort(array, left, left_point - 1)
        quicksort(array, right_point + 1, right)
    return array
        
array = [1,2,4,6,2,1,3]
print(quicksort(array, 0, len(array) - 1))
        
        