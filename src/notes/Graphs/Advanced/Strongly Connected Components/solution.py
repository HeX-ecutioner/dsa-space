class SCCAlgorithms:
    @staticmethod
    def kosaraju(vertices, adj):
        """
        Kosaraju's Algorithm for finding Strongly Connected Components.
        """
        visited = set()
        stack = []
        
        # Pass 1: Order by finishing time
        def dfs_pass1(node):
            visited.add(node)
            for neighbor in adj.get(node, []):
                if neighbor not in visited:
                    dfs_pass1(neighbor)
            stack.append(node)
            
        for i in range(vertices):
            if i not in visited:
                dfs_pass1(i)
                
        # Create Transpose Graph
        transpose_adj = {i: [] for i in range(vertices)}
        for u in range(vertices):
            for v in adj.get(u, []):
                transpose_adj[v].append(u)
                
        # Pass 2: DFS on Transpose
        visited.clear()
        sccs = []
        
        def dfs_pass2(node, current_scc):
            visited.add(node)
            current_scc.append(node)
            for neighbor in transpose_adj.get(node, []):
                if neighbor not in visited:
                    dfs_pass2(neighbor, current_scc)
                    
        while stack:
            node = stack.pop()
            if node not in visited:
                current_scc = []
                dfs_pass2(node, current_scc)
                sccs.append(current_scc)
                
        return sccs

# Test Execution
if __name__ == "__main__":
    V = 5
    adj = {
        0: [2, 3],
        1: [0],
        2: [1],
        3: [4],
        4: []
    }
    print("Kosaraju SCCs:", SCCAlgorithms.kosaraju(V, adj))
