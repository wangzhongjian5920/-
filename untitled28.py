# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 23:44:05 2018

@author: Administrator
"""
from math import floor

if __name__ == "__main__":
    times = int(input())
    res = []
    for _ in range(times):
        n, m = list(map(int, input().strip().split( )))
        min_pairs = 0
        max_pairs = 0
        if n > m:
            one_group = floor(n/m)
            remain = n - one_group * m
            min_pairs = remain * one_group + (one_group - 1) * one_group//2 * m
            max_pairs = (n - m + 1) * (n - m)//2
        res.append([min_pairs, max_pairs])
    for i in res:
        print(' '.join(list(map(str,i))))
            
            