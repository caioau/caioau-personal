#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import networkx as nx

G = nx.DiGraph()
# Adiciona os arcos
G.add_edge(1, 6, weight=-12)
G.add_edge(2, 6, weight=-7)
G.add_edge(3, 6, weight=-9)
G.add_edge(4, 6, weight=-7)
G.add_edge(5, 6, weight=-9)
# ###################################
G.add_edge(1, 7, weight=-8)
G.add_edge(2, 7, weight=-9)
G.add_edge(3, 7, weight=-6)
G.add_edge(4, 7, weight=-6)
G.add_edge(5, 7, weight=-6)
# ###################################
G.add_edge(1, 8, weight=-7)
G.add_edge(2, 8, weight=-17)
G.add_edge(3, 8, weight=-12)
G.add_edge(4, 8, weight=-14)
G.add_edge(5, 8, weight=-12)
# ####################################
G.add_edge(1, 9, weight=-15)
G.add_edge(2, 9, weight=-14)
G.add_edge(3, 9, weight=-6)
G.add_edge(4, 9, weight=-6)
G.add_edge(5, 9, weight=-10)
# ####################################
G.add_edge(1, 10, weight=-4)
G.add_edge(2, 10, weight=-10)
G.add_edge(3, 10, weight=-7)
G.add_edge(4, 10, weight=-10)
G.add_edge(5, 10, weight=-6)
# ####################################
atribuicao = nx.max_weight_matching(G, maxcardinality=True)
for i in atribuicao:
    print i, "->", atribuicao[i]
