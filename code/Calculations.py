"""
Graph Calculation Functions
"""
import networkx as nx
import pandas as pd
import numpy as np
import scipy as sp

def calc_connectedness(G):

    inter_layer = {}
    intra_layer = {}

    for i in G.nodes():
        inter = 0
        intra = 0
        layer = G.nodes[str(i)]['layer']

        suc = G.successors(i)
        pred = G.predecessors(i)

        for n in suc:
            # Check if the layer is the same
            if G.nodes[str(n)]['layer'] == G.nodes[str(i)]['layer']:
                intra += 1
            else:
                inter += 1

        for n in pred:
            # Check if the layer is the same
            if G.nodes[str(n)]['layer'] == G.nodes[str(i)]['layer']:
                intra += 1
            else:
                inter += 1

        inter_layer[i] = inter
        intra_layer[i] = intra

    nodes = nx.nodes(G)
    n = nx.number_of_nodes(G)

    alpha = 1
    beta = 1

    Cn = {}

    for i in nodes:
        val = intra_layer[i]*alpha + inter_layer[i]*beta
        Cn[i] = val

    return Cn

def calc_interdependency(G):

    # Betweenness Centrality
    bc = nx.betweenness_centrality(G,normalized = False)

    return bc

def calc_reliability(G):
    Rn = {}
    N = G.number_of_nodes()

    for node in G.nodes():
        # Make a Copy
        C = G.copy()

        R = 0

        # Find descendants of nodes
        failed = nx.descendants(C,node)

        # Remove Failed Nodes
        for failure in failed:
            failed_node = str(failure)
            C.remove_node(failed_node)

        # Count Importance of Ramining nodes
        for remaining in C.nodes():
            R += C.nodes[str(remaining)]['importance']

        Rn[node] = R

    return Rn
