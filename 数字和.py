# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 13:42:27 2018

@author: Administrator
"""

if __name__ == "__main__":
    num, target = map(int, input().strip().split(' '))
    lis = list(map(int, input().strip().split(' ')))
    lis.sort()
    if target == 0:
        print(1)
    else:
        dp = [0 for _ in range(target + 1)]
        for i in range(len(lis)):
            if lis[i] > target:
                break
            value = lis[i]
            for j in range(target - value, -1, -1):
                if dp[j] != 0 and j + value <= target:
                    dp[j + value] += dp[j]
            dp[value] += 1
        print(dp[-1])
        
        