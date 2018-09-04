# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 19:37:26 2018

@author: Administrator
"""

a = list(map(int, input().strip().split( )))
temp = 0
for i in a:
    temp = temp ^ i
print(temp)