#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import networkx as nx

G = nx.DiGraph()
# Adiciona os arcos
G.add_edge(1, 5, weight=-5)
G.add_edge(2, 5, weight=-10)
G.add_edge(3, 5, weight=-28)
G.add_edge(4, 5, weight=-10)
# ###################################
G.add_edge(1, 6, weight=-24)
G.add_edge(2, 6, weight=-25)
G.add_edge(3, 6, weight=-9)
G.add_edge(4, 6, weight=-17)
# ###################################
G.add_edge(1, 7, weight=-13)
G.add_edge(2, 7, weight=-3)
G.add_edge(3, 7, weight=-8)
G.add_edge(4, 7, weight=-15)
# ####################################
G.add_edge(1, 8, weight=-7)
G.add_edge(2, 8, weight=-23)
G.add_edge(3, 8, weight=-5)
G.add_edge(4, 8, weight=-3)
# ####################################
atribuicao = nx.max_weight_matching(G, maxcardinality=True)
for i in atribuicao:
    print i, "->", atribuicao[i]
