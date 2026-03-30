"""
Problem: N-ary Tree Fundamentals
Statement: Implement a generic N-ary tree node and demonstrate its core traversals.
Note: "Inorder" traversal is not standard for N-ary trees because there is no clear "middle" 
between an arbitrary number of children. We use Preorder, Postorder, and Level Order.
"""
from collections import deque

class NaryNode:
    def __init__(self, val=0, children=None):
        self.val = val
        # If no children are provided, initialize an empty list
        self.children = children if children is not None else []

class NaryTreeTraversals:
    # Time Complexity: O(N) for all traversals.
    # Space Complexity: O(H) for DFS, O(W) for BFS (where W is the max width).

    def preorder(self, root):
        """ Node -> All Children (Left to Right) """
        res = []
        def dfs(node):
            if not node: return
            # 1. Process the node itself first
            res.append(node.val)
            # 2. Iterate through the dynamic list of children
            for child in node.children:
                dfs(child)
        
        dfs(root)
        return res

    def postorder(self, root):
        """ All Children (Left to Right) -> Node """
        res = []
        def dfs(node):
            if not node: return
            # 1. Process all children first
            for child in node.children:
                dfs(child)
            # 2. Process the node itself last
            res.append(node.val)
            
        dfs(root)
        return res

    def level_order(self, root):
        """ Top to Bottom, Left to Right (BFS) """
        if not root: return []
        res = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # Append all children to the queue
                for child in node.children:
                    queue.append(child)
                    
            res.append(current_level)
            
        return res

# Example usage
if __name__ == "__main__":
    # Constructing an N-ary Tree:
    #        1
    #     /  |  \
    #    2   3   4
    #   / \      |
    #  5   6     7
    
    root = NaryNode(1, [
        NaryNode(2, [NaryNode(5), NaryNode(6)]),
        NaryNode(3),
        NaryNode(4, [NaryNode(7)])
    ])
    
    tree = NaryTreeTraversals()
    print("Preorder:   ", tree.preorder(root))    # Expected: [1, 2, 5, 6, 3, 4, 7]
    print("Postorder:  ", tree.postorder(root))   # Expected: [5, 6, 2, 3, 7, 4, 1]
    print("Level Order:", tree.level_order(root)) # Expected: [[1], [2, 3, 4], [5, 6, 7]]