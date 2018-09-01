# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 16:26:05 2018

@author: Administrator
"""
m = int(input())
array = input().split( )
if len(array) == m:
    for i in range(m):
        array[i] = int(array[i])
n, inter = input().split( )
n = int(n)
inter = int(inter)

dp_max = [[0 for _ in range(len(array))] for _ in range (n + 1)]
dp_min = [[0 for _ in range(len(array))] for _ in range (n + 1)]
for i in range(len(array)):
    dp_max[1][i] = array[i]
    dp_min[1][i] = array[i]

for p in range(len(array)):
    for k in range(1, n + 1):
        for ar in range(1, inter + 1):
            if p - ar >= 0:
                dp_max[k][p] = max(dp_max[k][p], max(dp_max[k - 1][p - ar] * array[p], dp_min[k-1][p - ar] * array[p]))
                dp_min[k][p] = min(dp_min[k][p], min(dp_max[k - 1][p - ar] * array[p], dp_min[k-1][p - ar] * array[p]))
            else:
                break

max_value = 0            
for i in dp_max:
    max_value = max(max_value, max(i))
print(max_value)