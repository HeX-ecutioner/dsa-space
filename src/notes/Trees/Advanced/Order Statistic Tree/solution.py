"""
Problem: Order Statistic Tree Logic
Statement: Implement an augmented BST that maintains subtree sizes to find the K-th smallest element.
"""

class OSNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.size = 1 # Number of nodes in this subtree

class OrderStatisticTree:
    # Time Complexity: Insert O(H), Find K-th O(H) (Where H is height, O(log N) if balanced)
    # Space Complexity: O(H) for recursion stack.

    def get_size(self, node):
        return node.size if node else 0

    def insert(self, root, val):
        if not root:
            return OSNode(val)
            
        if val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
            
        # Augmentation: Update the size after insertion!
        root.size = 1 + self.get_size(root.left) + self.get_size(root.right)
        return root

    def find_kth(self, root, k):
        """ Find the 1-based K-th smallest element """
        if not root:
            return None
            
        left_size = self.get_size(root.left)
        
        # If left subtree has exactly k-1 elements, root is the k-th!
        if left_size == k - 1:
            return root.val
            
        # If left subtree has k or more elements, the answer is in the left
        if left_size >= k:
            return self.find_kth(root.left, k)
            
        # Otherwise, the answer is in the right. We subtract the elements we skipped.
        return self.find_kth(root.right, k - left_size - 1)

# Example usage
if __name__ == "__main__":
    ost = OrderStatisticTree()
    root = None
    for val in [20, 10, 30, 5, 15, 25, 35]:
        root = ost.insert(root, val)
        
    print("3rd smallest element:", ost.find_kth(root, 3)) # Expected: 15
    print("6th smallest element:", ost.find_kth(root, 6)) # Expected: 30