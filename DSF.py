class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = set()
        self.graph[u].add(v)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)

        print(start)

        for next_node in self.graph[start] - visited:
            self.dfs(next_node, visited)
        return visited


# Sample Case 1
print("Sample Case 1:")
g1 = Graph()
g1.add_edge('0', '1')
g1.add_edge('0', '2')
g1.add_edge('1', '3')
g1.add_edge('1', '4')
g1.add_edge('1', '0')
g1.add_edge('2', '0')
g1.add_edge('3', '1')
g1.add_edge('4', '2')
g1.add_edge('4', '3')

print("DFS Traversal from vertex '0':")
g1.dfs('0')
print("\n")

# Sample Case 2
print("Sample Case 2:")
g2 = Graph()
g2.add_edge('A', 'B')
g2.add_edge('A', 'C')
g2.add_edge('B', 'D')
g2.add_edge('C', 'D')
g2.add_edge('D', 'E')
g2.add_edge('E', 'F')
g2.add_edge('F', 'C')

print("DFS Traversal from vertex 'A':")
g2.dfs('A')
print("\n")

# Additional Sample Case 3
print("Additional Sample Case 3:")
g3 = Graph()
g3.add_edge('X', 'Y')
g3.add_edge('X', 'Z')
g3.add_edge('Y', 'W')
g3.add_edge('W', 'Z')
g3.add_edge('Z', 'V')
g3.add_edge('V', 'X')

print("DFS Traversal from vertex 'X':")
g3.dfs('X')
