# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 16:45:50 2018

@author: Administrator
"""

_, b,_, c, *rest = [1,2,3,4,5]
print(b,c,rest)

b = {'hi':'we'}
print(b.get('hi','-1'))
print(b.get('no','-1'))

file = 'foobar.hahah.hahahhah.txt'
basename, _, ext = file.rpartition('.')
print(basename, ext)