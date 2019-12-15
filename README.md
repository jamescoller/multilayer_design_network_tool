# multilayer_design_network_tool

## Setup
1. Prepare node list and adjacency list, following templates Data/Node_List.csv and Data/Adjacency_Lists/All.csv
2. Download [Gephi](https://gephi.org/)
3. Load all [dependencies](##dependencies "Goto dependencies") for the python scripts.
3. Load the network into Gephi.
  * If using sample network, the file is Gephi/five_layer_map_v1.gephi. This will allow you to visualize the five layers distinctly and will be interactive to show the multiple layers and node interconnectivity.
  * If using your own network, Gephi is a powerful tool and you can load in the node list and adjacency list using the import excel sheet tool in the Data Dashboard.
4. Open the python code code/main.py and load the adjlist and node_list at the top to your files from step 1.
5. Run the code as shown below.

## Running the Code
to run the analysis: `python3 code/main.py`

to run the dashboard: `python3 code/dashboard.py`

to open the dashboard once it is running, open a web browser and open the page: http://127.0.0.1:8050/

## Dependencies
* python3
* networkx
* csv
* pandas
* numpy
* scipy
* matplotlib
* dash
* plotly
* datetime
* copy
* altair
* vegascope
