"""
Problem: B+ Tree Architecture & Range Queries
Statement: Demonstrate the structural difference between Internal Nodes (routing only) and Leaf Nodes (data + linked list), and implement a fast Range Query.
"""

class BPlusNode:
    def __init__(self, is_leaf=False):
        self.is_leaf = is_leaf
        self.keys = []

class BPlusInternalNode(BPlusNode):
    def __init__(self):
        super().__init__(is_leaf=False)
        self.children = [] # Pointers to other nodes

class BPlusLeafNode(BPlusNode):
    def __init__(self):
        super().__init__(is_leaf=True)
        self.values = []   # Actual database records/pointers
        self.next = None   # Magic pointer to the next leaf node!

class BPlusTree:
    # Time Complexity: Search O(log N), Range Query O(log N + K) where K is range size.
    # Space Complexity: O(N)
    
    def __init__(self):
        self.root = BPlusLeafNode()

    def search(self, key):
        """ Find the leaf node that should contain the key. """
        curr = self.root
        
        # Traverse down the internal nodes to find the correct leaf
        while not curr.is_leaf:
            i = 0
            while i < len(curr.keys) and key >= curr.keys[i]:
                i += 1
            curr = curr.children[i]
            
        # We are now at the leaf node. Check if the key exists.
        for i in range(len(curr.keys)):
            if curr.keys[i] == key:
                return curr.values[i]
                
        return None # Key not found

    def range_query(self, start_key, end_key):
        """ 
        The superpower of B+ Trees: Find the start key in O(log N), 
        then just walk the linked list in O(K) time! 
        """
        curr = self.root
        
        # 1. Find the starting leaf node O(log N)
        while not curr.is_leaf:
            i = 0
            while i < len(curr.keys) and start_key >= curr.keys[i]:
                i += 1
            curr = curr.children[i]
            
        result = []
        
        # 2. Walk the linked list to collect range O(K)
        # We don't have to traverse back up the tree at all!
        while curr:
            for i in range(len(curr.keys)):
                if start_key <= curr.keys[i] <= end_key:
                    result.append(curr.values[i])
                elif curr.keys[i] > end_key:
                    return result # We've passed the end of our range
                    
            curr = curr.next # Jump to the next leaf block
            
        return result

# Example usage
if __name__ == "__main__":
    # Manually constructing a small B+ Tree for demonstration
    # Internal Root Node
    tree = BPlusTree()
    root = BPlusInternalNode()
    root.keys = [20]
    
    # Left Leaf Node (Keys < 20)
    leaf1 = BPlusLeafNode()
    leaf1.keys = [10, 15]
    leaf1.values = ["Record_10", "Record_15"]
    
    # Right Leaf Node (Keys >= 20)
    leaf2 = BPlusLeafNode()
    leaf2.keys = [20, 25, 30]
    leaf2.values = ["Record_20", "Record_25", "Record_30"]
    
    # Connect the structure
    root.children = [leaf1, leaf2]
    leaf1.next = leaf2 # Link the leaves together!
    tree.root = root
    
    print("Exact Search for 25:", tree.search(25)) 
    # Expected: Record_25
    
    print("Range Query from 12 to 28:", tree.range_query(12, 28)) 
    # Expected: ['Record_15', 'Record_20', 'Record_25']