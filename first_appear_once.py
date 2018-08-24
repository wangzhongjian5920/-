# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 22:18:38 2018

@author: Administrator
"""
from collections import defaultdict

def first_ap_once(string):
    d = defaultdict()
    for i in string:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] += 1
    for i in string:
        if d[i] == 1:
            print(i)
            break
        