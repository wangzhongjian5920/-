# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 21:58:13 2018

@author: Administrator
"""
from math import sqrt, floor

def co_prime(a, b):
    if a >= b:
        big = a
        small = b
    else:
        big = b
        small = a
    if a == 1 or b == 1:
        return True
    if big%small == 0:
        return False
    else:
         return co_prime(big - small, small)
        