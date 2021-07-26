import auxiliarymethods.datasets as dp
from auxiliarymethods.reader import tud_to_networkx
from networkx.readwrite import json_graph
import json
import math

#Codigo de generacion del dataset comentado
"""dataset = "Tox21_AhR_training"
# Download dataset.
dp.get_dataset(dataset)
# Output dataset as a list of graphs.
graph_db = tud_to_networkx(dataset)

num_train_examples = len(graph_db)

training_data = []
for i in range(num_train_examples):
	parsed_graph = json_graph.node_link_data(graph_db[i])
	training_data.append(parsed_graph)

with open('training_data_tox.json', 'w') as json_file:
        json.dump(training_data, json_file)"""

#Comprobacion de que cada edge_labels existe y con la dimension adecuada
training_file = json.load(open('training_data_tox.json',))
length_file = len(training_file)
for i in range(length_file):
	for item in training_file[i]["links"]:
		x = len(item["edge_labels"])==4
		assert x == True

