# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 19:45:07 2018

@author: Administrator
"""

a, b = list(map(int, input().strip().split()))
n = (-7 * b)//(a-b)

if n >= 3:
    value = n * a + (7 - n) * b
    print(2 * value + 3 * a)
else:
    value = n * a + (7 - n) * b
    print(2 * value + n * a + (3 - n) * b)

