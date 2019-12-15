"""
Interactive Dashboard Code
"""
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
# data1 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-01-01.csv')
# data2 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-02-01.csv')
# data3 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-03-01.csv')
# data4 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-04-01.csv')
# data5 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-05-01.csv')
# data6 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-06-01.csv')
# data7 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-07-01.csv')
# data8 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-08-01.csv')
# data9 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-09-01.csv')
# data10 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-10-01.csv')
# data11 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-11-01.csv')
# data12 = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/all_data2018-12-01.csv')

# node_info = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/Data/Node_List.csv')

# time_summary = pd.read_csv('https://raw.githubusercontent.com/jamescoller/multilayer_design_network_tool/master/results/summary_data.csv')

data1 = pd.read_csv('results/all_data2018-01-01.csv')
data2 = pd.read_csv('results/all_data2018-02-01.csv')
data3 = pd.read_csv('results/all_data2018-03-01.csv')
data4 = pd.read_csv('results/all_data2018-04-01.csv')
data5 = pd.read_csv('results/all_data2018-05-01.csv')
data6 = pd.read_csv('results/all_data2018-06-01.csv')
data7 = pd.read_csv('results/all_data2018-07-01.csv')
data8 = pd.read_csv('results/all_data2018-08-01.csv')
data9 = pd.read_csv('results/all_data2018-09-01.csv')
data10 = pd.read_csv('results/all_data2018-10-01.csv')
data11 = pd.read_csv('results/all_data2018-11-01.csv')
data12 = pd.read_csv('results/all_data2018-12-01.csv')

node_info = pd.read_csv('Data/Node_List.csv')

time_summary = pd.read_csv('results/summary_data.csv')

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

# Setup Dash
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__)

# Create the webpage layout
app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.Img(
                            src='https://lh4.googleusercontent.com/SCwcG08iaTmrYsOm0VARUhOTa8obNoui8bBggQ7CvRahrBw5RpFQPwOkAbjAE65RUaoJ8lhtq6ePcGRgfLJX3hNvGqKoDKsTgRuJTjg3H2vDy4_ylg=w170',
                            id="ancr_logo",
                            style={
                                "height": "100px",
                                "width": "auto",
                                "margin-bottom": "25px",
                            },
                        )
                    ],
                    className="one-third column",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H2(
                                    "Complexity Analysis Dashboard",
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H4(
                                    "System Complexity Overview", style={"margin-top": "0px"}
                                ),
                            ]
                        )
                    ],
                    className="one-half column",
                    id="title",
                ),
                html.Div(
                    [
                        html.A(
                            html.Button("Learn More", id="learn-more-button"),
                            href="https://sites.google.com/umich.edu/si649-design-complexity/home",
                        )
                    ],
                    className="one-third column",
                    id="button",
                ),
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "25px"},
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.P(
                            "Filter by element creation date:",
                            className="control_label",
                        ),
                        dcc.Dropdown(
                        id = 'month_dropdown',
                        options=[{"label": i, "value": i} for i in months],
                        value='December',
                        className="dcc_control",
                        ),
                        html.P(
                            "Filter by network layer:",
                            className="control_label",
                        ),
                        dcc.Dropdown(
                        id = 'layer_dropdown',
                        options=[{"label": i, "value": i} for i in layers],
                        className="dcc_control",
                        ),
                        html.P(
                            "Choose if metrics should be normalized:",
                            className="control_label",
                        ),
                        dcc.RadioItems(
                        id = 'normalize_button',
                        options=[
                            {'label':'Normalize Values','value': 1},
                            {'label': 'Normal Values', 'value': 0},
                            ],
                        value=1,
                        className="dcc_control",
                        )
                    ],
                    className="pretty_container four columns",
                    id="cross-filter-options",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [html.H6(id="number_of_nodes"), html.P("No. of Nodes")],
                                    id="nodes",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="Mean_Cn"), html.P("Mean Cn")],
                                    id="cn",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="Mean_Rn"), html.P("Mean Rn")],
                                    id="rn",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="Mean_Id"), html.P("Mean Id")],
                                    id="id",
                                    className="mini_container",
                                ),
                            ],
                            id="info-container",
                            className="row container-display",
                        ),
                        html.Div(
                            [
                            dcc.Graph(id="node_count_fig")
                            ],
                            id="countGraphContainer",
                            className="pretty_container",
                        ),
                    ],
                    id="right-column",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [html.P("")],
                    className="pretty_container six columns"
                ),
                html.Div(
                [
                    html.Div(
                        [dcc.Graph(id="cn_histogram")],
                        className="pretty_container",
                    ),
                    html.Div(
                        [dcc.Graph(id="rn_histogram")],
                        className="pretty_container",
                    ),
                    html.Div(
                        [dcc.Graph(id="id_histogram")],
                        className="pretty_container",
                    ),
                ]
                )
            ],
            className="row flex-display",
        ),
        html.Div(
        [
            html.Div(
                [dcc.Graph(id="avg_metrics_fig")],
                className="pretty_container",
            ),
        ]
        ),
        html.Div(
        [
            html.Div(
                [dcc.Graph(id="cn_ranking")],
                className="pretty_container",
            ),
        ]
        )
])

# Helper Functions
def filter_df(df, month, layer, norm):
    if not layer:
        filtered = df[
        df["month"].isin([month])
        ]
    else:
        filtered = df[
        df["month"].isin([month])
        & df["Layer"].isin([layer])
        ]
    if norm:
        filtered = normalize_data(filtered)
    return filtered

def normalize_data(df):
    df["Cn"] = (df["Cn"]-min(df["Cn"]))/(max(df["Cn"])-min(df["Cn"]))
    df["Rn"] = (df["Rn"]-min(df["Rn"]))/(max(df["Rn"])-min(df["Rn"]))
    df["Id"] = (df["Id"]-min(df["Id"]))/(max(df["Id"])-min(df["Id"]))
    return df

def remake_summary_file(df,norm):
    sdf = pd.DataFrame({'Date':[], 'Cn':[], 'Id':[], 'Rn':[]})
    for i in months:
        dff = filter_df(df, i, '', norm)
        agg = dff.mean()
        summary = {'Date': i, 'Cn': [agg['Cn']], 'Id': [agg['Id']], 'Rn': [agg['Rn']]}
        summary = pd.DataFrame.from_dict(summary)
        sdf = pd.concat([sdf, summary])
    return sdf



# Histograms
@app.callback(
    Output('cn_histogram', 'figure'),
    [
        Input('month_dropdown', 'value'),
        Input('layer_dropdown', 'value'),
        Input('normalize_button', 'value')
    ])
def cn_histogram(selected_month, selected_layer, norm):
    fig = go.Figure()
    filtered_df = filter_df(all_data, selected_month, selected_layer, norm)
    fig.add_trace(go.Histogram(x=filtered_df["Cn"].tolist(),marker_color='#4e79a7'))
    #,text=filtered_df["Label"].tolist() (from above)
    #cn_hist = px.histogram(filtered_df, x='Cn')
    fig.update_layout(
    yaxis=dict(
        title="count",
        showgrid=True,
        gridcolor='grey',
        zeroline=True,
        zerolinecolor='grey',
    ),
    xaxis=dict(
        title = "Connectivity Metric",
        showgrid=True,
        gridcolor='grey',
        zeroline=True,
        zerolinecolor='grey'
    ),
    plot_bgcolor='white',
    bargap=0.2, # gap between bars of adjacent location coordinates
    bargroupgap=0.1 # gap between bars of the same location coordinates
    )
    return fig

@app.callback(
    Output('rn_histogram', 'figure'),
    [
        Input('month_dropdown', 'value'),
        Input('layer_dropdown', 'value'),
        Input('normalize_button','value')
    ])
def rn_histogram(selected_month, selected_layer, norm):
    fig = go.Figure()
    filtered_df = filter_df(all_data, selected_month, selected_layer, norm)
    fig.add_trace(go.Histogram(x=filtered_df["Rn"].tolist(),marker_color='#f28e2b'))
    #cn_hist = px.histogram(filtered_df, x='Cn')
    fig.update_layout(
    yaxis=dict(
        title="count",
        showgrid=True,
        gridcolor='grey',
        zeroline=True,
        zerolinecolor='grey',
    ),
    xaxis=dict(
        title = "Reliability Metric",
        showgrid=True,
        gridcolor='grey',
        zeroline=True,
        zerolinecolor='grey'
    ),
    plot_bgcolor='white',
    bargap=0.2, # gap between bars of adjacent location coordinates
    bargroupgap=0.1 # gap between bars of the same location coordinates
    )
    return fig

@app.callback(
    Output('id_histogram', 'figure'),
    [
        Input('month_dropdown', 'value'),
        Input('layer_dropdown', 'value'),
        Input('normalize_button', 'value')
    ])
def id_histogram(selected_month, selected_layer, norm):
    fig = go.Figure()
    filtered_df = filter_df(all_data, selected_month, selected_layer, norm)
    fig.add_trace(go.Histogram(x=filtered_df["Id"].tolist(),marker_color='#e15759'))
    #cn_hist = px.histogram(filtered_df, x='Cn')
    fig.update_layout(
    yaxis=dict(
        title="count",
        showgrid=True,
        gridcolor='grey',
        zeroline=True,
        zerolinecolor='grey',
    ),
    xaxis=dict(
        title = "Interdependency Metric",
        showgrid=True,
        gridcolor='grey',
        zeroline=True,
        zerolinecolor='grey'
    ),
    plot_bgcolor='white',
    bargap=0.2, # gap between bars of adjacent location coordinates
    bargroupgap=0.1 # gap between bars of the same location coordinates
    )
    return fig


# Node Count By Date
@app.callback(
    Output('node_count_fig', 'figure'),
    [
        Input('month_dropdown', 'value'),
        Input('layer_dropdown', 'value')
    ])
def node_count_fig(selected_month, selected_layer):
    # Determine Counts
    counts = [{'month': i, 'count': filter_df(all_data, i,'',0).shape[0]} for i in months]
    df = pd.DataFrame(data = counts)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=months, y=df["count"].tolist(), mode='lines+markers'))
    # layout
    fig.update_layout(
    yaxis=dict(
        title="count",
        showgrid=True,
        gridcolor='grey',
        zeroline=True,
        zerolinecolor='grey'
    ),
    xaxis=dict(
        showgrid=True,
        gridcolor='grey',
        zeroline=True,
        zerolinecolor='grey'
    ),
    title=dict(
        text = 'Node Count by Month'
    ),
    plot_bgcolor='white'
    )
    # node_fig = px.line(df, x='month',y='count', line_shape = 'spline')
    return fig

# Average Metrics by Date
@app.callback(
    Output('avg_metrics_fig', 'figure'),
    [
        Input('month_dropdown', 'value'),
        Input('layer_dropdown', 'value'),
        Input('normalize_button', 'value')
    ])
def avg_metrics_fig(selected_month, selected_layer, norm):
    fig = go.Figure()
    if norm:
        df = remake_summary_file(all_data,norm)
    else:
        df = time_summary
    fig.add_trace(go.Scatter(
        x=df["Date"].tolist(),
        y=df["Cn"].tolist(),
        mode='lines+markers',
        marker_color='#4e79a7',
        name='Cn',
    ))
    fig.add_trace(go.Scatter(
        x=df["Date"].tolist(),
        y=df["Rn"].tolist(),
        mode='lines+markers',
        marker_color='#f28e2b',
        name='Rn',
    ))
    fig.add_trace(go.Scatter(
        x=df["Date"].tolist(),
        y=df["Id"].tolist(),
        mode='lines+markers',
        marker_color='#e15759',
        name='Id',
    ))
    # layout
    fig.update_layout(
    yaxis=dict(
        title="mean (metric)",
        showgrid=True,
        gridcolor='grey',
        zeroline=True,
        zerolinecolor='grey'
    ),
    xaxis=dict(
        showgrid=True,
        gridcolor='grey',
        zeroline=True,
        zerolinecolor='grey'
    ),
    title=dict(
        text = 'Complexity by Month'
    ),
    plot_bgcolor='white'
    )
    # node_fig = px.line(df, x='month',y='count', line_shape = 'spline')
    return fig

# Node Value List
@app.callback(
    Output('cn_ranking', 'figure'),
    [
        Input('month_dropdown', 'value'),
        Input('layer_dropdown', 'value'),
        Input('normalize_button', 'value')
    ])
def cn_ranking(selected_month, selected_layer, norm):
    df = filter_df(all_data, selected_month, selected_layer, norm)
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df["Label"].tolist(),
        y=df["Cn"].tolist(),
        name='Cn',
        marker_color='#4e79a7',
    ))
    fig.add_trace(go.Bar(
        x=df["Label"].tolist(),
        y=df["Rn"].tolist(),
        name='Rn',
        marker_color='#f28e2b',
    ))
    fig.add_trace(go.Bar(
        x=df["Label"].tolist(),
        y=df["Id"].tolist(),
        name='Id',
        marker_color='#e15759',
    ))
    fig.update_layout(xaxis={'categoryorder':'total descending'})
    return fig

# Text Update
@app.callback(
    [
        Output("number_of_nodes", "children"),
        Output("Mean_Cn", "children"),
        Output("Mean_Rn", "children"),
        Output("Mean_Id", "children")
    ],
    [
        Input('month_dropdown', 'value'),
        Input('layer_dropdown', 'value'),
        Input('normalize_button', 'value')
    ])
def update_node_text(selected_month, selected_layer, norm):
    filtered_df = filter_df(all_data, selected_month, selected_layer, norm)
    agg = filtered_df.mean()
    cn_mean = '%s' % float('%.3g' % agg['Cn'])
    rn_mean = '%s' % float('%.3g' % agg['Rn'])
    id_mean = '%s' % float('%.3g' % agg['Id'])
    return [filtered_df.shape[0], cn_mean, rn_mean, id_mean]




if __name__ == '__main__':
    app.run_server(debug=True)
