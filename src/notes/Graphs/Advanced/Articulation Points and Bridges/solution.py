class NetworkVulnerabilities:
    @staticmethod
    def find_bridges(vertices, edges):
        """
        Finds all bridges (cut edges) in an undirected graph using Tarjan's Algorithm.
        """
        adj = {i: [] for i in range(vertices)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        time = 0
        disc = [-1] * vertices
        low = [-1] * vertices
        bridges = []
        
        def dfs(node, parent):
            nonlocal time
            disc[node] = time
            low[node] = time
            time += 1
            
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if disc[neighbor] == -1: # Unvisited
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])
                    
                    if low[neighbor] > disc[node]:
                        bridges.append((node, neighbor))
                else: # Back-edge
                    low[node] = min(low[node], disc[neighbor])
                    
        for i in range(vertices):
            if disc[i] == -1:
                dfs(i, -1)
                
        return bridges

    @staticmethod
    def find_articulation_points(vertices, edges):
        """
        Finds all articulation points in an undirected graph.
        """
        adj = {i: [] for i in range(vertices)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        time = 0
        disc = [-1] * vertices
        low = [-1] * vertices
        ap = set()
        
        def dfs(node, parent):
            nonlocal time
            children = 0
            disc[node] = time
            low[node] = time
            time += 1
            
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if disc[neighbor] == -1: # Unvisited
                    children += 1
                    dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])
                    
                    if parent != -1 and low[neighbor] >= disc[node]:
                        ap.add(node)
                else: # Back-edge
                    low[node] = min(low[node], disc[neighbor])
                    
            if parent == -1 and children > 1:
                ap.add(node)
                
        for i in range(vertices):
            if disc[i] == -1:
                dfs(i, -1)
                
        return list(ap)

# Test Execution
if __name__ == "__main__":
    V = 5
    edges = [(1, 0), (0, 2), (2, 1), (0, 3), (3, 4)]
    print("Bridges:", NetworkVulnerabilities.find_bridges(V, edges))
    print("Articulation Points:", NetworkVulnerabilities.find_articulation_points(V, edges))
