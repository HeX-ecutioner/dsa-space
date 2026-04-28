class MinimumSpanningTree:
    """
    Algorithms to find the Minimum Spanning Tree (MST) of a connected, undirected graph.
    An MST is a subset of edges that connects all vertices, without any cycles,
    and with the minimum possible total edge weight.
    """

    @staticmethod
    def kruskal(vertices, edges):
        """
        Kruskal's Algorithm.
        Greedy algorithm that sorts all edges and adds them one by one if they don't form a cycle.
        Cycle detection is done using Disjoint Set Union (Union-Find).
        Time: O(E log E) or O(E log V)
        Space: O(V)
        
        :param vertices: Number of vertices
        :param edges: List of tuples (u, v, weight)
        :return: Tuple of (MST total weight, list of edges in MST)
        """
        # Sort edges by weight
        edges.sort(key=lambda item: item[2])
        
        parent = [i for i in range(vertices)]
        rank = [0] * vertices
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                if rank[root_i] < rank[root_j]:
                    parent[root_i] = root_j
                elif rank[root_i] > rank[root_j]:
                    parent[root_j] = root_i
                else:
                    parent[root_j] = root_i
                    rank[root_i] += 1
                return True
            return False

        mst_weight = 0
        mst_edges = []
        
        for u, v, weight in edges:
            if union(u, v):
                mst_weight += weight
                mst_edges.append((u, v, weight))
                if len(mst_edges) == vertices - 1:
                    break
                    
        return mst_weight, mst_edges

    @staticmethod
    def prim(vertices, adj_list):
        """
        Prim's Algorithm.
        Greedy algorithm that starts from an arbitrary node and grows the MST
        by picking the cheapest edge that connects a visited node to an unvisited node.
        Uses a Min-Heap (Priority Queue).
        Time: O((V + E) log V)
        Space: O(V + E)
        
        :param vertices: Number of vertices
        :param adj_list: Adjacency list {u: [(v, weight), ...]}
        :return: MST total weight
        """
        import heapq
        
        visited = set()
        min_heap = [(0, 0)] # (weight, node). Start from node 0.
        mst_weight = 0
        
        while min_heap and len(visited) < vertices:
            weight, node = heapq.heappop(min_heap)
            
            if node in visited:
                continue
                
            visited.add(node)
            mst_weight += weight
            
            for neighbor, edge_weight in adj_list.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, neighbor))
                    
        return mst_weight

# Test Execution
if __name__ == "__main__":
    V = 4
    edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
    
    print("Kruskal's MST:", MinimumSpanningTree.kruskal(V, edges))
    
    # Convert edges to adj_list for Prim's
    adj = {i: [] for i in range(V)}
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
        
    print("Prim's MST Weight:", MinimumSpanningTree.prim(V, adj))
