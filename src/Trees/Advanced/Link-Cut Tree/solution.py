"""
Problem: Link-Cut Tree Architecture
Statement: Demonstrate the node structure and the core concept of 'path-parent' pointers that separate Splay trees in a Link-Cut forest.
"""

class LCTNode:
    def __init__(self, val):
        self.val = val
        
        # Standard Splay Tree pointers (represents a single solid path)
        self.left = None
        self.right = None
        self.parent = None
        
        # The Link-Cut Magic: Path-Parent pointer
        # If a node is the root of a Splay Tree, it might still be connected to another 
        # path in the represented tree. 'path_parent' points to that higher-up node.
        self.path_parent = None

class LinkCutTreeConceptual:
    # Time Complexity: O(log N) amortized for link, cut, and access.
    
    def is_root(self, node):
        """ A node is a Splay root if its parent does not point back to it. """
        return not node.parent or (node.parent.left != node and node.parent.right != node)

    # Note: Full implementations require complex Splay Tree rotations (zig, zag).
    # The absolute core operation of LCT is `access`:
    def access_conceptual(self, v):
        """ 
        Brings node 'v' and the root of the represented tree into the same Splay Tree,
        making 'v' the deepest node in that path (no right child).
        """
        last_splay_root = None
        curr = v
        
        while curr:
            # 1. Splay 'curr' to the top of its current auxiliary Splay Tree
            # self.splay(curr) 
            
            # 2. Disconnect the old right child (it becomes its own path)
            if curr.right:
                curr.right.path_parent = curr
                curr.right.parent = None
                
            # 3. Connect the path we are building from the bottom
            curr.right = last_splay_root
            if last_splay_root:
                last_splay_root.parent = curr
                last_splay_root.path_parent = None
                
            last_splay_root = curr
            curr = curr.path_parent # Move up to the next path
            
        # self.splay(v) # Finally, splay v to the very top

# Example usage
if __name__ == "__main__":
    print("Link-Cut Tree is a forest of Splay Trees connected by path-parent pointers.")
    print("Due to extreme complexity (300+ lines), it is represented conceptually for interviews.")