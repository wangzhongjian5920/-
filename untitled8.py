# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 23:16:23 2018

@author: Administrator
"""

s = 0
for i in range(4, 52):
    s += i*(i-1)*(i-2)*(i-3)
print(s/(52*51*50*49*48))