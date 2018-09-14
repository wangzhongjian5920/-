# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 22:29:04 2018

@author: Administrator
"""

n = int(input())
if n == 0 or n == 1:
    print(0, 0)
elif n == 2:
    print(1, 0)
else:
    print(3 * (n - 3) + 3, 3 * (n - 3) + 1)