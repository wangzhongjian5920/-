# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 14:11:41 2018

@author: Administrator
"""

"""
题目描述
n 只奶牛坐在一排，每个奶牛拥有 ai 个苹果，现在你要在它们之间转移苹果，使得最后所有奶牛拥有的苹果数都相同，每一次，你只能从一只奶牛身上拿走恰好两个苹果到另一个奶牛上，问最少需要移动多少次可以平分苹果，如果方案不存在输出 -1。
输入描述:
每个输入包含一个测试用例。每个测试用例的第一行包含一个整数 n（1 <= n <= 100），接下来的一行包含 n 个整数 ai（1 <= ai <= 100）。
输出描述:
输出一行表示最少需要移动多少次可以平分苹果，如果方案不存在则输出 -1。
"""
import sys
from copy import deepcopy

if __name__ == "__main__":
    num_of_cows = int(input())
    array = input().split( )
    if num_of_cows == len(array):
        for i in range(num_of_cows):
            array[i] = int(array[i])
    if sum(array)%num_of_cows == 0:
        avg = sum(array)//num_of_cows
        new_array = deepcopy(array)
        the_sum = 0
        for i in range(num_of_cows):
            new_array[i] -= avg
            if new_array[i] > 0:
                the_sum += new_array[i]
            if new_array[i] % 2 != 0:
                print(-1)
                sys.exit()
        print(int(the_sum//2))
    else:
        print(-1)
        sys.exit()
        