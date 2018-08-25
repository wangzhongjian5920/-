# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 13:36:35 2018

@author: Administrator
"""

t = input().split()
times = int(t[0])
hours = int(t[1])
array = input().split()
new = [int(i) for i in array] * hours
length = [1 for _ in range(times*hours)]
max_length = 1
min_num = new[0]
for i in range(1, times*hours):
    if new[i] <= new[i + 1] and length[i] + 1 > length[j]:
            length[j] = length[i] + 1
print(max(length))