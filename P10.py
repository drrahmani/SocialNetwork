import matplotlib.pyplot as plt
from collections import deque

file_path = 'email-Eu-core.txt'

def calculate_distance(file_path, pairs):
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

    distances = []
    for pair in pairs:
        start, end = pair
        if start not in graph or end not in graph:
            distances.append(-1)  # One or both nodes not found in the graph
        else:
            visited = set()
            queue = deque([(start, 0)])  # (node, distance) tuple

            while queue:
                node, distance = queue.popleft()

                if node == end:
                    distances.append(distance)
                    break

                if node not in visited:
                    visited.add(node)
                    neighbors = graph[node]
                    queue.extend((neighbor, distance + 1) for neighbor in neighbors)

            if node != end:
                distances.append(-1)  # No path found between the nodes

    return distances


# Example usage:
pairs = [(1, 426), (3, 183), (5, 212), (7, 717), (9, 932)]  # Replace with your pairs of nodes
distances = calculate_distance(file_path, pairs)

for pair, distance in zip(pairs, distances):
    start, end = pair
    print(f"Distance between {start} and {end}: {distance}")

