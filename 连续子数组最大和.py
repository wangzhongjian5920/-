# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 15:08:10 2018

@author: Administrator
"""

if __name__ == "__main__":
    nums = int(input())
    lis = list(map(int, input().strip().split(' ')))
    dp = [0 for _ in range(nums)]
    dp[0] = max(lis[0], 0)
    for i in range(1, nums):
        if dp[i-1] > 0:
            dp[i] = dp[i-1] + lis[i]
        else:
            if lis[i] > 0:
                dp[i] = lis[i]
    print(max(dp))
    