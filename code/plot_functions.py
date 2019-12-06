"""
Graph Calculation Functions
"""
import networkx as nx
import matplotlib.pyplot as plt
import csv


def plot_connectedness(dict, graph, num_bins = 10, width_bins = 0.8):

    # Get List of Values
    vals = dict.values()
    vals2 = list(vals)

    # multiply vals by number of nodes
    num_nodes = nx.number_of_nodes(graph)

    for i in range(len(vals)):
        vals2[i] = vals2[i]*num_nodes

    # Plot a histogram of the values
    plt.figure()
    plt.title("Connectedness Histogram")
    plt.xlabel("Connectedness Rating")
    plt.ylabel("Number of Nodes")
    plt.hist(vals2, bins=num_bins,rwidth=width_bins)
    # plt.savefig('Figures/example_connectedness_histogram.png')
    # plt.show()

def plot_interdependency(dict, graph, num_bins = 10, width_bins = 0.8):

    # Get List of Values
    vals = dict.values()
    vals2 = list(vals)

    # multiply vals by number of nodes
    num_nodes = nx.number_of_nodes(graph)

    for i in range(len(vals)):
        vals2[i] = vals2[i]*num_nodes

    # Plot a histogram of the values
    plt.figure()
    plt.title("Interdependency Histogram")
    plt.xlabel("Betweenness Centrality")
    plt.ylabel("Number of Nodes")
    plt.hist(vals2, bins=num_bins,rwidth=width_bins)
    # plt.savefig('Figures/example_interdependency_histogram.png')
    # plt.show()

def plot_reliability(dict, graph, num_bins = 10, width_bins = 0.8):

    # Get List of Values
    vals = dict.values()
    vals2 = list(vals)


    # Plot a histogram of the values
    plt.figure()
    plt.title("Reliability Histogram")
    plt.xlabel("Reliability")
    plt.ylabel("Number of Nodes")
    plt.hist(vals2, bins=num_bins,rwidth=width_bins)
    # plt.savefig('Figures/example_reliability_histogram.png')
    # plt.show()

def save_metric_to_csv(dict,filename):
    with open(filename, 'w') as f:
        for node in dict:
            f.write("%s,%f\n"%(node,dict[node]))
    return
