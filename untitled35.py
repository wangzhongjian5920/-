# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 21:46:01 2018

@author: Administrator
"""
def comp(string_a, string_b):
    lis1 = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v']
    lis2 = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'b', 'n', 'm']
    cost_1 = 3 * max(len(string_a), len(string_b))
    cost_2 = 3 * max(len(string_a), len(string_b))
    cost_3 = 3 * max(len(string_a), len(string_b))
    cost_4 = 3 * max(len(string_a), len(string_b))
    if string_a == '' or string_b == '':
        if string_a == '' and string_b == '':
            return 0
        else:
            return float('Inf')
    if string_a[0] == string_b[0]:
        return comp(string_a[1:], string_b[1:])
    if len(string_a) > len(string_b):
        cost_1 = 3 + comp(string_a[1:], string_b)
    if len(string_a) < len(string_b):
        cost_2 = 3 + comp(str(string_b[0]) + string_a, string_b)
    if len(string_a) == len(string_b):
        if (string_a[0] in lis1 and string_b[0] in lis2) or\
        (string_a[0] in lis2 and string_b[0] in lis1):
            cost_3 = 2 + comp(string_a[1:], string_b[1:])
        else:
            cost_4 = 1 + comp(string_a[1:], string_b[1:])
    return min([cost_1, cost_2, cost_3, cost_4])
    
a = list(input().strip().split(' '))
grid = [[float('Inf') for _ in range(len(a))] for _ in range(len(a))]
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        grid[i][j] = comp(a[i], a[j])
## zhanshi
for i in grid:
    print(i)
#lis = []
#for i in range(len(a)):
#    count = 0
#    for j in range(len(a)):
#        if i != j:
#            count += comp(a[i], a[j])
#    lis.append(count)
#string = ''
#count = 0
#while count <= 3:
#    for i in range(len(lis)):
#        if lis[i] == min(lis):
#            string += str(a[i])
#            lis.remove(i)
#            count += 1
        
