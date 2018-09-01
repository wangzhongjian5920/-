# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 14:46:24 2018

@author: Administrator
"""

##有 n 个学生站成一排，每个学生有一个能力值，
##牛牛想从这 n 个学生中按照顺序选取 k 名学生，
##要求相邻两个学生的位置编号的差不超过 d，使得这 k 个学生的能力值的乘积最大，
##你能返回最大的乘积吗？

array = input("please input the ability of members: ").split( )
k = int(input("please input number of members: "))
d= int(input("please input max interval of members: "))
print(len(array), k)
dp_max = [[0 * len(array)] * (k + 1)]
dp_min = [[0 * len(array)] * (k + 1)]

for i in range(len(array)):
    dp_max[i][1] = int(array[i])
    dp_min[i][1] = int(array[i])
print(dp_max)
for p in range(len(array)):
    for num in range(1, k + 1):
        for interval in range(1, d + 1):
            if p - interval >= 0:
                dp_max[num][p] = max(dp_max[num][p], max(dp_max[num-1][p - interval] * int(array[p]), \
                      dp_min[num-1][p - interval] * int(array[p])))
                dp_min[num][p] = min(dp_min[num][p], min(dp_max[num-1][p - interval] * int(array[p]), \
                      dp_min[num-1][p - interval] * int(array[p])))
print(dp_max)
                
                