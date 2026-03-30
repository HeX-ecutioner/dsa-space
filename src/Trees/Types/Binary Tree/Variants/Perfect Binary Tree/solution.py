"""
Problem: Check if a Binary Tree is Perfect
Statement: Determine if all internal nodes have 2 children and all leaves are at the exact same depth.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isPerfectTree(root):
    # Time Complexity: O(N) - Must check all nodes.
    # Space Complexity: O(H) - Recursion depth.
    
    # Helper function to find the depth of the leftmost node
    def find_depth(node):
        d = 0
        while node:
            d += 1
            node = node.left
        return d
        
    def check_perfect(node, d, level=0):
        if not node:
            return True
            
        # If it's a leaf node, its level must equal the leftmost depth
        if not node.left and not node.right:
            return d == level + 1
            
        # If an internal node has only one child, it's not perfect
        if not node.left or not node.right:
            return False
            
        # Recurse for left and right children
        return check_perfect(node.left, d, level + 1) and check_perfect(node.right, d, level + 1)

    if not root: return True
    d = find_depth(root)
    return check_perfect(root, d)

# Example usage
if __name__ == "__main__":
    # Perfect Tree
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    perfect = TreeNode(1, 
                       TreeNode(2, TreeNode(4), TreeNode(5)), 
                       TreeNode(3, TreeNode(6), TreeNode(7)))
                       
    print("Is Perfect:", isPerfectTree(perfect)) # Expected: True