# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 12:35:30 2018

@author: Administrator
"""

if __name__ == "__main__":
    n = input().strip().split( )
    for i in range(len(n)):
        lis = list(n[i])
        lis.reverse()
        n[i] = ''.join(lis)
    print(' '.join(n))