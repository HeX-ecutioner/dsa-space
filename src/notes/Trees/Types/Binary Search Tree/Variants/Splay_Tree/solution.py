"""
Problem: Splay Tree Concept
Statement: Implement the 'Splay' operation, which brings a recently accessed node to the root.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class SplayTree:
    # Time Complexity: Amortized O(log N) per operation.
    # Space Complexity: O(log N) average, O(N) worst case for recursion.

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def splay(self, root, key):
        if not root or root.val == key:
            return root

        # Left Subtree
        if key < root.val:
            if not root.left: return root
            
            # Zig-Zig (Left Left)
            if key < root.left.val:
                root.left.left = self.splay(root.left.left, key)
                root = self.right_rotate(root)
            # Zig-Zag (Left Right)
            elif key > root.left.val:
                root.left.right = self.splay(root.left.right, key)
                if root.left.right:
                    root.left = self.left_rotate(root.left)
                    
            return self.right_rotate(root) if root.left else root

        # Right Subtree
        else:
            if not root.right: return root
            
            # Zag-Zig (Right Left)
            if key < root.right.val:
                root.right.left = self.splay(root.right.left, key)
                if root.right.left:
                    root.right = self.right_rotate(root.right)
            # Zag-Zag (Right Right)
            elif key > root.right.val:
                root.right.right = self.splay(root.right.right, key)
                root = self.left_rotate(root)
                
            return self.left_rotate(root) if root.right else root

    def search(self, root, key):
        # Search also splays the node to the root!
        return self.splay(root, key)

# Example usage
if __name__ == "__main__":
    tree = SplayTree()
    root = Node(100)
    root.left = Node(50)
    root.right = Node(200)
    root.left.left = Node(40)
    
    # We search for 40. The Splay tree will rotate 40 all the way to the root.
    new_root = tree.search(root, 40)
    print("New Root after searching 40:", new_root.val) # Expected: 40