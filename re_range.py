# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 14:54:47 2018

@author: Administrator
"""

"""
题目描述
牛牛的作业薄上有一个长度为 n 的排列 A，这个排列包含了从1到n的n个数，但是因为一些原因，其中有一些位置（不超过 10 个）看不清了，但是牛牛记得这个数列顺序对的数量是 k，顺序对是指满足 i < j 且 A[i] < A[j] 的对数，请帮助牛牛计算出，符合这个要求的合法排列的数目。
输入描述:
每个输入包含一个测试用例。每个测试用例的第一行包含两个整数 n 和 k（1 <= n <= 100, 0 <= k <= 1000000000），接下来的 1 行，包含 n 个数字表示排列 A，其中等于0的项表示看不清的位置（不超过 10 个）。
输出描述:
输出一行表示合法的排列数目。
"""
from copy import deepcopy
from itertools import permutations

def count_pairs(array):
    count = 0
    for i in range(1, len(array)):
        for j in range(i):
            if array[i] > array[j]:
                count += 1
    return count
    
def packet_and_count(new_array, locations, perm):
    for i in range(len(locations)):
        new_array[locations[i]] = perm[i]
    return new_array

if __name__ == "__main__":
    numbers, pairs =  map(int, input().strip().split( ))
    ##record states, change datatype
    array = input().strip().split( )
    state = [0 for _ in range(numbers + 1)]
    locations = []
    for i in range(len(array)):
        array[i] = int(array[i])
        state[array[i]] = 1
        if array[i] == 0:
            locations.append(i)
    new_array = deepcopy(array)
    ##record not_used_numberrs
    number_not_used = []
    for i in range(numbers + 1):
        if state[i] == 0:
            number_not_used.append(i)
            
    if len(locations) == 0:
        if count_pairs(array) == pairs:
            print(1)
        else:
            print(0)
    else:
        perms = permutations(number_not_used, len(number_not_used))
        count = 0
        for perm in list(perms):
            if count_pairs(packet_and_count(new_array, locations, perm)) == pairs:
                count += 1
        print(count)