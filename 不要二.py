# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 19:30:16 2018

@author: Administrator
"""
"""
题目描述
二货小易有一个W*H的网格盒子，网格的行编号为0~H-1，网格的列编号为0~W-1。每个格子至多可以放一块蛋糕，任意两块蛋糕的欧几里得距离不能等于2。
对于两个格子坐标(x1,y1),(x2,y2)的欧几里得距离为:
( (x1-x2) * (x1-x2) + (y1-y2) * (y1-y2) ) 的算术平方根
小易想知道最多可以放多少块蛋糕在网格盒子里。
输入描述:
每组数组包含网格长宽W,H，用空格分割.(1 ≤ W、H ≤ 1000)
输出描述:
输出一个最多可以放的蛋糕数
"""
def putcake(row_i, wideth):
    if row_i%4 in [0, 1]:
        parts, remain = divmod(wideth, 4)
        cakes = 2 * parts + min(remain, 2)
    else:
        parts, remain = divmod(wideth, 4)
        cakes = 2 * parts + max(remain - 2, 0)
    return cakes

if __name__ == '__main__':
    total_cakes = 0
    m, w = map(int, input().strip().split( ))
    for i in range(m):
        total_cakes += putcake(i, w)
    print(total_cakes)

    