"""
Functions to read in a node list from CSV to NetworkX Objects
"""

import pandas as pd
import networkx as nx

def read_node_list(filename):

    # Open CSV as Panads List
    nodes = pd.read_csv(filename)

    # Now loop
    G = nx.DiGraph()

    for i,row in nodes.iterrows():
        G.add_node(i,label = nodes.Label[i], start_date = nodes.StartDate[i], layer = nodes.Layer[i])

    return G
