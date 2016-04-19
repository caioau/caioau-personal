#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 01:20:46 2016

@author: caioau
"""

import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout

def main():
    G = nx.DiGraph()  # G eh um grafo direcionado
    # gera o grafo apartir de suas arestas
    G.add_weighted_edges_from([(1,2,2.0),(1,3,1.0),(2,3,3.0),(2,4,3.0),(3,5,1.0),(4,6,2.0),(5,4,2.0),(5,6,5.0)])
    for i in G.edges():
        # print i[0], i[1]
        G[i[0]][i[1]]["color"] = "black"
    # G[1][2]["color"] = "red"
    comprimento, caminho = nx.single_source_dijkstra(G, 1)
    print caminho
    for i in caminho:
        print i, comprimento[i], caminho[i]
        for j in range(1, len(caminho[i])):
            #print caminho[i][j-1], caminho[i][j]
            G[caminho[i][j-1]][caminho[i][j]]["color"] = "red"
    desenhaGrafo(G, "grafo-1c.png")


def desenhaGrafo(G,pngfilename): # desenha o grafo e salva numa imagem png
    edge_labels=dict([((u,v,),d['weight']) # gera os labels das arestas
                    for u,v,d in G.edges(data=True)])
    colors = [G[u][v]['color'] for u,v in G.edges()]
    pos = graphviz_layout(G,prog='neato') # obtem a posicao dos nos (para desenhalo) # TODO: desativar isso?
    nx.draw_networkx_edges(G,pos, edge_color=colors) # desenha as arestas
    nx.draw_networkx_labels(G,pos) # desenha os labels das arestas
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels) # desenha os labels dos nos
    nx.draw_networkx_nodes(G,pos,node_color='w') # desenha os nos
    plt.axis('off') # desativa os eixos
    plt.savefig(pngfilename)
    plt.close("all")

if __name__ == "__main__":
    main()
