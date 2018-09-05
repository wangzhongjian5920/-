# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 16:54:35 2018

@author: Administrator
"""
from copy import deepcopy

def dp(array, m, lis):
    if m == 0:
        print(' '.join(list((map(str, lis)))))
    if len(array) != 0 and array[0] <= m:
        new_lis = deepcopy(lis)
        new_lis.append(array[0])
        dp(array[1:], m - array[0], new_lis)
        dp(array[1:], m, lis)
            
if __name__ == "__main__":
    n, m = map(int, input().strip().split( ))
    if n > m:
        array = [i for i in range(1, m + 1)]
    else:
        array = [i for i in range(1, n + 1)]
    dp(array, m, [])