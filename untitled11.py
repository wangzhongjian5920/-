# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 22:29:17 2018

@author: Administrator
"""

def mod(x, a):
    t = 0
    n = a
    while n < x:
        if 2 * n > x:
            return t + 1, abs(2 * n - x)
        else:
            n *= 2
            t += 1
        
if __name__ == "__main__":
    a, b = map(int, input().strip().split( ))
    time = 10000
    for n in range(a):
        b1, k1 = mod(b, a - n)
        time = min(time, (b1 + k1) + n)
    print(time)
