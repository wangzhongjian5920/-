# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 16:48:50 2018

@author: Administrator
"""

"""
题目描述
A,B,C三个人是好朋友,每个人手里都有一些糖果,我们不知道他们每个人手上具体有多少个糖果,但是我们知道以下的信息：
A - B, B - C, A + B, B + C. 这四个数值.每个字母代表每个人所拥有的糖果数.
现在需要通过这四个数值计算出每个人手里有多少个糖果,即A,B,C。这里保证最多只有一组整数A,B,C满足所有题设条件。
输入描述:
输入为一行，一共4个整数，分别为A - B，B - C，A + B，B + C，用空格隔开。 范围均在-30到30之间(闭区间)。
输出描述:
输出为一行，如果存在满足的整数A，B，C则按顺序输出A，B，C，用空格隔开，行末无空
"""

lis = list(map(int, input().strip().split( )))
two_a = lis[0] + lis[2]
two_b = lis[1] + lis[3]
if two_a >= 0 and two_b >= 0:
    if two_a%2 == 0 and two_b%2== 0:
        a = two_a//2
        b = two_b//2
        c = b - lis[1]
        if c >= 0:
            print(a,b,c)
        else:
            print('No')
    else:
        print('No')
else:
    print('No')
    