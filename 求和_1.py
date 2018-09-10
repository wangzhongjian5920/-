# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 16:42:06 2018

@author: Administrator
"""

lis_1, lis_2 = list(input().strip().split('.'))
re_1 = list(lis_1)
re_1.append('.')
re_2 = list(lis_2)

li = ""
for j in re_1:
    if j == " " or j not in re_2:
        li += j
print(li)