# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 22:27:19 2018

@author: Administrator
"""    

import networkx as nx

g = nx.DiGraph()
a = int(input())

for i in range(a + 2):
    g.add_node(i)

for _ in range(a - 1):
    s, t = map(int, input().strip().split( ))
    g.add_edge(s, t, capacity=1)
g.add_edge(0, 1, capacity=float('inf'))
for i in range(2, a):
    g.add_edge(i, a + 1, capacity=float('inf'))

max_flow = nx.algorithms.flow.maxflow.maximum_flow(g, 0, a+1)[0]
print(2 * max_flow)