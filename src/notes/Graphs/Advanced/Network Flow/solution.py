from collections import deque

class NetworkFlow:
    @staticmethod
    def edmonds_karp(vertices, capacity_matrix, source, sink):
        """
        Edmonds-Karp Algorithm for Maximum Flow.
        Uses BFS to find the shortest augmenting path.
        """
        def bfs(parent):
            visited = set()
            queue = deque([source])
            visited.add(source)
            
            while queue:
                u = queue.popleft()
                for v in range(vertices):
                    # If not visited and residual capacity is > 0
                    if v not in visited and capacity_matrix[u][v] > 0:
                        queue.append(v)
                        visited.add(v)
                        parent[v] = u
                        if v == sink:
                            return True
            return False

        max_flow = 0
        parent = [-1] * vertices

        while bfs(parent):
            # Find minimum residual capacity along the path
            path_flow = float("inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, capacity_matrix[parent[s]][s])
                s = parent[s]
                
            # Update residual capacities
            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                capacity_matrix[u][v] -= path_flow
                capacity_matrix[v][u] += path_flow # Reverse edge for undo
                v = parent[v]
                
        return max_flow

# Test Execution
if __name__ == "__main__":
    # Graph representation: Adjacency Matrix
    graph = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]
    print("Maximum Flow:", NetworkFlow.edmonds_karp(6, graph, 0, 5))
