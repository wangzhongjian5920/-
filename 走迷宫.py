# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 17:14:15 2018

@author: Administrator
"""

if __name__ == "__main__":
    n = int(input())
    grid = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        lis = list(map(int, input().strip().split(',')))
        for j in range(n):
            grid[i][j] = lis[j]
    new_grid = grid[0]
    for i in range(1, n):
        new_grid[i] += grid[0][i-1]
    layer = 0
    while(layer != n - 1):
        layer += 1
        result = grid[layer]
        result[0] += new_grid[0]
        for i in range(1, n):
            result[i] = min(result[i - 1] + result[i], new_grid[i] + result[i])
        new_grid = result
    print(result[-1])