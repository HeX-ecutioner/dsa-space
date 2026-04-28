class CycleDetection:
    """
    Algorithms to detect cycles in both Undirected and Directed Graphs.
    """

    @staticmethod
    def is_cyclic_undirected_dfs(vertices, adj):
        """
        Cycle detection in Undirected Graph using DFS.
        A cycle exists if we visit a visited node that is NOT the immediate parent.
        Time: O(V + E), Space: O(V)
        """
        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    # Visited, and not the parent we just came from -> Cycle!
                    return True
            return False

        for i in range(vertices):
            if i not in visited:
                if dfs(i, -1):
                    return True
        return False

    @staticmethod
    def is_cyclic_directed_dfs(vertices, adj):
        """
        Cycle detection in Directed Graph using DFS (Coloring/Recursion Stack method).
        0 = Unvisited
        1 = Visiting (currently in recursion stack)
        2 = Visited (fully processed)
        
        If we hit a node in state 1, a back-edge exists, so there is a cycle.
        Time: O(V + E), Space: O(V)
        """
        state = {i: 0 for i in range(vertices)}

        def dfs(node):
            state[node] = 1 # Mark as visiting
            for neighbor in adj.get(node, []):
                if state[neighbor] == 0:
                    if dfs(neighbor):
                        return True
                elif state[neighbor] == 1:
                    # Back-edge detected
                    return True
            state[node] = 2 # Fully processed
            return False

        for i in range(vertices):
            if state[i] == 0:
                if dfs(i):
                    return True
        return False

    @staticmethod
    def union_find_undirected(vertices, edges):
        """
        Cycle detection in Undirected Graph using Disjoint Set Union (Union-Find).
        Only works for UNDIRECTED graphs.
        Time: O(E * alpha(V)), Space: O(V)
        """
        parent = [i for i in range(vertices)]
        rank = [0] * vertices

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i]) # Path compression
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            
            if root_i == root_j:
                return False # Cycle! They are already in the same set.
                
            # Union by rank
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            else:
                parent[root_j] = root_i
                rank[root_i] += 1
            return True

        for u, v in edges:
            if not union(u, v):
                return True # Cycle detected during union
        return False

# Test Execution
if __name__ == "__main__":
    undirected_adj = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    print("Undirected DFS Cycle:", CycleDetection.is_cyclic_undirected_dfs(3, undirected_adj))
    
    directed_adj = {0: [1], 1: [2], 2: [0]}
    print("Directed DFS Cycle:", CycleDetection.is_cyclic_directed_dfs(3, directed_adj))
