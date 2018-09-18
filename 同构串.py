# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 22:11:55 2018

@author: Administrator
"""
def same_structure(string_a, string_b):
    if len(string_a) != len(string_b):
        return False
    dic = {}
    for i in range(len(string_a)):
        char_a = string_a[i]
        char_b = string_b[i]
        if char_b == char_a:
            return False
        if char_b not in dic.keys() and char_a not in dic.keys():
            dic[char_b] = char_a
        elif char_b not in dic.keys() and char_a in dic.keys():
            if dic[char_a] == char_a:
                return False
            else:
                dic[char_b] = char_a
        elif char_b in dic.keys() and char_a not in dic.keys():
            if dic[char_b] != char_a:
                return False
        else:
            if dic[char_b] != char_a or dic[char_a] == char_a or \
            dic[char_a] == dic[char_b]:
                return False
    return True

if __name__ == "__main__":
    n = int(input())
    res = []
    for _ in range(n):
        string_A = input().strip()
        string_B = input().strip()
        if same_structure(string_A, string_B):
            res.append('Yes')
        else:
            res.append('No')
    for i in res:
        print(i)