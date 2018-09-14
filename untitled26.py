# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 17:01:52 2018

@author: Administrator
"""
                                                                                                                                                                                                                                                                                                                                                
n = int(input())
lis = [0 for _ in range(n)]
for i in range(n):
    a = int(input())
    lis[i] = a
line = []
aim = list(set(lis))
min_length = n
pos_left = 0
pos_right = 0
res = []
for i in range(n):
    if len(line) == len(aim):
        length = pos_right - pos_left + 1
        if length == min_length:
            res.append([pos_left, pos_right])
        elif length < min_length:
            min_length = length
            res = [[pos_left, pos_right]]
    if len(line) == 0:
        line.append(lis[i])
        pos_left = i + 1
        pos_right = i + 1
    else:
        if lis[i] != line[0]:
            if lis[i] not in line:
                line.append(lis[i])
                pos_right += 1
            else:
                pos_right += 1
        else:
            line = line[1:]
            line.append(lis[i])
            pos_left += 1
            pos_right += 1
print(min_length, len(res))
fin = str(res[0])
for i in range(1, len(res)):
    fin += ' ' + str(res[i])
print(fin)
    
        































































































































































































































































































































































