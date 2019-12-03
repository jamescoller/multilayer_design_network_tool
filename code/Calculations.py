"""
Graph Calculation Functions
"""
import networkx as nx
import time
import graphviz as gv
import pandas as pd
import numpy as np

def calc_connectedness(G):

    # In and Out Degree are normalized by 1/n
    in_deg = nx.in_degree_centrality(G) # returns a dict
    out_deg = nx.out_degree_centrality(G) # returns a dict
    nodes = nx.nodes(G)
    n = nx.number_of_nodes(G)

    alpha = 1
    beta = 1

    Cn = {}

    for i in nodes:
        val = in_deg[i]*alpha + out_deg[i]*beta
        Cn[i] = val

    return Cn

def calc_interdependency(G):

    # Betweenness Centrality
    bc = nx.betweenness_centrality(G,normalized = True)

    return bc
