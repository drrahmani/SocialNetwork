import matplotlib.pyplot as plt
from collections import deque
import random

file_path = 'email-Eu-core.txt'
N = 1005


def count_nodes_in_outgoing_set(file_path, node_list):
    graph = {}
    with open(file_path, 'r') as file:
        for line in file:
            sender, receiver = map(int, line.strip().split())
            if sender not in graph:
                graph[sender] = []
            if receiver not in graph:
                graph[receiver] = []
            graph[sender].append(receiver)

    num_nodes_in_outgoing_set = []
    for node in node_list:
        if node in graph:
            num_nodes_in_outgoing_set.append(len(graph[node]))
        else:
            num_nodes_in_outgoing_set.append(0)

    return num_nodes_in_outgoing_set


# Example usage:
random_nodes = random.sample(range(1, N + 1), 5)  # Replace num_nodes with the actual number of nodes in the graph
num_nodes_in_outgoing_set = count_nodes_in_outgoing_set(file_path, random_nodes)

for i, node in enumerate(random_nodes):
    print(f"Number of nodes in Out({node}): {num_nodes_in_outgoing_set[i]}")

