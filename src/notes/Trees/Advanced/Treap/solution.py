"""
Problem: Treap Implementation (Cartesian Tree Concept)
Statement: Implement the core Node structure and Split/Merge operations of a Treap.
"""
import random

class TreapNode:
    def __init__(self, key):
        self.key = key
        # Assign a random priority to maintain the heap property and balance
        self.priority = random.random()
        self.left = None
        self.right = None

class Treap:
    # Time Complexity: O(log N) expected for all operations.
    # Space Complexity: O(N)
    
    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        return x

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def insert(self, root, key):
        if not root:
            return TreapNode(key)
            
        # Standard BST Insert
        if key <= root.key:
            root.left = self.insert(root.left, key)
            # Fix Heap property via rotation if priority is violated
            if root.left.priority > root.priority:
                root = self.right_rotate(root)
        else:
            root.right = self.insert(root.right, key)
            if root.right.priority > root.priority:
                root = self.left_rotate(root)
                
        return root

    def inorder(self, root, res=None):
        if res is None: res = []
        if root:
            self.inorder(root.left, res)
            res.append((root.key, round(root.priority, 2)))
            self.inorder(root.right, res)
        return res

# Example usage
if __name__ == "__main__":
    t = Treap()
    root = None
    # Insert keys sequentially. A normal BST would become a degenerate O(N) linked list.
    # The Treap's random priorities will force rotations, keeping it balanced!
    for key in [1, 2, 3, 4, 5, 6, 7]:
        root = t.insert(root, key)
        
    print("Inorder Traversal (Key, Priority):", t.inorder(root))
    print("Root is randomly decided by priority:", root.key)