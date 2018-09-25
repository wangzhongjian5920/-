# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 17:31:10 2018

@author: Administrator
"""

lis = list(map(int, input().strip().split(' ')))
nums = list(set(lis))
target = (len(lis)+1)//2
n = len(lis)
for i in nums:
    if n < target:
        break
    t = lis.count(i)
    n -= t
    if t >= target:
        print(i)