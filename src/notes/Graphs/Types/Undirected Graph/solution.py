class UndirectedGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        # Edge is bidirectional
        self.adj[u].append(v)
        self.adj[v].append(u)

    def print_graph(self):
        for vertex in range(self.V):
            print(f"Vertex {vertex} is connected to: {self.adj[vertex]}")

    def get_degrees(self):
        return {i: len(self.adj[i]) for i in range(self.V)}

# Test
if __name__ == "__main__":
    g = UndirectedGraph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    
    g.print_graph()
    print("Degrees:", g.get_degrees())
