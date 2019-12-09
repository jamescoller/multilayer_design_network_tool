"""
Run for one time step
"""

import datetime as dt
from Calculations import *
from plot_functions import *
from Read_Nodes import read_node_list
from create_graph import create_network

def run_single_timestep(G,max_date):
    # Max date: dt.date.fromisoformat('2019-12-20')

    # Make a copy of the network
    C = G.copy()

    # Remove nodes in C that are after the max_date
    for node in G.nodes():
        if C.nodes[str(node)]['start_date'] > max_date:
            C.remove_node(str(node))

    print(C.number_of_nodes())

    # Now calculate metrics
    Cn = calc_connectedness(C)
    Id = calc_interdependency(C)
    Rn = calc_reliability(C)

    # Save Metrics to csv
    save_metric_to_csv(Cn,'results/cn'+max_date.isoformat()+'.csv')
    save_metric_to_csv(Id,'results/id'+max_date.isoformat()+'.csv')
    save_metric_to_csv(Rn,'results/rn'+max_date.isoformat()+'.csv')

    # Convert dicts to pandas dataframe
    Cn_data = pd.DataFrame.from_dict(Cn, orient = 'index', columns = ['Cn'])
    Id_data = pd.DataFrame.from_dict(Id, orient = 'index', columns = ['Id'])
    Rn_data = pd.DataFrame.from_dict(Rn, orient = 'index', columns = ['Rn'])

    frames = [Cn_data, Id_data, Rn_data]
    all_data = pd.merge(Cn_data, Id_data,left_index=True,right_index=True)

    all_data = pd.merge(all_data,Rn_data,left_index=True,right_index=True)

    all_data.to_csv('results/all_data'+max_date.isoformat()+'.csv',index=True, index_label = 'NodeID')

    # Find aggregate measures
    agg = all_data.mean()

    # Reformat
    summary = {'Date': [max_date.isoformat()], 'Cn': [agg['Cn']], 'Id': [agg['Id']], 'Rn': [agg['Rn']]}

    return pd.DataFrame.from_dict(summary)
