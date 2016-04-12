# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 21:36:04 2016

@author: caioau
"""

import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph() # G eh um grafo direcionado

G.add_weighted_edges_from([(1,2,2.0),(1,3,2.0),(1,4,3.0),(2,5,5.0),(3,2,4.0),(3,5,3.0),(4,3,1.0),(4,5,0.0)])

edge_labels=dict([((u,v,),d['weight']) # gera os labels das arestas
                 for u,v,d in G.edges(data=True)])
pos = nx.spectral_layout(G,weight=None) # obtem a posicao dos nos (para desenhalo)
#nx.draw_spectral(G)
nx.draw_networkx_edges(G,pos) # desenha as arestas
nx.draw_networkx_labels(G,pos) # desenha os labels das arestas
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels) # desenha os labels dos nos
nx.draw_networkx_nodes(G,pos,node_color='w') # desenha os nos
plt.axis('off') # desativa os eixos
plt.savefig("grafo-a.png")
plt.close("all")
H = nx.to_networkx_graph(G)
T = nx.minimum_spanning_tree(H)

edge_labels=dict([((u,v,),d['weight'])
                 for u,v,d in T.edges(data=True)])

pos = nx.spectral_layout(T,weight=None)
nx.draw_networkx_edges(T,pos)
nx.draw_networkx_labels(T,pos)
nx.draw_networkx_edge_labels(T,pos,edge_labels=edge_labels)
nx.draw_networkx_nodes(T,pos,node_color='w')
plt.axis('off')
plt.savefig("arv-min-a.png")
#print list(nx.simple_cycles(G))
