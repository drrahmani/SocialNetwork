import matplotlib.pyplot as plt
from collections import deque

file_path = 'email-Eu-core.txt'

def calculate_shortest_path_lengths(file_path):
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

    diameter = 0

    shortest_path_lengths = []
    num_nodes = len(graph)

    for start_node in graph:
        distances = {}
        visited = set()
        queue = deque([(start_node, 0)])  # (node, distance) tuple

        while queue:
            node, distance = queue.popleft()

            if node not in visited:
                visited.add(node)
                distances[node] = distance
                neighbors = graph[node]
                queue.extend((neighbor, distance + 1) for neighbor in neighbors)

        max_distance = max(distances.values())
        diameter = max(diameter, max_distance)

        for end_node in graph:
            if start_node != end_node:
                shortest_path_lengths.append(distances.get(end_node, -1))

    return shortest_path_lengths, diameter


# Example usage:
shortest_path_lengths, diameter = calculate_shortest_path_lengths(file_path)

# Plotting the shortest path length distribution
print('Diameter is:', diameter)
plt.hist(shortest_path_lengths, bins=10, edgecolor='black')
plt.title("Shortest Path Length Distribution")
plt.xlabel("Shortest Path Length")
plt.ylabel("Count")
plt.show()
