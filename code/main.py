"""
Oceans 2020 Code

@author: jcoller
"""
import datetime as dt
import pandas as pd

from Calculations import *
from plot_functions import *
from Read_Nodes import read_node_list
from create_graph import create_network
from run_functions import run_single_timestep

# Create the Network Structure
adjlist = "Data/Adjacency_Lists/All.txt"
node_list = "Data/Node_List.csv"

G = create_network(adjlist, node_list)

# Determine Metrics
# Cn = calc_connectedness(G)
# Id = calc_interdependency(G)
# Rn = calc_reliability(G)

# Save Metrics to csv
# save_metric_to_csv(Cn,'results/cn.csv')
# save_metric_to_csv(Id,'results/id.csv')
# save_metric_to_csv(Rn,'results/rn.csv')


# Plot Metrics
# plot_connectedness(Cn, G, num_bins = 20)
# plot_interdependency(Id,G,num_bins = 20)
# plot_reliability(Rn,G,num_bins=20)
# plt.show()

# Run over time
# dates = ['2018-01-01','2018-02-01','2018-03-01','2018-04-01', '2018-05-01', '2018-06-01','2018-07-01','2018-08-01','2018-09-01','2018-10-01','2018-11-01','2018-12-01']
#
# summary = pd.DataFrame({'Date':[], 'Cn':[], 'Id':[], 'Rn':[]})
#
# for date in dates:
#     data = run_single_timestep(G,dt.date.fromisoformat(date))
#     summary = pd.concat([summary, data])
#
# summary.to_csv('results/summary_data.csv',index=False)

plot_interactive_histograms_sm()
#
# print(summary)
