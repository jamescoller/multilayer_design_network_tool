import pandas as pd
import networkx as nx

pd.options.display.max_columns = 20
df = pd.DataFrame([[1, 1], [2, 1]])
G = nx.from_pandas_adjacency(df)
G.name = 'Graph from pandas adjacency matrix'
print(nx.info(G))
