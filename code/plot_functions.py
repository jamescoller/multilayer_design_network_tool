"""
Graph Calculation Functions
"""
import networkx as nx
import matplotlib.pyplot as plt
import csv
import altair as alt
import pandas as pd
alt.renderers.enable('vegascope')


def plot_connectedness(dict, graph, num_bins = 10, width_bins = 0.8):

    # Get List of Values
    vals = dict.values()

    # Plot a histogram of the values
    plt.figure()
    plt.title("Connectedness Histogram")
    plt.xlabel("Connectedness Rating")
    plt.ylabel("Number of Nodes")
    plt.hist(vals, bins=num_bins,rwidth=width_bins)
    # plt.savefig('Figures/example_connectedness_histogram.png')
    # plt.show()

def plot_interdependency(dict, graph, num_bins = 10, width_bins = 0.8):

    # Get List of Values
    vals = dict.values()
    vals2 = list(vals)

    # multiply vals by number of nodes
    num_nodes = nx.number_of_nodes(graph)

    # for i in range(len(vals)):
    #     vals2[i] = vals2[i]*num_nodes

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

def plot_interactive_histograms_sm():
    # Load the Data
    data1 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-01-01.csv')
    data2 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-02-01.csv')
    data3 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-03-01.csv')
    data4 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-04-01.csv')
    data5 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-05-01.csv')
    data6 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-06-01.csv')
    data7 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-07-01.csv')
    data8 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-08-01.csv')
    data9 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-09-01.csv')
    data10 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-10-01.csv')
    data11 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-11-01.csv')
    data12 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-12-01.csv')

    time_summary = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/summary_data.csv')

    data1['month'] = 'January'
    data2['month'] = 'February'
    data3['month'] = 'March'
    data4['month'] = 'April'
    data5['month'] = 'May'
    data6['month'] = 'June'
    data7['month'] = 'July'
    data8['month'] = 'August'
    data9['month'] = 'September'
    data10['month'] = 'October'
    data11['month'] = 'November'
    data12['month'] = 'December'

    all_data = pd.concat([data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12])

    # Selection
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September','October','November','December']

    input_dropdown = alt.binding_select(options=months)
    selection = alt.selection_single(fields=['month'], bind=input_dropdown, name = 'Month')

    brush = alt.selection_interval()

    cn = alt.Chart(all_data).mark_bar().encode(
        x = alt.X('Cn:Q', bin = alt.Bin(maxbins=20), title = 'Connectedness Rating'),
        y = alt.Y('count()', title = 'Number of Nodes'),
        color = alt.value('#4e79a7')
    ).add_selection(
        selection
    ).transform_filter(
        selection
    )

    rn = alt.Chart(all_data).mark_bar().encode(
        x = alt.X('Rn:Q', bin = alt.Bin(maxbins=20), title = 'Reliability Rating'),
        y = alt.Y('count()', title = 'Number of Nodes'),
        color = alt.value('#f28e2b')
    ).add_selection(
        selection
    ).transform_filter(
        selection
    )

    id = alt.Chart(all_data).mark_bar().encode(
        x = alt.X('Id:Q', bin = alt.Bin(maxbins=20), title = 'Interdependency Rating'),
        y = alt.Y('count()', title = 'Number of Nodes'),
        color = alt.value('#e15759')
    ).add_selection(
        selection
    ).transform_filter(
        selection
    )

    chart = alt.hconcat(cn,rn,id)
    #(cn | rn | id)
    # chart.serve()
