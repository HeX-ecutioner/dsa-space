from collections import deque

class TopologicalSort:
    """
    Algorithms for Topological Sorting of Directed Acyclic Graphs (DAGs).
    A topological sort is a linear ordering of vertices such that for every directed edge u -> v, 
    vertex u comes before v in the ordering.
    """

    @staticmethod
    def kahn_algorithm(vertices, edges):
        """
        Kahn's Algorithm (BFS based).
        Iteratively removes nodes with in-degree 0.
        Also extremely useful for detecting cycles in directed graphs (if sort length != V).
        
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        
        :param vertices: Integer number of vertices (0 to V-1)
        :param edges: List of directed edges (u, v)
        :return: List representing topological order, or None if cycle exists
        """
        # 1. Initialize Adjacency List and In-Degree array
        adj = {i: [] for i in range(vertices)}
        in_degree = {i: 0 for i in range(vertices)}
        
        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1
            
        # 2. Queue all nodes with 0 in-degree
        queue = deque([i for i in range(vertices) if in_degree[i] == 0])
        topo_order = []
        
        # 3. BFS
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            
            # Decrease in-degree of all neighbors
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # 4. Check for cycles
        if len(topo_order) != vertices:
            print("Cycle detected! Topological sort not possible.")
            return None
            
        return topo_order

    @staticmethod
    def dfs_based(vertices, edges):
        """
        DFS-based Topological Sort.
        Perform DFS, and push a node to a stack only after all its descendants are visited.
        Reversing the stack gives the topological sort.
        
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        adj = {i: [] for i in range(vertices)}
        for u, v in edges:
            adj[u].append(v)
            
        visited = set()
        stack = []
        
        # To detect cycles during DFS, use a recursion stack (visiting set)
        visiting = set()
        
        def dfs(node):
            if node in visiting:
                return False # Cycle detected
            if node in visited:
                return True
                
            visiting.add(node)
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False
            visiting.remove(node)
            
            visited.add(node)
            stack.append(node) # Crucial: add to stack AFTER processing children
            return True
            
        for i in range(vertices):
            if i not in visited:
                if not dfs(i):
                    print("Cycle detected! Topological sort not possible.")
                    return None
                    
        return stack[::-1] # Return reversed stack

# Test Execution
if __name__ == "__main__":
    V = 6
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    print("Kahn's Algorithm:", TopologicalSort.kahn_algorithm(V, edges))
    print("DFS-Based:", TopologicalSort.dfs_based(V, edges))
