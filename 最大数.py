# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 00:46:28 2018

@author: Administrator
"""
def first(lis):
    dic = {}
    new_lis = []
    max_length=len(str(max(lis)))
    for i in range(len(lis)):
        key = lis[i]
        value = lis[i]
        if len(str(lis[i])) < max_length:
            key *= 10 ** (max_length - len(str(lis[i])))
        new_lis.append(key)
        dic[key] = value
    return dic, new_lis

num = int(input())
lis = []
res = []
for _ in range(num):
    lis.append(int(input()))

dic, new_lis = first(lis)
sorted(new_lis).reverse()
for i in new_lis:
    res.append(dic[i])
print(res)
print(''.join(list(map(str, res))))