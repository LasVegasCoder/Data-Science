# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 07:58:44 2017

@author: Prince Adeyemi
"""

from scipy.stats import bernoulli

def er_graph(N, p):
    """Generage an ER Graph"""
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvp(p=p):
                G.add_edge(node1, node2)
                
    return G
