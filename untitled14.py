# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 17:32:13 2018

@author: Administrator
"""
def valid(total, group_2):
    for i in range(len(group_2)):
        m = group_2[i]
        for j in range(i+1, len(group_2)):
            k = group_2[j]
            if total[m-1][k] == 0:
                return False
    return True
    
num = int(input())
req = int(input())
grid = [[1 for i in range(num)] for j in range(num)]
total = [[0] for _ in range(num)]
for _ in range(req):
    n, m = list(map(int, input().strip().split()))
    total[n-1].append(m)
    total[m-1].append(n)
max_time = 0
for i in range(len(total)):
    lis = total[i]
    if len(lis) >= max_time:
        group_2 = lis.sort()
        max_time = len(lis)
if len(group_2) == 0:
    print(0)
else:
    if valid(total, group_2):
        print(1)
    else:
        print(0)