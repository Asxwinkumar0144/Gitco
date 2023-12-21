class GraphPrim:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(self.V)] for _ in range(self.V)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w  # If the graph is undirected

    def prim_algorithm(self):
        INF = float('inf')
        selected = [False] * self.V
        selected[0] = True
        no_edge = 0
        while no_edge < self.V - 1:
            minimum = INF
            x = 0
            y = 0
            for i in range(self.V):
                if selected[i]:
                    for j in range(self.V):
                        if (not selected[j]) and self.graph[i][j]:
                            if minimum > self.graph[i][j]:
                                minimum = self.graph[i][j]
                                x = i
                                y = j
            print(f"Edge: {x}-{y}, Weight: {self.graph[x][y]}")  # Print chosen edge and weight
            selected[y] = True
            no_edge += 1


# Sample Case 1
print("Sample Case 1:")
g1 = GraphPrim(5)
g1.add_edge(0, 1, 9)
g1.add_edge(0, 2, 75)
g1.add_edge(1, 2, 95)
g1.add_edge(1, 3, 19)
g1.add_edge(1, 4, 42)
g1.add_edge(2, 3, 51)
g1.add_edge(2, 4, 66)
g1.add_edge(3, 4, 31)

g1.prim_algorithm()
print("\n")

# Sample Case 2
print("Sample Case 2:")
g2 = GraphPrim(5)
g2.add_edge(0, 1, 8)
g2.add_edge(0, 2, 6)
g2.add_edge(1, 2, 7)
g2.add_edge(1, 3, 9)
g2.add_edge(1, 4, 5)
g2.add_edge(2, 4, 7)
g2.add_edge(3, 4, 10)

g2.prim_algorithm()
print("\n")

# Sample Case 3
print("Sample Case 3:")
g3 = GraphPrim(4)
g3.add_edge(0, 1, 10)
g3.add_edge(0, 2, 6)
g3.add_edge(0, 3, 5)
g3.add_edge(1, 3, 15)
g3.add_edge(2, 3, 4)

g3.prim_algorithm()
