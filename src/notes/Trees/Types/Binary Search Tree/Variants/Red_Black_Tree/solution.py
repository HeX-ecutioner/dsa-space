"""
Problem: Red-Black Tree Structural Concept
Statement: Demonstrate the core Node structure and the concept of Left-Leaning Red-Black (LLRB) tree insertion (a simplified variant of standard RB trees).
Note: Full RB-Tree deletion is notoriously long; this focuses on the core insertion/coloring logic.
"""

class Node:
    def __init__(self, val, color="RED"):
        self.val = val
        self.left = None
        self.right = None
        self.color = color # New nodes are always inserted as RED

class RedBlackTree:
    # Time Complexity: O(log N)
    # Space Complexity: O(log N) recursion depth
    
    def __init__(self):
        self.root = None

    def is_red(self, node):
        if not node: return False
        return node.color == "RED"

    def rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = "RED"
        return x

    def rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = "RED"
        return x

    def flip_colors(self, node):
        node.color = "RED"
        node.left.color = "BLACK"
        node.right.color = "BLACK"

    def _insert(self, node, val):
        if not node:
            return Node(val)

        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)

        # Fix violations (LLRB rules)
        # 1. Right child is Red, Left child is Black -> Rotate Left
        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotate_left(node)
            
        # 2. Left child is Red, Left.Left child is Red -> Rotate Right
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotate_right(node)
            
        # 3. Both children are Red -> Flip Colors
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)

        return node

    def insert(self, val):
        self.root = self._insert(self.root, val)
        self.root.color = "BLACK" # Root must always be black

# Example usage
if __name__ == "__main__":
    rb_tree = RedBlackTree()
    for val in [10, 20, 30, 15, 25]:
        rb_tree.insert(val)
    print(f"Root is: {rb_tree.root.val}, Color: {rb_tree.root.color}") # Expected: 20, BLACK