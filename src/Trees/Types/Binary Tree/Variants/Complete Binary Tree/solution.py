"""
Problem: Check Completeness of a Binary Tree
Statement: Given the root of a binary tree, determine if it is a complete binary tree.
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isCompleteTree(root):
    # Time Complexity: O(N) - Standard BFS traversal.
    # Space Complexity: O(W) - Queue stores at most one level of nodes.
    
    if not root:
        return True
        
    queue = deque([root])
    encountered_null = False
    
    while queue:
        node = queue.popleft()
        
        if node is None:
            # The moment we see a null, EVERY subsequent node must also be null
            encountered_null = True
        else:
            # If we see a valid node AFTER seeing a null, the tree is not complete
            if encountered_null:
                return False
                
            # Keep adding children, EVEN if they are null
            queue.append(node.left)
            queue.append(node.right)
            
    return True

# Example usage
if __name__ == "__main__":
    # Complete Tree
    #       1
    #      / \
    #     2   3
    #    / \  /
    #   4  5 6
    complete = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
    
    # Incomplete Tree (Gap at left child of 3)
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4  5    7
    incomplete = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(7)))
    
    print("Is Complete:", isCompleteTree(complete))     # Expected: True
    print("Is Complete:", isCompleteTree(incomplete))   # Expected: False