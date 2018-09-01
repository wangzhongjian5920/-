# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 19:57:47 2018

@author: Administrator
"""

"""
输入描述:
每组输入数据共两行。
第一行为字符串A
第二行为字符串B
字符串长度均小于100且只包含小写字母
输出描述:
输出一个数字，表示把字符串B插入字符串A之后构成一个回文串的方法数
"""
from math import floor

def is_huiwen_string(string):
    if len(string) % 2 == 0:
        string_1 = string[:len(string)//2]
        string_2 = string[len(string)//2:][::-1]
        if string_1 == string_2:
            return True
        return False
    else:
        string_1 = string[:floor(len(string)/2)]
        string_2 = string[floor(len(string)/2) + 1:][::-1]
        if string_1 == string_2:
            return True
        return False
        
def reverse_insert(string_a, string_b):
    count = 0
    for i in range(len(string_a)):
        new_string = string_a[:i] + string_b + string_a[i:]
        if is_huiwen_string(new_string):
            count += 1
    return count

if __name__ == "__main__":
    string_a = input().strip()
    string_b = input().strip()
    print(reverse_insert(string_a, string_b))