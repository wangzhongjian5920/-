# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 17:48:36 2018

@author: Administrator
"""

string_a = list(input().strip())
string_b = list(input().strip())
string_c = [string_a[i] for i in range(len(string_a)) if string_a[i] not in string_b]
print(''.join(string_c))