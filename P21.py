import matplotlib.pyplot as plt
from collections import deque
import random

file_path = 'email-Eu-core.txt'
N = 1005

def calculate_average_clustering_coefficient(file_path):
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

    total_coefficient = 0
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
        total_coefficient += clustering_coefficient

    num_nodes = len(graph)
    average_clustering_coefficient = total_coefficient / num_nodes if num_nodes > 0 else 0

    return average_clustering_coefficient


# Example usage:
average_clustering_coefficient = calculate_average_clustering_coefficient(file_path)

print(f"Average Clustering Coefficient: {average_clustering_coefficient}")

