# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 21:56:26 2018

@author: Administrator
"""
def an(res):
    zeros = []
    for i in range(n):
        print(res[i])
        zero = len(res) - sum(res[i])
        if zero not in zeros:
            zeros.append(zero)
    if sum(zeros) != len(res):
        return False
    return True
        

a = int(input())
for _ in range(a):
    n, m = list(map(int, input().strip().split( )))
    lis = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        s, t = list(map(int, input().strip().split( )))
        lis[s-1][t-1] = 1
        lis[t-1][s-1] = 1
    res = []
    for i in range(n):
        res.append(lis[i])
    if an(res):
        print('yes')
    else:
        print('no')