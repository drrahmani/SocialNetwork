import matplotlib.pyplot as plt
from collections import deque

file_path = 'email-Eu-core.txt'

def tarjan_strongly_connected_components(graph):
    index_counter = [0]
    stack = []
    lowlink = {}
    index = {}
    result = []

    def strongconnect(node):
        index[node] = index_counter[0]
        lowlink[node] = index_counter[0]
        index_counter[0] += 1
        stack.append(node)

        for neighbor in graph[node]:
            if neighbor not in index:
                strongconnect(neighbor)
                lowlink[node] = min(lowlink[node], lowlink[neighbor])
            elif neighbor in stack:
                lowlink[node] = min(lowlink[node], index[neighbor])

        if lowlink[node] == index[node]:
            component = []
            while True:
                neighbor = stack.pop()
                component.append(neighbor)
                if neighbor == node:
                    break
            result.append(component)

    for node in graph:
        if node not in index:
            strongconnect(node)

    return result

def is_strongly_connected(file_path):
    graph = {}
    with open(file_path, 'r') as file:
        for line in file:
            sender, receiver = map(int, line.strip().split())
            if sender not in graph:
                graph[sender] = []
            if receiver not in graph:
                graph[receiver] = []
            graph[sender].append(receiver)

    sccs = tarjan_strongly_connected_components(graph)

    scc_sizes = [len(scc) for scc in sccs]
    scc_size_distribution = {size: scc_sizes.count(size) for size in set(scc_sizes)}

    return len(sccs) == 1, scc_size_distribution


# Example usage:
try:
    is_strongly_connected, scc_size_distribution = is_strongly_connected(file_path)

    print("Strongly Connected Component Size Distribution:")
    for size, count in scc_size_distribution.items():
        print(f"Component Size {size}: {count} component(s)")
    if is_strongly_connected:
        print("The graph is strongly connected.")
    else:
        print("The graph is not strongly connected.")
except KeyError as e:
    print(f"Error: Invalid node ID encountered: {e}")
