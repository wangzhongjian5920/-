# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 17:15:03 2018

@author: Administrator
"""
import sys

def solution():
    final = []
    while True:
        things = sys.stadin.readline().strip()
        if len(things) != 0:
            things = things.split( )
            for i in things:
                if i not in final:
                    final.append(i)
        else:
            break
    print(len(final))
    
solution()