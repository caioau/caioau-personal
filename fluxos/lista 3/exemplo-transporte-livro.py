#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import networkx as nx
import numpy as np

G = nx.DiGraph()
# Adiciona nos de oferta
G.add_node(1, demand=-18)
G.add_node(2, demand=-22)
G.add_node(3, demand=-39)
G.add_node(4, demand=-14)
# Adiciona nos de demanda
G.add_node(5, demand=10)
G.add_node(6, demand=11)
G.add_node(7, demand=13)
G.add_node(8, demand=20)
G.add_node(9, demand=24)
G.add_node(10, demand=15)
# Adiciona os arcos
G.add_edge(1, 5, weight=10)
G.add_edge(2, 5, weight=15)
G.add_edge(3, 5, weight=17)
G.add_edge(4, 5, weight=19)
# ###################################
G.add_edge(1, 6, weight=12)
G.add_edge(2, 6, weight=18)
G.add_edge(3, 6, weight=16)
G.add_edge(4, 6, weight=18)
# ###################################
G.add_edge(1, 7, weight=13)
G.add_edge(2, 7, weight=12)
G.add_edge(3, 7, weight=13)
G.add_edge(4, 7, weight=20)
# ####################################
G.add_edge(1, 8, weight=8)
G.add_edge(2, 8, weight=16)
G.add_edge(3, 8, weight=14)
G.add_edge(4, 8, weight=21)
# ################################
G.add_edge(1, 9, weight=14)
G.add_edge(2, 9, weight=19)
G.add_edge(3, 9, weight=10)
G.add_edge(4, 9, weight=12)
# ################################
G.add_edge(1, 10, weight=19)
G.add_edge(2, 10, weight=20)
G.add_edge(3, 10, weight=18)
G.add_edge(4, 10, weight=13)
flowCost, flowDict = nx.network_simplex(G)
print flowCost
# print flowDict
k,w = 0,0
mat = np.zeros([4,6])
cost = np.zeros([4,6])
total = 0
for i in flowDict:
    #print "i:%d\n"%i
    w = 0
    for j in flowDict[i]:
        # print flowDict[i][j],
        mat[k,w] = flowDict[i][j]
        cost[k,w] = G[i][j]["weight"]
        w += 1
        total += flowDict[i][j]*G[i][j]["weight"]
    k += 1
    #print "\n"
print mat
print cost
print total