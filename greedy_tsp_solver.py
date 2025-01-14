import numpy as np

def greedy_tsp_solver(adj_matrix, full_nodes, start_node=0):

    n = adj_matrix.shape[0]
    distance = 0
    visited = np.zeros(n, dtype=bool)
    visited[start_node] = True
    path = [start_node]

    sub_matrix = adj_matrix[np.ix_(full_nodes, full_nodes)] # only consider full nodes
    for _ in range(n-1):
        current_node = path[-1]
        next_node = np.argmin(adj_matrix[current_node] + 1e6*visited)
        visited[next_node] = True
        path.append(int(next_node))

    for node in path:
        distance += adj_matrix[path[node-1], path[node]]

    distance = int(distance)

    return path, distance

adj_matrix = np.array([
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
])

adj_matrix = (adj_matrix + adj_matrix.T)/2

print(adj_matrix)

path = greedy_tsp_solver(adj_matrix, start_node=0)
print("Path:", path)




