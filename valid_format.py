# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 12:41:50 2018

@author: Administrator
"""

if __name__ == "__main__":
    n = int(input())
    graph = [[0 for _ in range(n + 1)] for _ in range(3)]
    graph[0][0] = "numbers"
    graph[1][0] = "porm"
    graph[2][0] = "col"
    graph[0][1] = 10
    graph[0][2] = 90
    if n == 1:
        print(10)
    elif n == 2:
        print(20)
    else:
        for i in range(3, n + 1):
            graph[0][i] = 10**int(i) - 10**int(i-1)
            graph[2][i] += graph[0][i-2]
            for j in range(2, i):
                graph[1][i] += 2*((graph[0][j-1]+graph[1][j-1]) * (graph[0][n-j]+graph[1][j-1]))
                if i-1 >= 3:
                    graph[2][i] += graph[0][i-3]
                if n -i >= 3:
                    graph[2][i] += graph[0][n-i-2]
        for i in graph:
            print(i)
        print((graph[0][n]+graph[1][n]+graph[2][n])%1000000007)