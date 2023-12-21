import collections

class Graph:
    def __init__(self):
        self.graph = collections.defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, root):
        visited = set()
        queue = collections.deque([root])
        visited.add(root)

        while queue:
            vertex = queue.popleft()
            print(str(vertex) + " ", end="")

            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

# Sample Case 1
print("Sample Case 1:")
g1 = Graph()
g1.add_edge(0, 1)
g1.add_edge(0, 2)
g1.add_edge(1, 2)
g1.add_edge(2, 0)
g1.add_edge(2, 3)
g1.add_edge(3, 3)

print("Breadth First Traversal from vertex 0:")
g1.bfs(0)
print("\n")

# Sample Case 2
print("Sample Case 2:")
g2 = Graph()
g2.add_edge(0, 1)
g2.add_edge(0, 2)
g2.add_edge(1, 2)
g2.add_edge(1, 3)
g2.add_edge(2, 3)
g2.add_edge(3, 3)

print("Breadth First Traversal from vertex 2:")
g2.bfs(2)
