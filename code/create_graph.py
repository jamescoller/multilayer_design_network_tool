"""
Function to read in and create NetworkX Graph
"""

import networkx as nx
import csv
import pandas as pd

def create_network(adjacency_list, node_list):

    G = nx.DiGraph()
    E = nx.DiGraph()

    # Read in the Edge List
    E = nx.read_adjlist(adjacency_list, create_using=nx.DiGraph())

    # Read node list into Pandas dataframe
    nodes = pd.read_csv(node_list)

    # Iterate over all of the rows of the node list and add the node
    for i,row in nodes.iterrows():
        G.add_node(str(nodes.ID[i]),label = nodes.Label[i], start_date = nodes.StartDate[i], layer = nodes.Layer[i], importance = nodes.Importance[i])

    # adjlist reads in the nodeids as strings, as does the snippet below, while add_node added them as ints. The solution was to make the add_node make the nodeid a string upon creation so the two could be merged.

    # Now, read in the edge list, line by line, and add the edges
    # with open(adjacency_list) as csvfile:
    #     readCSV = csv.reader(csvfile, delimiter=',')
    #     for row in readCSV:
    #         num_edges = len(row)
    #         if num_edges > 1:
    #             for i in range(1,num_edges-1):
    #                 E.add_edge(row[0],row[i])

    # print(list(G.nodes(data=False)))
    # print(list(E.nodes(data=False)))
    # print(G.number_of_nodes())
    G.update(E.edges())
    # print(G.number_of_nodes())
    return G
