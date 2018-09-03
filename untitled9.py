# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 15:26:45 2018

@author: Administrator
"""

"""
题目描述
小易喜欢的单词具有以下特性：
1.单词每个字母都是大写字母
2.单词没有连续相等的字母
3.单词没有形如“xyxy”(这里的x，y指的都是字母，并且可以相同)这样的子序列，子序列可能不连续。
例如：
小易不喜欢"ABBA"，因为这里有两个连续的'B'
小易不喜欢"THETXH"，因为这里包含子序列"THTH"
小易不喜欢"ABACADA"，因为这里包含子序列"AAAA"
小易喜欢"A","ABA"和"ABCBA"这些单词
给你一个单词，你要回答小易是否会喜欢这个单词（只要不是不喜欢，就是喜欢）。
输入描述:
输入为一个字符串，都由大写字母组成，长度小于100
输出描述:
如果小易喜欢输出"Likes",不喜欢输出"Dislikes"
"""

def appear_table(string):
    dic = {}
    dp = [0 for _ in range(len(string))]
    if len(string):
        dic[string[0]] = 1
        dp[0] = 1
    for index in range(1, len(string)):
        if string[index] == string[index - 1]:
            return False
        zimu = string[index]
        if zimu in dic.keys():
            dic[zimu] += 1
            dp[index] = dic[zimu]
            if dic[zimu] == 4:
                return False
        else:
            dic[zimu] = 1
            dp[index] = 1
    return True

if __name__ == "__main__":
    string = input().strip()
    if appear_table(string):
        print("Likes")
    else:
        print("Dislikes")