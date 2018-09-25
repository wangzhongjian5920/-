# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 18:11:26 2018

@author: Administrator
"""

s= list(input().strip())
x = len(s)
n= (ord(s[0])-97)*((26*25+1)*25+1)
if x > 1:
    n+=(ord(s[1])-97)*(26*25+1)+1
if x>2:
    n+=(ord(s[2])-97)*26+1
if x>3:
    n+=ord(s[3])-97+1
print (n)