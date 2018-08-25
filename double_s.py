# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 13:23:41 2018

@author: Administrator
"""

def check(bag):
    for i in range(len(bag)):
        for j in range(i + 1, len(bag)):
            if len(bag[i]) == len(bag[j]):
                for k in range(1, len(bag[i])):
                    if bag[i] == bag[j][:k] + bag[j][k:] or bag[i] == bag[j][:k][:-1] + bag[j][k:][:-1]:
                        return 1
    return 0

num_pairs = int(input())
num_cols = int(input())

result = ["Sad" for _ in range(num_pairs)]
for i in range(num_pairs):
    bag = []
    for j in range(num_cols):
        bag.append(input())
    if check(bag):
        result[i] = "Yeah"
for i in result:
    print(i)
    