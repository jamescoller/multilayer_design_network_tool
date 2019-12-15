# Multilayer Network Design Visualization Tool

## Introduction
This is an analyst tool for examining design complexity. The data provided is a use case for an unmanned surface vehicle, though other designs can be analyzed as long as the data source matches the source csv files provided.

## Requirements
To install all of the required packages to this tool, from within this folder, simply run:

```
pip3 install -r requirements.txt
```
and all of the required `pip3` packages, will be installed, and the app will be able to run.

## Running the Code
to run the analysis and launch the dashboard: `python3 code/main.py`

to run the dashboard independently: `python3 code/dashboard.py`

to open the dashboard once it is running, open a web browser and open the page: http://127.0.0.1:8050/

## To Run Other Data
1. Prepare node list and adjacency list, following templates Data/Node_List.csv and Data/Adjacency_Lists/All.csv
2. Download [Gephi](https://gephi.org/)
3. Load all for the python scripts, as described above.
3. Load the network into Gephi.
  * If using sample network, the file is Gephi/five_layer_map_v1.gephi. This will allow you to visualize the five layers distinctly and will be interactive to show the multiple layers and node interconnectivity.
  * If using your own network, Gephi is a powerful tool and you can load in the node list and adjacency list using the import excel sheet tool in the Data Dashboard.
4. Open the python code code/main.py and load the adjlist and node_list at the top to your files from step 1.
5. Run the code as shown above. 

## Dependencies
* python3
* networkx
* pandas
* numpy
* scipy
* dash
* altair
* vegascope
