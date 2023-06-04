import numpy as np
import networkx as nx

# Load the dataset and create a directed graph using NetworkX
dataset = np.loadtxt("soc-Epinions1.txt", delimiter='\t', skiprows=4)

# Create a directed graph
graph = nx.DiGraph()
graph.add_edges_from(dataset)

# Compute the probability of a path existing between two randomly chosen nodes from the graph
num_nodes = len(graph.nodes())
num_trials = 10000
connected_count = 0

for _ in range(num_trials):
    while True:
        node1, node2 = np.random.choice(list(graph.nodes()), size=2, replace=False)
        if graph.out_degree(node1) > 0 and graph.out_degree(node2) > 0:
            break

    if nx.has_path(graph, node1, node2):
        connected_count += 1

probability_graph = connected_count / num_trials

# Compute the probability of a path existing between two randomly chosen nodes from the WCC of the graph
wcc = max(nx.weakly_connected_components(graph), key=len)
wcc_graph = graph.subgraph(wcc)

connected_count_wcc = 0

for _ in range(num_trials):
    while True:
        node1, node2 = np.random.choice(list(wcc), size=2, replace=False)
        if wcc_graph.out_degree(node1) > 0 and wcc_graph.out_degree(node2) > 0:
            break

    if nx.has_path(wcc_graph, node1, node2):
        connected_count_wcc += 1

probability_wcc = connected_count_wcc / num_trials

# Calculate the percentage of node pairs that were connected in each case
percentage_graph = probability_graph * 100
percentage_wcc = probability_wcc * 100

print("Percentage of connected node pairs in the graph:", percentage_graph)
print("Percentage of connected node pairs in the WCC:", percentage_wcc)
