class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph_edges = []

    def add_edge(self, u, v, weight):
        self.graph_edges.append((u, v, weight))

    def bellman_ford(self, start_vertex):
        # Step 1: Initialize distances and predecessors
        distances = {vertex: float('inf') for vertex in range(self.num_vertices)}
        predecessors = {vertex: None for vertex in range(self.num_vertices)}
        distances[start_vertex] = 0

        # Step 2: Relax edges repeatedly
        for _ in range(self.num_vertices - 1):
            for u, v, weight in self.graph_edges:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    predecessors[v] = u

        # Step 3: Check for negative cycles
        for u, v, weight in self.graph_edges:
            if distances[u] + weight < distances[v]:
                raise ValueError("Graph contains a negative cycle")

        return distances, predecessors


# Example usage with sample cases:
g = Graph(5)
g.add_edge(0, 1, 6)
g.add_edge(0, 3, 7)
g.add_edge(1, 2, 5)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, -4)
g.add_edge(2, 1, -2)
g.add_edge(3, 2, -3)
g.add_edge(3, 4, 9)
g.add_edge(4, 0, 2)
g.add_edge(4, 2, 7)

# Test Case 1
source_vertex_1 = 3
distances_1, predecessors_1 = g.bellman_ford(source_vertex_1)

print("Shortest distances from source vertex", source_vertex_1)
for vertex in range(g.num_vertices):
    print(f"Vertex {vertex}: Distance = {distances_1[vertex]}, Predecessor = {predecessors_1[vertex]}")

# Test Case 2
g2 = Graph(4)
g2.add_edge(0, 1, 3)
g2.add_edge(0, 3, 5)
g2.add_edge(1, 2, -2)
g2.add_edge(2, 0, 4)

source_vertex_2 = 0
distances_2, predecessors_2 = g2.bellman_ford(source_vertex_2)

print("\nShortest distances from source vertex", source_vertex_2)
for vertex in range(g2.num_vertices):
    print(f"Vertex {vertex}: Distance = {distances_2[vertex]}, Predecessor = {predecessors_2[vertex]}")
