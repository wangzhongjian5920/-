# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 21:33:22 2018

@author: Administrator
"""

if __name__ == "__main__":
    num = int(input())
    dic = {}
    location = []
    right = 0
    for i in range(num):
        x_axi, height = map(int, input().strip().split())
        location.append(x_axi)
        attachable = [x_axi + 1, x_axi + height - 1]
        if i == 0:
            right = x_axi + height - 1
        else:
            right = max(right, x_axi + height - 1)
        dic[x_axi] = attachable
    dp = [0 for _ in range(right + 1)]
    for i in sorted(dic.keys())[::-1]:
        lis = list(range(dic[i][0], dic[i][1] + 1))
        for j in lis:
            dp[j] += 1
            if j in dic.keys():
                dp[j] += 1
    for i in dic.keys():
        left = dic[i][0]
        right = dic[i][1]
        print(max(dp[left:right + 1]))