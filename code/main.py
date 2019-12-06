"""
Oceans 2020 Code

@author: jcoller
"""
from Calculations import *
from plot_functions import *
from Read_Nodes import read_node_list
from create_graph import create_network

# Create the Network Structure
adjlist = "Data/Adjacency_Lists/All.txt"
node_list = "Data/Node_List.csv"

G = create_network(adjlist, node_list)

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
