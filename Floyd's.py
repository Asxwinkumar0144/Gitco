class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.INF = 999
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append((u, v, weight))

    def floyd_warshall(self):
        distance = [[self.INF for _ in range(self.num_vertices)] for _ in range(self.num_vertices)]
        
        for i in range(self.num_vertices):
            distance[i][i] = 0
        
        for u, v, weight in self.graph:
            distance[u][v] = weight
        
        for k in range(self.num_vertices):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        
        self.print_solution(distance)

    def print_solution(self, distance):
        print("Shortest distances between every pair of vertices:")
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if distance[i][j] == self.INF:
                    print("INF", end=" ")
                else:
                    print(distance[i][j], end=" ")
            print()

# Test Cases
g = Graph(4)
g.add_edge(0, 1, 3)
g.add_edge(0, 3, 5)
g.add_edge(1, 2, 1)
g.add_edge(2, 3, 2)

g.floyd_warshall()

# Additional Test Cases
g2 = Graph(4)
g2.add_edge(0, 1, 3)
g2.add_edge(0, 3, 2)
g2.add_edge(1, 2, 4)
g2.add_edge(2, 3, 1)

g2.floyd_warshall()

g3 = Graph(4)
g3.add_edge(0, 1, 2)
g3.add_edge(1, 2, 1)
g3.add_edge(2, 3, 3)
g3.add_edge(3, 0, 4)

g3.floyd_warshall()
