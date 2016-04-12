#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 01:20:46 2016

@author: caioau
"""

import matplotlib.pyplot as plt
import networkx as nx

def main():
    G = nx.DiGraph() # G eh um grafo direcionado
    # gera o grafo apartir de suas arestas 
    G.add_weighted_edges_from([(1,2,13.0),(1,3,8.0),(1,5,33.0),(2,3,22.0),(2,4,17.0),(2,6,20.0),(3,5,18.0),(4,5,10.0),(4,6,5.0),(5,6,15.0)])
    
    desenhaGrafo(G,"grafo-c.png")
    T = nx.minimum_spanning_tree(nx.to_networkx_graph(G))
    desenhaGrafo(T,"arv-min-c.png")


def desenhaGrafo(G,pngfilename): # desenha o grafo e salva numa imagem png
    edge_labels=dict([((u,v,),d['weight']) # gera os labels das arestas
                    for u,v,d in G.edges(data=True)])
    pos = nx.fruchterman_reingold_layout(G,weight=None) # obtem a posicao dos nos (para desenhalo) # TODO: desativar isso?
    nx.draw_networkx_edges(G,pos) # desenha as arestas
    nx.draw_networkx_labels(G,pos) # desenha os labels das arestas
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels) # desenha os labels dos nos
    nx.draw_networkx_nodes(G,pos,node_color='w') # desenha os nos
    plt.axis('off') # desativa os eixos
    plt.savefig(pngfilename)
    plt.close("all")

if __name__ == "__main__":
    main()