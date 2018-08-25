# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 12:16:12 2018

@author: Administrator
"""

def min_groups(graph, num):
    color = 2
    for i in range(1, num + 1):
        for j in range(i, num + 1):
            if graph[i][j] == 1:
                graph = colour_graph(graph, i, j, num, color)
                color += 1
    min_g = 1
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            min_g = max(graph[i][j], min_g)
    return min_g - 1
                
def colour_graph(graph, i, j, num, color):
    graph[i][j] = color
    for k in range(j, num + 1):
        if graph[j][k] == 1:
            graph = colour_graph(graph, j, k, num, color)
    return graph
    
if __name__ == "__main__":
    num = int(input())
    graph = [[0 for _ in range(num + 2)] for _ in range(num + 2)]
    for i in range(1, num + 1):
        man = input().split("\s")
        graph[i][i] = 1
        for j in man:
            j = int(j)
            if j != 0:
                graph[i][j] = 1
                graph[j][i] = 1
    print(min_groups(graph, num))