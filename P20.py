import matplotlib.pyplot as plt
from collections import deque
import random

file_path = 'email-Eu-core.txt'
N = 1005


def calculate_clustering_coefficient_distribution(file_path):
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
    for node in graph:
        neighbors = graph[node]
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
clustering_coefficients = calculate_clustering_coefficient_distribution(file_path)

# Plotting the clustering coefficient distribution
plt.hist(clustering_coefficients, bins=10, edgecolor='black')
plt.xlabel('Clustering Coefficient')
plt.ylabel('Frequency')
plt.title('Clustering Coefficient Distribution')
plt.show()
