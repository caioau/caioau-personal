#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import networkx as nx

G = nx.DiGraph()
# Adiciona os arcos
G.add_edge(1, 4, weight=-2)
G.add_edge(2, 4, weight=-1)
G.add_edge(3, 4, weight=-1)
# ###################################
G.add_edge(1, 5, weight=-1)
G.add_edge(2, 5, weight=-3)
G.add_edge(3, 5, weight=-2)
# ###################################
G.add_edge(1, 6, weight=0)
G.add_edge(2, 6, weight=-4)
G.add_edge(3, 6, weight=-6)
# ####################################
atribuicao = nx.max_weight_matching(G, maxcardinality=True)
for i in atribuicao:
    print i, "->", atribuicao[i]
