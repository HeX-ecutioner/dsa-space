"""
Problem: Binary Tree Fundamentals (Traversals)
Statement: Implement a standard Binary Tree node and demonstrate all four core traversal methods: Preorder, Inorder, Postorder, and Level Order.
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTreeTraversals:
    # Time Complexity: O(N) for all traversals since every node is visited exactly once.
    # Space Complexity: O(H) for DFS (recursion stack), O(W) for BFS where W is max width.

    def inorder(self, root):
        """ Left -> Node -> Right """
        res = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res

    def preorder(self, root):
        """ Node -> Left -> Right """
        res = []
        def dfs(node):
            if not node: return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res

    def postorder(self, root):
        """ Left -> Right -> Node """
        res = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res

    def level_order(self, root):
        """ Top to Bottom, Left to Right (BFS) """
        if not root: return []
        res = []
        queue = deque([root])
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(level)
        return res

# Example usage
if __name__ == "__main__":
    # Constructing a simple tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3)
    
    bt = BinaryTreeTraversals()
    print("Inorder:   ", bt.inorder(root))    # Expected: [4, 2, 5, 1, 3]
    print("Preorder:  ", bt.preorder(root))   # Expected: [1, 2, 4, 5, 3]
    print("Postorder: ", bt.postorder(root))  # Expected: [4, 5, 2, 3, 1]
    print("Level Order:", bt.level_order(root)) # Expected: [[1], [2, 3], [4, 5]]