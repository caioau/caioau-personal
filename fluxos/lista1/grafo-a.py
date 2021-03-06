#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 01:20:46 2016

@author: caioau
"""

import matplotlib.pyplot as plt
import networkx as nx


def main():
    G = nx.Graph()  # G eh um grafo direcionado
    # gera o grafo apartir de suas arestas
    G.add_weighted_edges_from([(1, 2, 2.0), (1, 3, 2.0), (1, 4, 3.0), (2, 5, 5.0), (3, 2, 4.0), (3, 5, 3.0), (4, 3, 1.0), (4, 5, 0.0)])
    desenhaGrafo(G, "grafo-a.png")
    T = nx.minimum_spanning_tree(G)
    desenhaGrafo(T, "arv-min-a.png")


def desenhaGrafo(G, pngfilename):  # desenha o grafo e salva numa imagem png
    edge_labels = dict([((u, v,), d['weight'])  # gera os labels das arestas
                                                for u, v, d in G.edges(data=True)])
    pos = nx.spectral_layout(G, weight=None)  # obtem a posicao dos nos (para desenhalo) # TODO: desativar isso?
    nx.draw_networkx_edges(G, pos)  # desenha as arestas
    nx.draw_networkx_labels(G, pos)  # desenha os labels das arestas
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)  # desenha os labels dos nos
    nx.draw_networkx_nodes(G, pos, node_color='w')  # desenha os nos
    plt.axis('off')  # desativa os eixos
    plt.savefig(pngfilename)
    plt.close("all")

if __name__ == "__main__":
    main()
