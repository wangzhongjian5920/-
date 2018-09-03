# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 16:12:41 2018

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
"""
import re
 
if __name__ == "__main__":
    pattern1 = re.compile(r"[^A-Z]+")
    pattern2 = re.compile(r"([A-Z])\1")
    pattern3 = re.compile(r"([A-Z])[A-Z]*([A-Z])[A-Z]*\1[A-Z]*\2")
    word = input().strip('\n')
    if pattern1.search(word) or pattern2.search(word) or pattern3.search(word):
        print("Dislikes")
    else:
        print("Likes")