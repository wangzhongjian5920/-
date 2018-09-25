# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 20:06:42 2018

@author: Administrator
"""

n = int(input())
dp_2 = [0 for _ in range(n + 1)]
dp_5 = [0 for _ in range(n + 1)]
for index in range(1, n + 1):
    i = index
    c2 = 0
    c5 = 0
    while i%2 == 0:
        i //=2
        c2 += 1
    while i%5 == 0:
        i //=5
        c5 += 1
    dp_2[index] = c2
    dp_5[index] = c5
print(min(sum(dp_2), sum(dp_5)))