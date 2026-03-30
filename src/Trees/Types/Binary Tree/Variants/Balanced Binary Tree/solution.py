"""
Problem: Check if a Binary Tree is Balanced
Statement: Given a binary tree, determine if it is height-balanced.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
    # Time Complexity: O(N) - We visit each node once.
    # Space Complexity: O(H) - Recursion stack equals the height of the tree.
    
    def check_height(node):
        if not node:
            return 0
            
        left_height = check_height(node.left)
        if left_height == -1: return -1 # Left subtree is unbalanced
        
        right_height = check_height(node.right)
        if right_height == -1: return -1 # Right subtree is unbalanced
        
        # If the current node is unbalanced, return -1 to signal failure up the chain
        if abs(left_height - right_height) > 1:
            return -1
            
        # Return actual height of this subtree
        return max(left_height, right_height) + 1

    # If check_height returns -1, it's not balanced.
    return check_height(root) != -1

# Example usage
if __name__ == "__main__":
    # Balanced Tree
    #       1
    #      / \
    #     2   3
    balanced_root = TreeNode(1, TreeNode(2), TreeNode(3))
    
    # Unbalanced Tree
    #       1
    #      /
    #     2
    #    /
    #   3
    unbalanced_root = TreeNode(1, TreeNode(2, TreeNode(3)))
    
    print("Is Tree 1 Balanced?", isBalanced(balanced_root))     # Expected: True
    print("Is Tree 2 Balanced?", isBalanced(unbalanced_root))   # Expected: False