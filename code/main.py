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
G = read_node_list("Data/Node_List.csv")

# Read in the Edges
G = nx.read_adjlist("Data/Adjacency_Lists/All.txt", create_using=nx.DiGraph())

# Determine Metrics
Cn = calc_connectedness(G)
Id = calc_interdependency(G)
print(Id)

# Plot Metrics
plot_connectedness(Cn, G, num_bins = 20)
plot_interdependency(Id,G,num_bins = 20)

print(list(G.nodes(data=True)))
