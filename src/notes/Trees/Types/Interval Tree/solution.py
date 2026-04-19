"""
Problem: Interval Tree Search Logic
Statement: Implement an augmented BST to find overlapping intervals.
"""

class IntervalNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.max_end = end # The maximum end value in the subtree
        self.left = None
        self.right = None

class IntervalTree:
    # Time Complexity: Insert O(log N), Search Overlap O(log N)
    
    def insert(self, root, start, end):
        if not root:
            return IntervalNode(start, end)
            
        # Standard BST insert based on the start time
        if start < root.start:
            root.left = self.insert(root.left, start, end)
        else:
            root.right = self.insert(root.right, start, end)
            
        # Augmentation: Update the max_end value!
        root.max_end = max(root.max_end, end)
        return root

    def is_overlap(self, root, start, end):
        """ Returns the first overlapping interval, or None """
        if not root:
            return None
            
        # Check if the current node overlaps with the target
        if root.start <= end and start <= root.end:
            return (root.start, root.end)
            
        # If left child exists and its max_end is large enough to reach our start time,
        # an overlap MIGHT exist in the left subtree. Search left.
        if root.left and root.left.max_end >= start:
            return self.is_overlap(root.left, start, end)
            
        # Otherwise, if an overlap exists, it MUST be in the right subtree.
        return self.is_overlap(root.right, start, end)

# Example usage
if __name__ == "__main__":
    it = IntervalTree()
    root = None
    intervals = [(15, 20), (10, 30), (17, 19), (5, 20), (12, 15), (30, 40)]
    
    for start, end in intervals:
        root = it.insert(root, start, end)
        
    print("Does [14, 16] overlap with anything?", it.is_overlap(root, 14, 16)) 
    # Expected: (15, 20) or (12, 15) or (10, 30) - any valid overlap.
    
    print("Does [21, 23] overlap with anything?", it.is_overlap(root, 21, 23)) 
    # Expected: (10, 30)