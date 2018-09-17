# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 21:18:31 2018

@author: Administrator
"""
def find(string_a, string_b):
    if len(string_a) < len(string_b):
        return 0
    dp = [[0 for _ in range(len(string_a) + 1)] for _ in range(len(string_b) + 1)]
    for i in range(len(string_a) + 1):
        dp[0][i] = 1
    for i in range(1, len(string_a) + 1):
        for j in range(1, len(string_b) + 1):
            if string_a[i - 1] == string_b[j - 1]:
                dp[j][i] = dp[j-1][i-1]
    return sum(dp[-1])

a = list(input().strip())
b = list(input().strip())
n = int(input())
res = []
for _ in range(n):
    l,r = list(map(int, input().strip().split()))
    num = find(a[l : r + 1], b)
    res.append(num)
for i in res:
    print(i)