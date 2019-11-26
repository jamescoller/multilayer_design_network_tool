"""
Created on Tue Mar 26 2019

PRADS 2019 Code

@author: jcoller
"""

# Do float division
from __future__ import division

# Imports
# matplotlib.use('TkAgg')

import networkx as nx
import time
import graphviz as gv
import networkx.drawing
# from networkx.drawing.nx_pydot import grahviz_layout
# from graphviz import Digraph
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout
import random
import csv
# import pylab as plt
# import random
# import scipy
import numpy as np


# Setup Base Network

#whole = gv.Digraph(comment='Launch and Recovery Infulence Diagram',format ='png',engine = 'dot')

 # Read in as Pandas data frame then read into networkx from that

# Read in Adjacency Lists
G = nx.Graph()
G=nx.read_adjlist("Data/Adjacency_Lists/All.csv")


G.nodes()
#G.edges()


plt.figure(figsize=(8,8))
nx.draw_random(G)
plt.show()
