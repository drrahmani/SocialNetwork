import matplotlib.pyplot as plt
from collections import deque

file_path = 'email-Eu-core.txt'


from collections import defaultdict, deque

def construct_undirected_graph(file_path):
    undirected_graph = defaultdict(list)
    with open(file_path, 'r') as file:
        for line in file:
            sender, receiver = map(int, line.strip().split())
            undirected_graph[sender].append(receiver)
            undirected_graph[receiver].append(sender)
    return undirected_graph

def find_weakly_connected_components(graph):
    visited = set()
    weakly_connected_components = []

    for node in graph:
        if node not in visited:
            component = []
            queue = deque([node])
            while queue:
                current_node = queue.popleft()
                if current_node not in visited:
                    visited.add(current_node)
                    component.append(current_node)
                    queue.extend(graph[current_node])
            weakly_connected_components.append(component)

    return weakly_connected_components

def calculate_weakly_connected_component_size_distribution(file_path):
    undirected_graph = construct_undirected_graph(file_path)
    weakly_connected_components = find_weakly_connected_components(undirected_graph)

    size_distribution = defaultdict(int)
    for component in weakly_connected_components:
        size_distribution[len(component)] += 1

    return len(weakly_connected_components) == 1, size_distribution,


# Example usage:
is_weakly_connected, weakly_connected_component_size_distribution = calculate_weakly_connected_component_size_distribution(file_path)

print("Weakly Connected Component Size Distribution:")
for size, count in weakly_connected_component_size_distribution.items():
    print(f"Component Size {size}: {count} component(s)")

if is_weakly_connected:
    print("The graph is weakly connected.")
else:
    print("The graph is not weakly connected.")

