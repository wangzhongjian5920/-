# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 18:24:43 2018

@author: Administrator
"""
from math import sqrt

a = int(input())
count = 0
for i in range(-1 * int(sqrt(a)), int(sqrt(a)) + 1):
    if int(sqrt(a - i ** 2) ** 2) == a - i ** 2:
        count += 1
print(count)
