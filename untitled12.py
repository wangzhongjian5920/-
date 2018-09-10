# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 18:16:58 2018

@author: Administrator
"""
input_1, input_2 = list(input().strip().split( ))
lis_1 = input_1.split('.')
lis_2 = input_2.split('.')

com_length = min(len(lis_1), len(lis_2))
for i in range(com_length):
    if lis_1 < lis_2:
        