import numpy as np
import matplotlib.pyplot as plt
from collections import deque

# Load the dataset and compute adjacency lists
dataset = np.loadtxt("soc-Epinions1.txt", delimiter='\t', skiprows=4)

adj_list = {}
for edge in dataset:
    source = int(edge[0])
    target = int(edge[1])

    if source in adj_list:
        adj_list[source].append(target)
    else:
        adj_list[source] = [target]

# Randomly select 100 nodes
random_nodes = np.random.choice(list(adj_list.keys()), size=100, replace=False)

# Forward BFS traversal
def forward_bfs(start_node):
    visited = set()
    queue = deque([start_node])
    count = 0

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            count += 1
            if node in adj_list:
                queue.extend(adj_list[node])

    return count

# Backward BFS traversal
def backward_bfs(start_node):
    visited = set()
    queue = deque([start_node])
    count = 0

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            count += 1
            if node in adj_list:
                queue.extend(adj_list[node])

    return count

# Perform forward and backward BFS traversals on selected nodes
forward_bfs_counts = [forward_bfs(node) for node in random_nodes]
backward_bfs_counts = [backward_bfs(node) for node in random_nodes]

# Compute cumulative distributions
forward_bfs_counts.sort()
forward_bfs_cumulative = np.cumsum(forward_bfs_counts) / np.sum(forward_bfs_counts)

backward_bfs_counts.sort()
backward_bfs_cumulative = np.cumsum(backward_bfs_counts) / np.sum(backward_bfs_counts)

# Plot cumulative distributions
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(range(len(forward_bfs_cumulative)), forward_bfs_cumulative)
plt.xlabel('Number of Nodes')
plt.ylabel('Cumulative Distribution')
plt.title('Forward BFS')

plt.subplot(1, 2, 2)
plt.plot(range(len(backward_bfs_cumulative)), backward_bfs_cumulative)
plt.xlabel('Number of Nodes')
plt.ylabel('Cumulative Distribution')
plt.title('Backward BFS')

plt.tight_layout()
plt.show()

# Calculate the number of nodes in OUT, IN, and TENDRILS components
num_nodes_out = forward_bfs_cumulative[-1]
num_nodes_in = backward_bfs_cumulative[-1]
num_nodes_tendrils = len(adj_list) - num_nodes_out - num_nodes_in

print("Nodes in OUT component:", num_nodes_out)
print("Nodes in IN component:", num_nodes_in)
print("Nodes in TENDRILS component:", num_nodes_tendrils)
