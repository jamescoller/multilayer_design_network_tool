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

from dashboard_help import *

# Import DataFrame
time_summary = pd.read_csv('results/summary_data.csv')

all_data = load_data()

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September','October','November','December']

layers = ['Algorithm', 'Physical', 'Task', 'Function', 'Information']

# Setup Dash
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__)

# Create the webpage layout
app.layout = html.Div(
    [
        # Header
        html.Div(
            [
                html.Div(
                    [
                        html.Img(
                            # src='https://drive.google.com/file/d/1JMGLKFt-u_z5O-M2GDsntihJ315qVR7G/view?usp=sharing',
                            src = 'https://lh4.googleusercontent.com/Sbg8KyREFkVD0WHpavEpdf7bvfc8gLdU7b1k-QACq4hni8XRyPt6lIIxqPjJU7_dUojqzDUfrFjXTcB--57eCCo6a-GpGUgXVsdpFUYX3rpZoUtkeA=w170',
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
                            # href="https://sites.google.com/umich.edu/si649-design-complexity/home",
                            href = 'https://drive.google.com/file/d/1ihuatCAwifl7Gs0lt7FskYtSK3v4xpma/view?usp=sharing',
                        ),
                        # html.A(
                        #     html.Button("Github", id="git-button"),
                        #     href = 'https://github.com/jamescoller/multilayer_design_network_tool/',
                        # )
                    ],
                    className="one-third column",
                    id="button",
                ),
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "25px"},
        ),
        # Filters, Summary, and Overview
        html.Div(
            [
                html.Div(
                    [
                        dcc.Markdown('''
                        ###### Overview

                        This full web page is interactive. You can zoom pan, hover over data points, filter, and discover more insights from the data.

                        The top level of graphs provide a system overview. These graphs represent the trend of the design over time and do not change with the time filters.

                        Below them, the three histograms will change with the filters and options from the panel to the right. They represent the distribution within the design of the various metrics.

                        Additional plots at the bottom allow comparing individual elements of the design and the layers amongst one another.

                        For more information on the metrics, click on the *Learn More* button above.
                        ''')
                    ],
                    className="pretty_container four columns",
                    id="basic-options",
                ),
                html.Div(
                    [
                        html.H6(
                            "Filters and Options",
                            style={"margin-top": "0px"}
                        ),
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
                    className="pretty_container",
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
                                className="row flex-display",
                            ),
                    ],
                    id="right-column",
                    className="four columns",
                ),
            ],
            className="row flex-display",
        ),
        # Node counts
        html.Div(
        [
            html.Div(
                [
                dcc.Graph(id="node_count_fig")
                ],
                id="countGraphContainer",
                className="pretty_container three columns",
            ),
            html.Div(
                [dcc.Graph(id="avg_metrics_fig")],
                className="pretty_container five columns",
            ),
        ],
        className="row flex-display",
        ),
        # Histograms
        html.Div(
            [
                    html.Div(
                        [dcc.Graph(id="cn_histogram")],
                        className="pretty_container five columns",
                    ),
                    html.Div(
                        [dcc.Graph(id="rn_histogram")],
                        className="pretty_container five columns",
                    ),
                    html.Div(
                        [dcc.Graph(id="id_histogram")],
                        className="pretty_container five columns",
                    ),
            ],
            className="row flex-display",
        ),
        html.Div(
        [
            html.Div(
                [dcc.Graph(id="radar")],
                className = "pretty_container",
            )
        ]
        ),
        html.Div(
        [
            html.Div(
                [dcc.Graph(id="cn_ranking")],
                className="pretty_container",
            ),
        ]
        ),
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
    fig.update_layout(
    yaxis=dict(
        showgrid=True,
        gridcolor='grey',
        zeroline=True,
        zerolinecolor='grey'
    ),
    xaxis=dict(
        showgrid=False,
        gridcolor='grey',
        zeroline=True,
        zerolinecolor='grey'
    ),
    title=dict(
        text = 'Metric by Node'
    ),
    plot_bgcolor='white'
    )
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

# Radar Chart
@app.callback(
    Output('radar', 'figure'),
    [
        Input('month_dropdown', 'value'),
        Input('layer_dropdown', 'value'),
        Input('normalize_button', 'value')
    ])
def create_radar_chart(selected_month, selected_layer, norm):
    df = filter_df(all_data, selected_month, selected_layer, norm)
    fig = go.Figure()
    categories = ['Adaptability','Connectivity', 'Interconnectedness']
    # All
    agg_all = df.mean()
    fig.add_trace(go.Scatterpolar(
        r = [agg_all["Rn"], agg_all["Cn"], agg_all["Id"]],
        theta = categories,
        fill = 'toself',
        name = 'All Layers'
    ))
    # Function Layer
    agg_func = df[df['Layer'].isin(['Function'])].mean()
    fig.add_trace(go.Scatterpolar(
        r = [agg_func["Rn"], agg_func["Cn"], agg_func["Id"]],
        theta = categories,
        fill = 'toself',
        name = 'Function'
    ))
    # Task Layer
    agg_task = df[df['Layer'].isin(['Task'])].mean()
    fig.add_trace(go.Scatterpolar(
        r = [agg_task["Rn"], agg_task["Cn"], agg_task["Id"]],
        theta = categories,
        fill = 'toself',
        name = 'Task'
    ))
    # Alg Layer
    agg_alg = df[df['Layer'].isin(['Algorithm'])].mean()
    fig.add_trace(go.Scatterpolar(
        r = [agg_alg["Rn"], agg_alg["Cn"], agg_alg["Id"]],
        theta = categories,
        fill = 'toself',
        name = 'Algorithm'
    ))
    # Info Layer
    agg_info = df[df['Layer'].isin(['Information'])].mean()
    fig.add_trace(go.Scatterpolar(
        r = [agg_info["Rn"], agg_info["Cn"], agg_info["Id"]],
        theta = categories,
        fill = 'toself',
        name = 'Information'
    ))
    # Physical Layer
    agg_phys = df[df['Layer'].isin(['Physical'])].mean()
    fig.add_trace(go.Scatterpolar(
        r = [agg_phys["Rn"], agg_phys["Cn"], agg_phys["Id"]],
        theta = categories,
        fill = 'toself',
        name = 'Physical'
    ))
    fig.update_layout(
        polar=dict(
        radialaxis=dict(
          visible=True,
          # range=[0, 5]
        )),
        showlegend=True
    )
    return fig

# Delta Indicators - Works indpendently, can't get it to render in dash
# @app.callback(
#     Output("d_nodes", "figure"),
#     [
#         Input('month_dropdown', 'value'),
#         Input('layer_dropdown', 'value'),
#         Input('normalize_button', 'value')
#     ])
# def update_deltas(selected_month, selected_layer, norm):
#     filtered_df = filter_df(all_data, 'December', '', 0)
#     fig = go.Figure()
#     fig.add_trace(go.Indicator(
#         mode = "number+delta",
#         value = filtered_df.shape[0],
#         delta = {"reference": 0, "valueformat": ".0f", 'relative': True},
#         title = {"text": "Number of Nodes"},
#     ))
#     return fig

# Allow to run from main
def launch_dashboard():
    app.run_server(debug=True)

# Allow to run locally
if __name__ == '__main__':
    app.run_server(debug=True)
