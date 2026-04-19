"""
Problem: Check if a Binary Tree is Degenerate (Skewed)
Statement: Determine if a given binary tree is degenerate (every internal node has exactly one child).
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isDegenerate(root):
    # Time Complexity: O(N)
    # Space Complexity: O(N) for the recursive call stack.
    
    if not root:
        return True # Empty tree is technically degenerate
        
    # If it's a leaf, it's valid
    if not root.left and not root.right:
        return True
        
    # If it has TWO children, it is NOT degenerate
    if root.left and root.right:
        return False
        
    # Recurse down the only existing path
    if root.left:
        return isDegenerate(root.left)
    else:
        return isDegenerate(root.right)

# Example usage
if __name__ == "__main__":
    # Degenerate Tree (Right Skewed)
    # 1
    #  \
    #   2
    #    \
    #     3
    skewed = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    
    # Normal Tree
    normal = TreeNode(1, TreeNode(2), TreeNode(3))
    
    print("Is Skewed:", isDegenerate(skewed)) # Expected: True
    print("Is Skewed:", isDegenerate(normal)) # Expected: False