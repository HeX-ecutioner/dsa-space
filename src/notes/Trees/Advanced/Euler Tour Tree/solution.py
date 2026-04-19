"""
Problem: Euler Tour (Tree Flattening)
Statement: Given a tree (represented as an adjacency list), compute the entry and exit times for every node to flatten subtrees into contiguous array segments.
"""

class EulerTour:
    # Time Complexity: O(N) for DFS traversal.
    # Space Complexity: O(N) for arrays.
    
    def __init__(self, n, adj):
        self.adj = adj
        self.entry = [0] * n
        self.exit = [0] * n
        self.flat_tree = []
        self.timer = 0
        
    def dfs(self, u, parent):
        self.entry[u] = self.timer
        self.flat_tree.append(u)
        self.timer += 1
        
        for neighbor in self.adj[u]:
            if neighbor != parent:
                self.dfs(neighbor, u)
                
        self.exit[u] = self.timer - 1

# Example usage
if __name__ == "__main__":
    # Tree graph: 0 is root. 0 connects to 1 and 2. 1 connects to 3.
    #    0
    #   / \
    #  1   2
    #  |
    #  3
    adj = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}
    
    tour = EulerTour(4, adj)
    tour.dfs(0, -1)
    
    print("Flattened Tree (Discovery order):", tour.flat_tree)
    print("Node 1 Subtree range in array: index", tour.entry[1], "to", tour.exit[1])
    # Subtree of 1 includes nodes 1 and 3. Entry is 1, Exit is 2.