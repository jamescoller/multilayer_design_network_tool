"""
Oceans 2020 Code

@author: jcoller
"""

# Do float division
from __future__ import division

# Imports
# matplotlib.use('TkAgg')

import networkx as nx
import graphviz as gv
import pandas as pd

import numpy as np
import collections

from Calculations import *
from plot_functions import *
from Read_Nodes import read_node_list

# Read in the Nodes
# G = read_node_list("Data/Node_List.csv")

# Read in the Edges
G = nx.read_adjlist("Data/Adjacency_Lists/All.txt", create_using=nx.DiGraph())

# Simple Example Graph
# G = nx.DiGraph()
# G.add_edge(1, 2)
# G.add_edge(1, 3)
# G.add_edge(2, 4)
# G.add_edge(2, 5)
# G.add_edge(3, 6)
# G.add_edge(3, 7)
# G.add_edge(6, 8)
# G.add_edge(6, 9)
# G.add_edge(7, 10)

# Determine Metrics
Cn = calc_connectedness(G)
Id = calc_interdependency(G)
Rn = calc_reliability(G)

# Save Metrics to csv
save_metric_to_csv(Cn,'results/cn.csv')
save_metric_to_csv(Id,'results/id.csv')
save_metric_to_csv(Rn,'results/rn.csv')

# Plot Metrics
plot_connectedness(Cn, G, num_bins = 20)
plot_interdependency(Id,G,num_bins = 20)
plot_reliability(Rn,G,num_bins=20)
plt.show()

#print(list(G.nodes(data=True)))
