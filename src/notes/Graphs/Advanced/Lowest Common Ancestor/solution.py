import math

class LowestCommonAncestor:
    def __init__(self, vertices, edges, root=0):
        """
        Initializes the LCA structure using Binary Lifting.
        Time: O(N log N)
        Space: O(N log N)
        """
        self.vertices = vertices
        self.max_jump = math.ceil(math.log2(vertices)) if vertices > 0 else 0
        
        self.adj = {i: [] for i in range(vertices)}
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)
            
        self.depth = [0] * vertices
        # up[i][j] stores the 2^j-th ancestor of node i
        self.up = [[-1] * self.max_jump for _ in range(vertices)]
        
        self._dfs(root, -1)

    def _dfs(self, node, parent):
        self.up[node][0] = parent
        
        # Precompute the 2^j th ancestor
        for j in range(1, self.max_jump):
            if self.up[node][j-1] != -1:
                self.up[node][j] = self.up[self.up[node][j-1]][j-1]
            else:
                self.up[node][j] = -1
                
        for neighbor in self.adj[node]:
            if neighbor != parent:
                self.depth[neighbor] = self.depth[node] + 1
                self._dfs(neighbor, node)

    def get_lca(self, u, v):
        """
        Gets the Lowest Common Ancestor of u and v.
        Time: O(log N)
        """
        # Ensure u is deeper than v
        if self.depth[u] < self.depth[v]:
            u, v = v, u
            
        # 1. Lift u to the same depth as v
        diff = self.depth[u] - self.depth[v]
        for j in range(self.max_jump):
            if (diff >> j) & 1:
                u = self.up[u][j]
                
        if u == v:
            return u
            
        # 2. Lift both u and v until they are just below the LCA
        for j in range(self.max_jump - 1, -1, -1):
            if self.up[u][j] != self.up[v][j]:
                u = self.up[u][j]
                v = self.up[v][j]
                
        # The parent of u (or v) is the LCA
        return self.up[u][0]

# Test Execution
if __name__ == "__main__":
    V = 7
    # Tree edges
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
    lca_solver = LowestCommonAncestor(V, edges, root=0)
    
    print("LCA of 3 and 4:", lca_solver.get_lca(3, 4)) # Expected 1
    print("LCA of 3 and 6:", lca_solver.get_lca(3, 6)) # Expected 0
    print("LCA of 4 and 1:", lca_solver.get_lca(4, 1)) # Expected 1
