# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 22:55:15 2018

@author: Administrator
"""

tests = int(input())
res = []
for _ in range(tests):
    n, m, string = list(input().strip().split( ))
    n = int(n)
    m = int(m)
    string = list(map(int, list(string)))
    l_value = string[0]
    r_value = string[1]
    left_right = 0
    for i in range(2, len(string)):
        r_value *= m
        r_value += string[i]
    while(l_value < r_value):
        left_right += 1
        value = string[left_right]
        if ord(str(value)) >= 65:
            value = ord(str(string(left_right))) - 55
        l_value *= n
        l_value += value
        r_value -= value * (m**(len(string)-1-left_right))
    if l_value == r_value:
        res.append(l_value)
for i in res:
    print(i)