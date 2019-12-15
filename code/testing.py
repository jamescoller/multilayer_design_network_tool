import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import copy

# Import DataFrame
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

layout = dict(
    autosize=True,
    automargin=True,
    margin=dict(l=30, r=30, b=20, t=40),
    hovermode="closest",
    plot_bgcolor="#F9F9F9",
    paper_bgcolor="#F9F9F9",
    legend=dict(font=dict(size=10), orientation="h"),
    title="Satellite Overview",
)

# Helper Functions
def filter_df(df, month, layer):
    if not layer:
        filtered = df[
        df["month"].isin([month])
        ]
    else:
        filtered = df[
        df["month"].isin([month])
        & df["Layer"].isin([layer])
        ]
    return filtered

def node_count_fig():
    # Determine Counts
    counts = [{"month": i, "count": filter_df(all_data, i, '').shape[0]} for i in months]
    # counts = [
    #     "month": "January", filter_df(all_data, "January", '').shape[0],
    #     filter_df(all_data, "February", '').shape[0],
    #     filter_df(all_data, "March", '').shape[0],
    #     filter_df(all_data, "April", '').shape[0],
    #     filter_df(all_data, "May", '').shape[0],
    #     filter_df(all_data, "June", '').shape[0],
    #     filter_df(all_data, "July", '').shape[0],
    #     filter_df(all_data, "August", '').shape[0],
    #     filter_df(all_data, "September", '').shape[0],
    #     filter_df(all_data, "October", '').shape[0],
    #     filter_df(all_data, "November", '').shape[0],
    #     filter_df(all_data, "December", '').shape[0]
    # ]
    # Make Figure
    df = pd.DataFrame(data = counts)
    # fig = go.Figure()
    # fig.add_trace(go.Scatter(x=months, y=counts, mode='lines+markers'))
    # fig.show()
    fig = px.scatter(df, x='month',y='count')
    return fig

def node_count_fig2():
    # Determine Counts
    counts = [{'month': i, 'count': filter_df(all_data, i, '').shape[0]} for i in months]
    df = pd.DataFrame(data = counts)
    #
    layout_individual = copy.deepcopy(layout)
    #
    data = [
            dict(
                type="scatter",
                mode="lines+markers",
                name="Gas Produced (mcf)",
                x=df.month,
                y=df.count,
                line=dict(shape="spline", smoothing=2, width=1, color="#fac1b7"),
                marker=dict(symbol="diamond-open"),
            )
    ]
    layout_individual["title"] = "Something"
    figure = dict(data = data, layout = layout_individual)
    return figure


node_count_fig2().show()
