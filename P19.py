import matplotlib.pyplot as plt
from collections import deque
import random

file_path = 'email-Eu-core.txt'
N = 1005

def calculate_clustering_coefficient(file_path, node_list):
    graph = {}
    with open(file_path, 'r') as file:
        for line in file:
            sender, receiver = map(int, line.strip().split())
            if sender not in graph:
                graph[sender] = set()
            if receiver not in graph:
                graph[receiver] = set()
            graph[sender].add(receiver)
            graph[receiver].add(sender)

    clustering_coefficients = []
    for node in node_list:
        neighbors = graph.get(node, set())
        num_edges = len(neighbors)
        num_possible_edges = num_edges * (num_edges - 1) / 2 if num_edges >= 2 else 1
        num_actual_edges = 0

        for neighbor in neighbors:
            for neighbor2 in graph.get(neighbor, set()):
                if neighbor2 in neighbors:
                    num_actual_edges += 1

        clustering_coefficient = num_actual_edges / num_possible_edges if num_possible_edges > 0 else 0
        clustering_coefficients.append(clustering_coefficient)

    return clustering_coefficients


# Example usage:
random_nodes = random.sample(range(1, N + 1), 5)  # Replace num_nodes with the actual number of nodes in the graph
clustering_coefficients = calculate_clustering_coefficient(file_path, random_nodes)

for i, node in enumerate(random_nodes):
    print(f"Clustering coefficient for Node {node}: {clustering_coefficients[i]}")

