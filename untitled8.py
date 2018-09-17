# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 12:24:47 2018

@author: Administrator
"""

if __name__ == "__main__":
    n = [i for i in list(input().strip()) if i != ' ']
    flag = 0
    visited = []
    for i in range(len(n))[::-1]:
        if n[i] not in visited:
            if n[i] not in n[:i]:
                flag = 1
                print(n[i])
                break
            else:
                visited.append(n[i])
    if flag == 0:
        print("NUll")