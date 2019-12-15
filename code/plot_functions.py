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

    node_info = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/Data/Node_List.csv')

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

    data1 = pd.merge(data1, node_info, how = 'inner', left_on = 'NodeID', right_on = 'ID')
    data2 = pd.merge(data2, node_info, how = 'inner', left_on = 'NodeID', right_on = 'ID')
    data3 = pd.merge(data3, node_info, how = 'inner', left_on = 'NodeID', right_on = 'ID')
    data4 = pd.merge(data4, node_info, how = 'inner', left_on = 'NodeID', right_on = 'ID')
    data5 = pd.merge(data5, node_info, how = 'inner', left_on = 'NodeID', right_on = 'ID')
    data6 = pd.merge(data6, node_info, how = 'inner', left_on = 'NodeID', right_on = 'ID')
    data7 = pd.merge(data7, node_info, how = 'inner', left_on = 'NodeID', right_on = 'ID')
    data8 = pd.merge(data8, node_info, how = 'inner', left_on = 'NodeID', right_on = 'ID')
    data9 = pd.merge(data9, node_info, how = 'inner', left_on = 'NodeID', right_on = 'ID')
    data10 = pd.merge(data10, node_info, how = 'inner', left_on = 'NodeID', right_on = 'ID')
    data11 = pd.merge(data11, node_info, how = 'inner', left_on = 'NodeID', right_on = 'ID')
    data12 = pd.merge(data12, node_info, how = 'inner', left_on = 'NodeID', right_on = 'ID')


    all_data = pd.concat([data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12])

    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September','October','November','December']

    layers = ['Algorithm', 'Physical', 'Task', 'Function', 'Information']

    input_dropdown = alt.binding_select(options=months)
    selection = alt.selection_single(fields=['month'], bind=input_dropdown, name = 'Month')

    layer_dropdown = alt.binding_select(options = layers)
    layer_selection = alt.selection_single(fields=['Layer'], bind=layer_dropdown, name = 'Layer')



    cn = alt.Chart(all_data).mark_bar().encode(
        x = alt.X('Cn:Q', bin = alt.Bin(maxbins=20), title = 'Connectedness Rating'),
        y = alt.Y('count()', title = 'Number of Nodes'),
        color = alt.value('#4e79a7')
    ).add_selection(
        selection
    ).transform_filter(
        selection
    ).add_selection(
        layer_selection
    ).transform_filter(
        layer_selection
    )


    rn = alt.Chart(all_data).mark_bar().encode(
        x = alt.X('Rn:Q', bin = alt.Bin(maxbins=20), title = 'Reliability Rating'),
        y = alt.Y('count()', title = 'Number of Nodes'),
        color = alt.value('#f28e2b')
    ).add_selection(
        selection
    ).transform_filter(
        selection
    ).add_selection(
        layer_selection
    ).transform_filter(
        layer_selection
    )

    id = alt.Chart(all_data).mark_bar().encode(
        x = alt.X('Id:Q', bin = alt.Bin(maxbins=20), title = 'Interdependency Rating'),
        y = alt.Y('count()', title = 'Number of Nodes'),
        color = alt.value('#e15759')
    ).add_selection(
        selection
    ).transform_filter(
        selection
    ).add_selection(
        layer_selection
    ).transform_filter(
        layer_selection
    )


    chart = alt.hconcat(cn,rn,id)
    #(cn | rn | id)
    chart.serve()
    return

def plot_summary_stats():
    summary_rev = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/summary_data_rev.csv')

    # Nearest Selection
    nearest = alt.selection(type='single', nearest=True, on='mouseover', fields = ['Date'], empty='none');

    # Transparent selectors across the chart. This is what tells us
    # the x-value of the cursor
    selectors = alt.Chart(summary_rev).mark_point().encode(
        x='Date:T',
        opacity=alt.value(0),
    ).add_selection(
        nearest
    )

    # Line on selection
    vLine = alt.Chart(summary_rev).mark_rule(strokeDash = [5, 5],opacity=0.6).encode(
        x='Date:T',
    ).transform_filter(
        nearest
    )

    # Data
    Line = alt.Chart(summary_rev).mark_line().encode(
        x = alt.X('Date:T',title='Date'),
        y = alt.Y('Value:Q',title='Mean Metric Value'),
        color = alt.Color('Metric:N')
    )

    Val = alt.Chart(summary_rev).mark_text(align='left', baseline = 'top',dx=5, dy=-25, color = 'Black').encode(
        text = alt.condition(nearest, 'Value:Q', alt.value(''),format = '1.3f'),
        x = alt.X('Date:T'),
        y = alt.Y('Value:Q')
    )


    # Draw points on the line, and highlight based on selection
    Points = alt.Chart(summary_rev).mark_circle().encode(
        x = alt.X('Date:T'),
        y = alt.Y('Value:Q'),
        opacity=alt.condition(nearest, alt.value(1), alt.value(0)),
        color = alt.Color('Metric:N')
    )




    viz2 = alt.layer(Line, selectors, vLine, Val, Points).properties(width=700)

    viz2.configure_legend(
        orient = 'right',
    )

    viz2.serve()

def plot_normalization_comparison():
    normalized = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/id_normalized.csv',names = ['NodeID','id'])
    not_normal = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/id_not_normalized.csv',names = ['NodeID','id'])

    # normalization = pd.DataFrame()
    # normalization['NodeID'] = normalized['NodeID']
    # normalization['normal'] = normalized['id']
    # normalization['not_normal'] = not_normal['id']

    # normalization

    normalized['normal'] = 1
    not_normal['normal'] = 0

    norm2 = pd.concat([normalized, not_normal])

    radial_input = alt.binding_radio(options=[1,0])
    norm_choice = alt.selection_single(fields=['normal'], bind=radial_input, name = 'Normalized?')

    norm_comparison = alt.Chart(norm2).mark_bar().encode(
        x = alt.X('id:Q', bin = alt.Bin(maxbins=20), title = 'Interdependency Rating'),
        y = alt.Y('count()', title = 'Number of Nodes')
    ).add_selection(
        norm_choice
    ).transform_filter(
        norm_choice
    ).transform_filter(
        alt.datum.NodeID != 64
    )

    norm_comparison.serve()
