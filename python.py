# import matplotlib.pyplot as plt

import triangle as tr
import networkx as nx

import os, json, sys
import pickle
from pathlib import Path


### DATA INPUT

# run locally
if len(sys.argv) < 2:
	# hard code data path
	script_path = os.path.realpath(__file__).split("\\")
	data_path = "\\".join(script_path[:-1] + ["_temp", "script_inputs.d"])
# run from outside with args
else:
	# load data path from args
	data_path = sys.argv[-1]


with open(data_path, 'rb') as f:
	data_in = pickle.load(f, encoding='latin1') 


### PROCESS

data_out = "Data received: {}".format(data_in)


### DATA OUTPUT

output_path = "\\".join(data_path.split("\\")[:-1] + ["script_output.d"])

with open(output_path, 'wb') as f:
	pickle.dump(data_out, f, protocol=2)

print("Done with output:")

# must be last print statement
print(output_path)