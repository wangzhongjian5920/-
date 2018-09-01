# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 20:13:39 2018

@author: Administrator
"""

"""
题目描述
小易总是感觉饥饿，所以作为章鱼的小易经常出去寻找贝壳吃。最开始小易在一个初始位置x_0。
对于小易所处的当前位置x，他只能通过神秘的力量移动到 4 * x + 3或者8 * x + 7。
因为使用神秘力量要耗费太多体力，所以它只能使用神秘力量最多100,000次。
贝壳总生长在能被1,000,000,007整除的位置(比如：位置0，位置1,000,000,007，位置2,000,000,014等)。
小易需要你帮忙计算最少需要使用多少次神秘力量就能吃到贝壳。
输入描述:
输入一个初始位置x_0,范围在1到1,000,000,006
输出描述:
输出小易最少需要使用神秘力量的次数，如果使用次数使用完还没找到贝壳，则输出-1
示例1
输入
125000000
输出
1
"""
from collections import deque

def find_shell():
    max_time = 100000
    division = 1000000007
    a = int(input().strip())
    mod_1 = a%division
    if mod_1 == 0:
        return 0
    q = deque()
    q.append([mod_1, 0])
    while (len(q) != 0):
        lis = q.popleft()
        if lis[1] < max_time:
            if (4 * lis[0] + 3)%division == 0 or (8 * lis[0] + 7)%division == 0:
                return lis[1] + 1
            new_lis1 = [(4 * lis[0] + 3)%division, lis[1] + 1]
            new_lis2 = [(8 * lis[0] + 7)%division, lis[1] + 1]
            q.append(new_lis1)
            q.append(new_lis2)

print(find_shell())
    
