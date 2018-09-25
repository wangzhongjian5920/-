# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 14:12:58 2018

@author: Administrator
"""
import re

string = input().strip()
pattern = re.compile(r'\d+')
lis = pattern.findall(string)
max_length = 0
res = []
for i in range(len(lis)):
    nums = list(map(int, lis[i]))
    dp = [0 for i in range(len(nums))]
    dp[0] = 1
    for j in range(1, len(nums)):
        if nums[j] - nums[j-1] > 0:
            dp[j] = dp[j-1] + 1
        else:
            dp[j] = 1
    length = max(dp)
    if length > max_length:
        res = []
        for j in range(length - 1, len(nums)):
            if dp[j] == length:
                res.append(''.join(map(str, nums[j-length+1:j+1])))
        max_length = length
    elif length == max_length:
        for j in range(length - 1, len(nums)):
            if dp[j] == length:
                res.append(''.join(map(str, nums[j-length+1:j+1])))
for i in res:
    print(i)
#dp = [0 for _ in range(len(string))]
#dp[0] = 1
#for i in range(1, len(string)):
#    if ord(string[i]) > ord(string[i-1]):
#        dp[i] = dp[i-1] + 1
#    else:
#        dp[i] = 1
#max_value = max(dp)
#
#i = max_value - 1
#while i <= len(string) - 1:
#    if dp[i] == max_value:
#        print(''.join(string[i-max_value + 1:i+1]))
#        i += max_value
#    else:
#        i += max_value- dp[i]