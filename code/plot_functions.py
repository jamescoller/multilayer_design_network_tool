"""
Graph Calculation Functions
"""
import networkx as nx
import time
import graphviz as gv
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

def plot_connectedness(dict, graph, num_bins = 10, width_bins = 0.8):

    # Get List of Values
    vals = dict.values()
    vals2 = list(vals)

    # multiply vals by number of nodes
    num_nodes = nx.number_of_nodes(graph)

    for i in range(len(vals)):
        vals2[i] = vals2[i]*num_nodes

    # Plot a histogram of the values
    plt.title("Connectedness Histogram")
    plt.xlabel("Connectedness Rating")
    plt.ylabel("Number of Nodes")
    plt.hist(vals2, bins=num_bins,rwidth=width_bins)
    plt.savefig('Figures/connectedness_histogram.png')
    plt.show()

def plot_interdependency(dict, graph, num_bins = 10, width_bins = 0.8):

    # Get List of Values
    vals = dict.values()
    vals2 = list(vals)

    # multiply vals by number of nodes
    num_nodes = nx.number_of_nodes(graph)

    for i in range(len(vals)):
        vals2[i] = vals2[i]*num_nodes

    # Plot a histogram of the values
    plt.title("Interdependency Histogram")
    plt.xlabel("Betweenness Centrality")
    plt.ylabel("Number of Nodes")
    plt.hist(vals2, bins=num_bins,rwidth=width_bins)
    plt.savefig('Figures/interdependency_histogram.png')
    plt.show()
