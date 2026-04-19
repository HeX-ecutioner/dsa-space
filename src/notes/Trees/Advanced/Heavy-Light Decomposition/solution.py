"""
Problem: Heavy-Light Decomposition (HLD)
Statement: Perform the two DFS passes required to decompose a tree into Heavy Chains.
"""

class HLD:
    # Time Complexity: O(N) to build the decomposition.
    # Space Complexity: O(N) for the arrays tracking chains, sizes, and depths.

    def __init__(self, n, adj):
        self.n = n
        self.adj = adj
        
        self.parent = [-1] * n
        self.depth = [0] * n
        self.subtree_size = [0] * n
        self.heavy_child = [-1] * n
        
        self.chain_head = [-1] * n # The top node of the chain this node belongs to
        self.pos_in_array = [0] * n # To map tree nodes to a flat Segment Tree array
        self.current_pos = 0

    def dfs_size(self, u, p, d):
        """ Pass 1: Calculate subtree sizes and find heavy children. """
        self.parent[u] = p
        self.depth[u] = d
        self.subtree_size[u] = 1
        max_sub = 0
        
        for v in self.adj[u]:
            if v != p:
                sub_size = self.dfs_size(v, u, d + 1)
                self.subtree_size[u] += sub_size
                # The child with the largest subtree becomes the heavy child
                if sub_size > max_sub:
                    max_sub = sub_size
                    self.heavy_child[u] = v
                    
        return self.subtree_size[u]

    def dfs_hld(self, u, p, head):
        """ Pass 2: Build the chains and map them to a 1D array. """
        self.chain_head[u] = head
        self.pos_in_array[u] = self.current_pos
        self.current_pos += 1
        
        # 1. Continue the heavy chain first (ensures they are contiguous in memory)
        if self.heavy_child[u] != -1:
            self.dfs_hld(self.heavy_child[u], u, head)
            
        # 2. Start new chains for all light children
        for v in self.adj[u]:
            if v != p and v != self.heavy_child[u]:
                # The light child becomes the head of its own new chain
                self.dfs_hld(v, u, v)

# Example usage
if __name__ == "__main__":
    # Tree: 0-1, 0-2, 1-3, 1-4, 3-5
    # Subtree sizes: 0(6), 1(4), 2(1), 3(2), 4(1), 5(1)
    # Heavy edges: 0->1, 1->3, 3->5.
    adj = {0: [1, 2], 1: [0, 3, 4], 2: [0], 3: [1, 5], 4: [1], 5: [3]}
    
    hld = HLD(6, adj)
    hld.dfs_size(0, -1, 0)
    hld.dfs_hld(0, -1, 0)
    
    print("Heavy Children for each node:", hld.heavy_child) 
    # Node 0's heavy child is 1, Node 1's is 3, Node 3's is 5.
    print("Chain Heads for each node:", hld.chain_head)
    # Nodes 0, 1, 3, 5 all belong to the chain headed by 0. Nodes 2 and 4 are their own heads.