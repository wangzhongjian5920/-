# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 21:47:05 2018

@author: Administrator
"""
import sys
import os
import re

#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ 
#******************************开始写代码******************************
def swap(values, a, b):
    temp = values[a]
    values[a] = values[b]
    values[b] = temp
    return values

def  minSwapTime(values):
    count = 0
    for i in range(len(values)//2 + 1)[::-1]:
        if 2 * i <= len(values) - 3:
            ##中左右
            if values[2 * i + 1] > values[i] and values[2 * i + 2] > values[2 * i + 1]:
                values = swap(values, i, 2 * i + 1)
                count += 1
            ##左右中
            elif values[2 * i + 1] < values[2 * i + 2] and values[2 * i + 2] < values[i]:
                values = swap(values, i, 2 * i + 2)
                count += 1
            ##左中右
            elif values[2 * i + 2] > values[i] and values[i] > values[2 * i + 1]:
                continue
            ##右中左
            elif values[2 * i + 2] < values[i] and values[2 * i + 1] > values[i]:
                values = swap(values, i, 2 * i + 1)
                count += 1
                values = swap(values, i, 2 * i + 2)
                count += 1
                values = swap(values, i, 2 * i + 1)
                count += 1
            ##右左中
            elif values[2 * i + 2] < values[2 * i + 1] and values[2 * i + 1] < values[i]:
                values = swap(values, 2 * i + 1, 2 * i + 2)
                count += 1
                values = swap(values, i, 2 * i + 2)
                count += 1
            ## 中右左
            elif values[i] < values[2 * i + 2] and values[2 * i + 2] < values[2 * i + 1]:
                values = swap(values, i, 2 * i + 2)
                count += 1
                values = swap(values, i, 2 * i + 1)
                count += 1
        elif 2 * i == len(values) - 2:
            if values[2 * i + 1] > values[i]:
                values = swap(values, i, 2 * i + 1)
                count += 1
    return count
            
            

#******************************结束写代码******************************


_values_cnt = 0
_values_cnt = int(input())
_values_i=0
_values = []
while _values_i < _values_cnt:
    _values_item = int(input())
    _values.append(_values_item)
    _values_i+=1

  
res = minSwapTime(_values)

print(str(res) + "\n")