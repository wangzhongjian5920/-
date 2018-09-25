# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 18:02:01 2018

@author: Administrator
"""
"""
题目描述
小青蛙有一天不小心落入了一个地下迷宫,小青蛙希望用自己仅剩的体力值P跳出这个地下迷宫。
为了让问题简单,假设这是一个n*m的格子迷宫,迷宫每个位置为0或者1,
0代表这个位置有障碍物,小青蛙达到不了这个位置;
1代表小青蛙可以达到的位置。小青蛙初始在(0,0)位置,地下迷宫的出口在(0,m-1)
(保证这两个位置都是1,并且保证一定有起点到终点可达的路径)
小青蛙在迷宫中水平移动一个单位距离需要消耗1点体力值,
向上爬一个单位距离需要消耗3个单位的体力值,
向下移动不消耗体力值,当小青蛙的体力值等于0的时候还没有到达出口,小青蛙将无法逃离迷宫。
现在需要你帮助小青蛙计算出能否用仅剩的体力值跳出迷宫(即达到(0,m-1)位置)。

输入描述:
输入包括n+1行:
 第一行为三个整数n,m(3 <= m,n <= 10),P(1 <= P <= 100)
 接下来的n行:
 每行m个0或者1,以空格分隔
输出描述:
如果能逃离迷宫,则输出一行体力消耗最小的路径,输出格式见样例所示;
如果不能逃离迷宫,则输出"Can not escape!"。 测试数据保证答案唯一
"""
from collections import deque
from copy import deepcopy

n, m, p = list(map(int, input().strip().split(' ')))
##grid shows whether the place has obstacles
grid = []
for i in range(n):
    grid.append(list(map(int, input().strip().split(' '))))
    
## -1 不可达， 0 未探测
dp = [[-1 for _ in range(m + 2)] for _ in range(n + 2)]
for i in range(n):
    for j in range(m):
        dp[i+1][j+1] = grid[i][j] - 1

q = deque()
q.append([0,[[1, 1]]])
lis = p + 1
fin_path = []
while len(q) != 0:
    health, path = list(q.pop())
    x = path[-1][0]
    y = path[-1][1]
    if x == 1 and y == m and health < lis:
        lis = health
        fin_path = path 
    if health <= health:
        if p - health >= 3 and dp[x-1][y] != -1 and [x-1, y] not in path:
            new_path = deepcopy(path)
            new_path.append([x-1,y])
            q.append([health + 3, new_path])
        if p - health >= 1 and dp[x][y-1] != -1 and [x, y-1] not in path:
            new_path = deepcopy(path)
            new_path.append([x, y-1])
            q.append([health + 1, new_path])
        if p - health >= 1 and dp[x][y+1] != -1 and [x, y+1] not in path:
            new_path = deepcopy(path)
            new_path.append([x, y+1])
            q.append([health + 1, new_path])
        if p - health >= 0 and dp[x+1][y] != -1 and [x+1, y] not in path:
            new_path = deepcopy(path)
            new_path.append([x+1,y])
            q.append([health, new_path])
if lis == p+1:
    print('Can not escape!')
else:
    l = []
    for i in fin_path:
        string = '[' + ','.join([str(i[0] - 1), str(i[1] - 1)]) + ']'
        l.append(string)
    print(','.join(l))
        
        
                
    