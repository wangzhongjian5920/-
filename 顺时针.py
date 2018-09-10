# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 17:34:26 2018

@author: Administrator
"""

def rotate_conter_clock(grid):
    if len(grid) == 1:
        return grid[0], []
    value = grid[0]
    grid = grid[1:]
    width = len(grid)
    length = len(grid[0])
    new_grid = [[0 for _ in range(width)] for _ in range(length)]
    for i in range(width):
        for j in range(length):
            new_grid[length - 1 - j][i] = grid[i][j]
    for i in grid:
        print(i)
    for j in grid:
        print(j)
        
grid = [[1,2], [3, 4]]
rotate_conter_clock(grid)