import matplotlib.pyplot as plt
from collections import deque

file_path = 'email-Eu-core.txt'
def find_articulation_nodes(file_path):
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

    num_articulation_nodes = 0
    visited = set()
    discovery = {}
    lowlink = {}
    parent = {}
    is_articulation = set()

    def dfs(node):
        nonlocal num_articulation_nodes
        visited.add(node)
        discovery[node] = len(visited)
        lowlink[node] = discovery[node]
        child_count = 0
        is_articulation_node = False

        for neighbor in graph[node]:
            if neighbor not in visited:
                parent[neighbor] = node
                child_count += 1
                dfs(neighbor)

                lowlink[node] = min(lowlink[node], lowlink[neighbor])

                if parent[node] is None and child_count > 1:
                    is_articulation_node = True

                if parent[node] is not None and lowlink[neighbor] >= discovery[node]:
                    is_articulation_node = True
            elif neighbor != parent[node]:
                lowlink[node] = min(lowlink[node], discovery[neighbor])

        if is_articulation_node:
            num_articulation_nodes += 1
            is_articulation.add(node)

    for node in graph:
        if node not in visited:
            parent[node] = None
            dfs(node)

    return num_articulation_nodes, is_articulation


# Example usage:
num_articulation_nodes, articulation_nodes = find_articulation_nodes(file_path)

print("Number of Articulation Nodes:", num_articulation_nodes)
print("Articulation Nodes:", articulation_nodes)

