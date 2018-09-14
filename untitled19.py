# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 21:21:23 2018

@author: Administrator
"""
num = int(input())
lis = list(map(int, input().strip().split( )))
count_1 = 0
count_2 = 0
for i in range(len(lis)):
    for j in range(i + 1, len(lis)):
        if lis[i] > lis[j]:
            count_1 += 1
        else:
            count_2 += 1
print(min(count_1, count_2))
