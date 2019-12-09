"""
Graph Calculation Functions
"""
import networkx as nx
import pandas as pd
import numpy as np
import scipy as sp

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

# def calc_reliability(G):
#     Rn = {}
#
#     N = G.number_of_nodes()
#
#     A = nx.adjacency_matrix(G) # produces csr sparse matrix
#     # print(sp.sparse.isspmatrix_csr(A)) # true
#
#     # print(A.todense())
#
#     # Find Max Depth
#     # max_depth = nx.algorithms.distance_measures.diameter(G) # wamv Network
#     # max_depth = nx.dag_longest_path_length(G) # simple network
#     max_depth = 2
#     print(max_depth)
#
#     # Create matrix to find all connections
#     C = A
#     B = A
#     for r in range (2,max_depth+1):
#         C = C*A
#         B += C
#     B += sp.sparse.identity(B.shape[0]) # ensure it counts itself
#
#     # Now, B is a matrix where 1 indicates a connection from i to j
#     # Within a row i, nodes at col j with 0 exist when node i is removed
#
#     row = 0
#     for node in G.nodes():
#         rating = 0
#         for col in range(B.shape[0]):
#             if B[row,col] < 1:
#                 rating += 1
#         Rn[node] = rating
#         row += 1
#
#     print(B.todense())
#
#     np.savetxt("A.csv", A.todense(), delimiter=",")
#     np.savetxt("B.csv", B.todense(), delimiter=",")
#
#     return Rn
