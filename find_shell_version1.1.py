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
def f(x):
    division = 1000000007
    return (4 * x + 3)%division

def g(x):
    division = 1000000007
    return (8 * x + 7)%division

def find_shell():
    ##f(x) = 4 * mod + 3
    ##g(x) = 8 * mod + 7
    ##执行顺序无影响
    ##执行3次f = 执行2次g
    max_time = 100000
    division = 1000000007
    a = int(input().strip())
    mod_0 = a%division
    mod_1 = mod_0
    time_1 = 0
    mod_2 = f(mod_0)
    time_2 = 1
    mod_3 = f(f(mod_0))
    time_3 = 2
    if mod_0 == 0:
        return 0
    ##执行0次f
    while(time_1 < max_time):
        mod_1 = g(mod_1)
        time_1 += 1
        if mod_1 == 0:
            break
    while(time_2 < min(max_time,time_1)):
        mod_2 = g(mod_2)
        time_2 += 1
        if mod_2 == 0:
            break
    while(time_3 < min(time_1, time_2)):
        mod_3 = g(mod_3)
        time_3 += 1
        if mod_3 == 0:
            break
    return min(min(time_1, min(time_2, time_3)), max_time)

print(find_shell())
