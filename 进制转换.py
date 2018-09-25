# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 20:26:45 2018

@author: Administrator
"""
def change(dic, m, n):
    lis = list(n)
    base = 1
    res = 0
    for i in range(len(lis))[::-1]:
        res += dic[lis[i]] * base
        base *= m
    return res

if __name__ == "__main__":
    lis = []
    real_input = []
    dic = {}
    for i in range(10):
        dic[str(i)] = i
    for i in range(10, 16):
        dic[chr(i + 55)] = i
        
    while True:
        inp = input().strip()
        if inp == "END":
            break
        real_input.append(inp)
        m, n = map(inp.split('#'))
        m = int(m)
        lis.append(change(dic, m, n))
    fin = []
    visited = []
    for i in range(len(lis)):
        if lis[i] not in visited:
            if lis.count(lis[i])  == 1:
                fin.append(real_input[i])
            visited.append(lis[i])
    if len(fin) == 0:
        print('None')
    else:
        for i in fin:
            print(i)
        