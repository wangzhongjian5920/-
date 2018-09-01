# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 17:11:02 2018

@author: Administrator
"""

from functools import reduce
from itertools import combinations

a = int(input().strip())
b = input().strip().split( )
if len(b) == a:
    for i in range(a):
        b[i] = int(b[i])
b.sort()
count = 0
for num in range(2, a + 1):
    se = set(combinations(b, num))
    for cor in se:
        if cor[0] == 1:
            if sum(cor) > reduce(lambda x, y: x * y, cor):
                count += 1
print(count)
            