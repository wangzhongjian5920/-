# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 12:40:39 2018

@author: Administrator
"""

if __name__ == "__main__":
    n = int(input())
    m = list(map(int, list(input())))
    fin = 0
    base = n
    for i in range(len(m))[::-1]:
        fin += base * m[i]
        base *= 10
    print(fin)