# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 16:49:35 2018

@author: Administrator
"""

import heapq

lis = list(map(int, input().strip().split(' ')))
k = int(input())
heapq.heapify(lis)
print(' '.join(map(str,heapq.nsmallest(k, lis))))
    