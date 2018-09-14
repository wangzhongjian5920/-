# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 15:20:02 2018

@author: Administrator
"""
def reverse(a):
    nums = list(str(a))
    nums.reverse()
    return int(''.join(nums))

m,n = list(map(int, input().strip().split( )))
while (m%10 == 0):
    m = m//10
while (n%10 == 0):
    n = n//10
print(reverse(reverse(m) + reverse(n)))