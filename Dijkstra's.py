import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def next_unvisited_vertex(self, visited_distances):
        current_vertex = -10
        for index in range(self.V):
            if visited_distances[index][0] == 0 \
                    and (current_vertex < 0 or visited_distances[index][1] <= visited_distances[current_vertex][1]):
                current_vertex = index
        return current_vertex

    def dijkstra_algorithm(self, adj_matrix, weights_mat):
        visited_distances = [[0, 0]]
        for i in range(self.V - 1):
            visited_distances.append([0, sys.maxsize])

        for vertex in range(self.V):
            current_vertex = self.next_unvisited_vertex(visited_distances)
            for neighbor_index in range(self.V):
                if adj_matrix[current_vertex][neighbor_index] == 1 and visited_distances[neighbor_index][0] == 0:
                    new_distance = visited_distances[current_vertex][1] + weights_mat[current_vertex][neighbor_index]
                    if visited_distances[neighbor_index][1] > new_distance:
                        visited_distances[neighbor_index][1] = new_distance

                visited_distances[current_vertex][0] = 1

        vertex_index = 0
        for distance_info in visited_distances:
            print("Distance of ", chr(ord('A') + vertex_index), " from source vertex: ", distance_info[1])
            vertex_index += 1

# Define the graph using adjacency matrices for Sample Case 1
adjacency_matrix_1 = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

weights_matrix_1 = [
    [0, 4, 3, 0, 0, 0],
    [4, 0, 2, 5, 0, 0],
    [3, 2, 0, 1, 6, 0],
    [0, 5, 1, 0, 2, 4],
    [0, 0, 6, 2, 0, 3],
    [0, 0, 0, 4, 3, 0]
]

# Define the graph using adjacency matrices for Sample Case 2
adjacency_matrix_2 = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

weights_matrix_2 = [
    [0, 2, 0, 1],
    [2, 0, 3, 0],
    [0, 3, 0, 4],
    [1, 0, 4, 0]
]

# Sample Case 1
print("Sample Case 1:")
g1 = Graph(len(adjacency_matrix_1))
g1.dijkstra_algorithm(adjacency_matrix_1, weights_matrix_1)

# Sample Case 2
print("\nSample Case 2:")
g2 = Graph(len(adjacency_matrix_2))
g2.dijkstra_algorithm(adjacency_matrix_2, weights_matrix_2)
