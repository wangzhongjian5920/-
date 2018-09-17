# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 13:17:12 2018

@author: Administrator
"""
from collections import deque

n, m = list(map(int, input().strip().split( )))
roads = []
q = deque()
for _ in range(m):
    s, t = list(map(int, input().strip().split( )))
    roads.append([s, t])
for road in roads:
    flag = 0
    for _ in range(len(q)):
        path = q.popleft()
        if path[-1] == road[0] and road[1] not in path:
            q.append(path)
            q.append([path[0], road[1]])
        elif path[0] == road[1] and road[0] not in path:
            q.append(path)
            q.append([road[0], path[1]])
    q.append(road)
fin = []
while len(q):
    fin.append(q.popleft())
dp = [0 for _ in range(n + 1)]
for i in range(n + 1):
    for path in fin:
        if path[0] == i:
            dp[i] += 1
        elif path[1] == i:
            dp[i] -= 1
print(dp)
count = 0
for i in dp:
    if i > 0:
        count += 1
print(count)