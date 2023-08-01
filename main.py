# import
import pandas as pd
from jaal import Jaal

# load the data
edge_df = pd.read_csv("venv/networkData/edges.csv")
node_df = pd.read_csv("venv/networkData/nodes.csv")

# init Jaal and run server
Jaal(edge_df, node_df).plot()