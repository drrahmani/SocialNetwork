import matplotlib.pyplot as plt
from collections import deque

file_path = 'email-Eu-core.txt'


def find_bridge_edges(file_path):
    graph = {}
    with open(file_path, 'r') as file:
        for line in file:
            sender, receiver = map(int, line.strip().split())
            if sender not in graph:
                graph[sender] = []
            if receiver not in graph:
                graph[receiver] = []
            graph[sender].append(receiver)
            graph[receiver].append(sender)

    num_bridge_edges = 0
    visited = set()
    lowlink = {}
    discovery = {}
    parent = {}

    def dfs(node):
        nonlocal num_bridge_edges
        visited.add(node)
        lowlink[node] = discovery[node] = len(visited)

        for neighbor in graph[node]:
            if neighbor not in visited:
                parent[neighbor] = node
                dfs(neighbor)
                lowlink[node] = min(lowlink[node], lowlink[neighbor])
                if lowlink[neighbor] > discovery[node]:
                    num_bridge_edges += 1
            else:
                if parent[node] != neighbor:
                    lowlink[node] = min(lowlink[node], discovery[neighbor])

    for node in graph:
        if node not in visited:
            parent[node] = None
            dfs(node)

    return num_bridge_edges


# Example usage:
num_bridge_edges = find_bridge_edges(file_path)

print("Number of Bridge Edges:", num_bridge_edges)
