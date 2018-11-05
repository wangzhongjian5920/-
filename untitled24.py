# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 12:40:39 2018

@author: Administrator
"""
n = int(input())
dp = [0 for _ in range(n + 1)]
if n in [1, 2]:
    print(2)
else:
    dp[1] = 2
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
    print(dp[-1])