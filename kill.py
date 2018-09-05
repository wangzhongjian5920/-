# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 20:52:19 2018

@author: Administrator
"""
from collections import deque

def kill(n, m):
    q = deque()
    for i in range(1, n + 1):
        q.append(i)
    while len(q) != 1:
        for _ in range(m - 1):
            q.append(q.popleft())
        q.popleft()
    return q.popleft()

print(kill(4, 2))
    