# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 18:38:36 2018

@author: Administrator
"""
def compare(string_1,string_2):
    flag = 0
    for i in range(len(string_1)):
        if string_1[i] < string_2[i]:
            flag = -1
            break
        elif string_1[i] > string_2[i]:
            flag = 1
            break
    return flag

lis_1, lis_2 = list(input().strip().split( ))
lis_1 = lis_1.split('.')
lis_2 = lis_2.split('.')
length = min(len(lis_1), len(lis_2))
result = compare(lis_1[:length], lis_2[:length])
if result == 0:
    if len(lis_1) > len(lis_2):
        print(1)
    elif len(lis_1) == len(lis_2):
        print(0)
    else:
        print(-1)
else:
    print(result)