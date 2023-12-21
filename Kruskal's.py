class GraphKruskal:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, src, dest, weight):
        self.graph.append([src, dest, weight])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_algorithm(self):
        result = []
        i, edges = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = [i for i in range(self.V)]
        rank = [0] * self.V
        while edges < self.V - 1 and i < len(self.graph):
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                edges += 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))

# Sample Case
g = GraphKruskal(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)

print("Minimum Spanning Tree for Sample Case 1:")
g.kruskal_algorithm()

# Additional Sample Case 1
g1 = GraphKruskal(4)
g1.add_edge(0, 1, 10)
g1.add_edge(0, 2, 6)
g1.add_edge(0, 3, 5)
g1.add_edge(1, 3, 15)
g1.add_edge(2, 3, 4)

print("\nMinimum Spanning Tree for  Sample Case 2:")
g1.kruskal_algorithm()

# Additional Sample Case 2
g2 = GraphKruskal(5)
g2.add_edge(0, 1, 7)
g2.add_edge(0, 2, 8)
g2.add_edge(1, 2, 6)
g2.add_edge(1, 3, 5)
g2.add_edge(2, 4, 12)
g2.add_edge(3, 4, 9)

print("\nMinimum Spanning Tree for  Sample Case 3:")
g2.kruskal_algorithm()
