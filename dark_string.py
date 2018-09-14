# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 20:58:11 2018

@author: Administrator
"""
m = int(input())
dp = [0 for _ in range(m + 1)]
dp[1] = 3
dp[2] = 9
for i in range(3, m + 1):
    dp[i] = 2 * dp[i-1] + dp[i-2]
print(dp[-1])