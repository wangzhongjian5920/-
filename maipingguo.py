# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 16:36:07 2018

@author: Administrator
"""
"""
小易去附近的商店买苹果，奸诈的商贩使用了捆绑交易，
只提供6个每袋和8个每袋的包装(包装不可拆分)。 可是小易现在只想购买恰好n个苹果，
小易想购买尽量少的袋数方便携带。如果不能购买恰好n个苹果，小易将不会购买。
"""

##设6个每袋的买 0、1、2、3袋
count = [-1, -1, -1, -1, -1]
n = int(input())
if n%8 == 0:
    count[0] = n//8
if (n - 6)%8 == 0:
    count[1] = 1 + (n - 6)//8
if (n - 12)%8 == 0:
    count[2] = 2 + (n - 12)//8
if (n - 18) == 0:
    count[3] = 3 + (n - 18)//8
fin = []
for i in count:
    if i != -1:
        fin.append(i)
if len(fin) != 0:
    print(min(fin))
else:
    print(-1)
