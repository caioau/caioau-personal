#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import networkx as nx
import numpy as np

G = nx.DiGraph()
# Adiciona nos de oferta
G.add_node(1, demand=-18)
G.add_node(2, demand=-24)
G.add_node(3, demand=-6)
G.add_node(4, demand=-12)
# Adiciona nos de demanda
G.add_node(5, demand=6)
G.add_node(6, demand=14)
G.add_node(7, demand=35)
G.add_node(8, demand=5)
# Adiciona os arcos
G.add_edge(1, 5, weight=9)
G.add_edge(2, 5, weight=10)
G.add_edge(3, 5, weight=8)
G.add_edge(4, 5, weight=10)
# ###################################
G.add_edge(1, 6, weight=8)
G.add_edge(2, 6, weight=10)
G.add_edge(3, 6, weight=9)
G.add_edge(4, 6, weight=10)
# ###################################
G.add_edge(1, 7, weight=12)
G.add_edge(2, 7, weight=12)
G.add_edge(3, 7, weight=11)
G.add_edge(4, 7, weight=11)
# ####################################
G.add_edge(1, 8, weight=13)
G.add_edge(2, 8, weight=14)
G.add_edge(3, 8, weight=12)
G.add_edge(4, 8, weight=12)
flowCost, flowDict = nx.network_simplex(G)
print flowCost
# print flowDict
k,w = 0,0
mat = np.zeros([4,4])
cost = np.zeros([4,4])
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
