"""
Problem: B-Tree Node Structure & Concept
Statement: Demonstrate the core logic of a B-Tree node, which holds an array of keys and an array of child pointers, optimized for block-disk reads.
"""

class BTreeNode:
    # Space Complexity: O(t) per node, where t is the minimum degree.
    
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []      # Array to hold multiple keys
        self.children = []  # Array to hold multiple child pointers

class BTreeConceptual:
    # Time Complexity: Search O(log N) disk reads.
    
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t # Minimum degree (defines the range for number of keys)

    def search(self, node, k):
        """ Find the first key greater than or equal to k """
        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1
            
        # If the found key is equal to k, return this node
        if i < len(node.keys) and node.keys[i] == k:
            return (node, i)
            
        # If key is not found here and this is a leaf, it doesn't exist
        if node.leaf:
            return None
            
        # Go to the appropriate child
        return self.search(node.children[i], k)

# Example usage
if __name__ == "__main__":
    btree = BTreeConceptual(t=3) # Nodes can hold up to 2*t - 1 = 5 keys
    
    # Manually creating a B-Tree structure for demonstration
    btree.root.leaf = False
    btree.root.keys = [10, 20]
    
    # A node with 2 keys has exactly 3 children
    child1, child2, child3 = BTreeNode(True), BTreeNode(True), BTreeNode(True)
    child1.keys = [1, 5]
    child2.keys = [12, 15]
    child3.keys = [25, 30]
    
    btree.root.children = [child1, child2, child3]
    
    # Search for 15
    result = btree.search(btree.root, 15)
    print("Found key 15 in a child node:", result[0].keys if result else "Not found") # Expected: [12, 15]