"""
Problem: Check if a Binary Tree is a Full Tree
Statement: Determine if every node in the given binary tree has either 0 or 2 children.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isFullTree(root):
    # Time Complexity: O(N)
    # Space Complexity: O(H)
    
    if not root:
        return True
        
    # If it's a leaf node (0 children), it is full
    if not root.left and not root.right:
        return True
        
    # If it has both children, check its subtrees
    if root.left and root.right:
        return isFullTree(root.left) and isFullTree(root.right)
        
    # If it reaches here, it has exactly 1 child, which violates the Full Tree property
    return False

# Example usage
if __name__ == "__main__":
    # Full Tree
    #       1
    #      / \
    #     2   3
    #        / \
    #       4   5
    full = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    
    # Not Full Tree (node 2 has 1 child)
    #       1
    #      / \
    #     2   3
    #    /
    #   4
    not_full = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    
    print("Is Full:", isFullTree(full))     # Expected: True
    print("Is Full:", isFullTree(not_full)) # Expected: False