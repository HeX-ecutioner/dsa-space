class DirectedGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        # Edge goes strictly from u to v
        self.adj[u].append(v)

    def print_graph(self):
        for vertex in range(self.V):
            print(f"Vertex {vertex} points to: {self.adj[vertex]}")

    def get_in_degrees(self):
        in_degrees = {i: 0 for i in range(self.V)}
        for u in range(self.V):
            for v in self.adj[u]:
                in_degrees[v] += 1
        return in_degrees

# Test
if __name__ == "__main__":
    g = DirectedGraph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    
    g.print_graph()
    print("In-degrees:", g.get_in_degrees())
