# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 22:00:26 2018

@author: Administrator
"""
from collections import deque
from copy import deepcopy

a,b,c = map(int, input().strip().split(' '))
q = deque()
q.append([[1,0,0], 'r'])
q.append([[0,1,0], 'b'])
q.append([[0,0,1], 'y'])
count = 0
while len(q) != 0:
    sta, col = list(q.popleft())
    if sum(sta) == a + b + c:
        count += 1
    else:
        if col == 'r':
            if sta[1] <= b - 1:
                new_sta = deepcopy(sta)
                new_sta[1] += 1
                new_col = 'b'
                q.append([new_sta, new_col])
            if sta[2] <= c - 1:
                new_sta = deepcopy(sta)
                new_sta[2] += 1
                new_col = 'y'
                q.append([new_sta, new_col])
        if col == 'b':
            if sta[0] <= a - 1:
                new_sta = deepcopy(sta)
                new_sta[0] += 1
                new_col = 'r'
                q.append([new_sta, new_col])
            if sta[2] <= c - 1:
                new_sta = deepcopy(sta)
                new_sta[2] += 1
                new_col = 'y'
                q.append([new_sta, new_col])
        if col == 'y':
            if sta[0] <= a - 1:
                new_sta = deepcopy(sta)
                new_sta[0] += 1
                new_col = 'r'
                q.append([new_sta, new_col])
            if sta[1] <= b - 1:
                new_sta = deepcopy(sta)
                new_sta[1] += 1
                new_col = 'b'
                q.append([new_sta, new_col])
print(count)
            
                
    
