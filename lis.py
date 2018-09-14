# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 19:09:15 2018

@author: Administrator
"""
"""
题目描述
小易来到了一条石板路前，每块石板上从1挨着编号为：1、2、3.......
这条石板路要根据特殊的规则才能前进：对于小易当前所在的编号为K的 石板，小易单次只能往前跳K的一个约数(不含1和K)步，即跳到K+X(X为K的一个非1和本身的约数)的位置。 小易当前处在编号为N的石板，他想跳到编号恰好为M的石板去，小易想知道最少需要跳跃几次可以到达。
例如：
N = 4，M = 24：
4->6->8->12->18->24
于是小易最少需要跳跃5次，就可以从4号石板跳到24号石板
输入描述:
输入为一行，有两个整数N，M，以空格隔开。 (4 ≤ N ≤ 100000) (N ≤ M ≤ 100000)
输出描述:
输出小易最少需要跳跃的步数,如果不能到达输出-1
"""
def find_all(k):
    lis = []
    for i in range(2, k//2):
        if k%i == 0:
            lis.append(i)
    lis.reverse
    return lis

n, m = list(map(int, input().strip().split( )))
lis = [-1 for _ in range(m + 1)]
lis[n] = 0
for j in range(n + 1, len(lis)):
    for i in find_all(j):
        if lis[j-i] != -1 and lis[j] == -1:
            lis[j] = lis[j-i] + 1
        elif lis[j-i] != -1 and lis[j] != -1:
            lis[j] = min(lis[j], lis[j-i] + 1)
print(lis[-1])
