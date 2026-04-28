import heapq

class ShortestPathSolver:
    """
    A comprehensive suite of shortest path algorithms for different graph types.
    """

    @staticmethod
    def dijkstra(graph, start):
        """
        Dijkstra's Algorithm.
        Finds the shortest path from a starting node to all other nodes.
        Constraints: Non-negative edge weights only.
        Time Complexity: O((V + E) log V)
        Space Complexity: O(V)
        
        :param graph: Adjacency list representation {u: [(v, weight), ...]}
        :param start: The starting node
        :return: Dictionary of shortest distances from start to all nodes
        """
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        pq = [(0, start)] # (distance, node)
        visited = set()

        while pq:
            current_dist, current_node = heapq.heappop(pq)

            if current_node in visited:
                continue
            visited.add(current_node)

            # Important: It's possible to have a stale higher distance in the PQ
            if current_dist > distances[current_node]:
                continue

            for neighbor, weight in graph.get(current_node, []):
                distance = current_dist + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

    @staticmethod
    def bellman_ford(vertices, edges, start):
        """
        Bellman-Ford Algorithm.
        Finds the shortest path from a start node to all others.
        Can handle negative weights. Can detect negative weight cycles.
        Time Complexity: O(V * E)
        Space Complexity: O(V)
        
        :param vertices: Number of vertices (0 to V-1)
        :param edges: List of tuples (u, v, weight)
        :param start: The starting node
        :return: Dictionary of distances, or None if negative cycle detected.
        """
        distances = {i: float('inf') for i in range(vertices)}
        distances[start] = 0

        # Relax all edges V-1 times
        for _ in range(vertices - 1):
            for u, v, weight in edges:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

        # 1 more relaxation to check for negative-weight cycles
        for u, v, weight in edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                print("Graph contains a negative-weight cycle")
                return None

        return distances

    @staticmethod
    def floyd_warshall(vertices, edges):
        """
        Floyd-Warshall Algorithm.
        All-Pairs Shortest Path (APSP). Finds shortest path between every pair of nodes.
        Time Complexity: O(V^3)
        Space Complexity: O(V^2)
        
        :param vertices: Number of vertices (0 to V-1)
        :param edges: List of tuples (u, v, weight)
        :return: 2D array of shortest distances
        """
        dist = [[float('inf')] * vertices for _ in range(vertices)]
        for i in range(vertices):
            dist[i][i] = 0
            
        for u, v, weight in edges:
            dist[u][v] = weight
            # If undirected, uncomment: dist[v][u] = weight

        for k in range(vertices):
            for i in range(vertices):
                for j in range(vertices):
                    if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # Check for negative cycles
        for i in range(vertices):
            if dist[i][i] < 0:
                print("Negative cycle detected")
                return None
                
        return dist

# Test Execution
if __name__ == "__main__":
    print("Running Dijkstra...")
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('D', 3), ('C', 5)],
        'C': [('B', 1), ('D', 4), ('E', 5)],
        'D': [('E', 1)],
        'E': []
    }
    print(ShortestPathSolver.dijkstra(graph, 'A'))
