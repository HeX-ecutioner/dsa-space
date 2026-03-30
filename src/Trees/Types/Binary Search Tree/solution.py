"""
Problem: Implement a Binary Search Tree
Statement: Implement a BST with insert, search, and inorder traversal capabilities.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        # Time Complexity: O(log N) average, O(N) worst case.
        if not self.root:
            self.root = TreeNode(val)
            return
            
        def _insert(node, val):
            if val < node.val:
                if node.left: _insert(node.left, val)
                else: node.left = TreeNode(val)
            elif val > node.val:
                if node.right: _insert(node.right, val)
                else: node.right = TreeNode(val)
                
        _insert(self.root, val)

    def search(self, val):
        # Time Complexity: O(log N) average, O(N) worst case.
        def _search(node, val):
            if not node: return False
            if node.val == val: return True
            if val < node.val: return _search(node.left, val)
            return _search(node.right, val)
            
        return _search(self.root, val)

    def inorder(self):
        # An inorder traversal of a BST ALWAYS returns a sorted list.
        res = []
        def _inorder(node):
            if not node: return
            _inorder(node.left)
            res.append(node.val)
            _inorder(node.right)
        _inorder(self.root)
        return res

# Example usage
if __name__ == "__main__":
    tree = BST()
    for val in [5, 2, 8, 1, 3, 7, 9]:
        tree.insert(val)
        
    print("Inorder (Sorted):", tree.inorder())  # Expected: [1, 2, 3, 5, 7, 8, 9]
    print("Search for 3:", tree.search(3))      # Expected: True
    print("Search for 10:", tree.search(10))    # Expected: False