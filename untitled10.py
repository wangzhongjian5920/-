# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 21:56:45 2018

@author: Administrator
"""
string_a = 'baba'
string_b = 'ababa'
dp = [0 for _ in range(1 + len(string_a))]
for i in range(len(string_a)):
    for j in range(len(string_b)):
        if string_a[i] == string_b[j]:
            dp[i+1] = max(max(dp[:i+1]) + 1, dp[i+1])
        else:
            dp[i+1] = max(max(dp[:i+1]), dp[i+1])
print(dp[-1])
lis = []
i = 1
for j in range(len(dp)):
    if dp[j] == i:
        i += 1
        lis.append(string_a[j-1])
print(''.join(map(str,lis)))
    