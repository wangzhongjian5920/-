# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 15:06:12 2018

@author: Administrator
"""

"""
题目描述
考拉有n个字符串字符串，任意两个字符串长度都是不同的。考拉最近学习到有两种字符串的排序方法： 1.根据字符串的字典序排序。例如：
"car" < "carriage" < "cats" < "doggies < "koala"
2.根据字符串的长度排序。例如：
"car" < "cats" < "koala" < "doggies" < "carriage"
考拉想知道自己的这些字符串排列顺序是否满足这两种排序方法，考拉要忙着吃树叶，所以需要你来帮忙验证。
输入描述:
输入第一行为字符串个数n(n ≤ 100)
接下来的n行,每行一个字符串,字符串长度均小于100，均由小写字母组成
输出描述:
如果这些字符串是根据字典序排列而不是根据长度排列输出"lexicographically",

如果根据长度排列而不是字典序排列输出"lengths",

如果两种方式都符合输出"both"，否则输出"none"
"""
def in_order(front, back):
    front_point = 0
    back_point = 0
    while (front_point != len(front) and back_point != len(back)):
        if ord(front[front_point]) < ord(back[back_point]):
            return True
        elif ord(front[front_point]) > ord(back[back_point]):
            return False
        front_point += 1
        back_point += 1
    if len(front) < len(back):
        return True
    return False

if __name__ == "__main__":
    a = int(input().strip())
    if a < 2:
        print("both")
    else:
        flag_1 = 1
        flag_2 = 1
        front = input().strip()
        for _ in range(a - 1):
            back = input().strip()
            if flag_2 == 1:
                if len(back) < len(front):
                    flag_2 = 0
            if flag_1 == 1:
                if not in_order(front, back):
                    flag_1 = 0
            front = back
        if flag_1 and flag_2:
            print("both")
        elif flag_1:
            print("lexicographically")
        elif flag_2:
            print("lengths")
        else:
            print("none")
            