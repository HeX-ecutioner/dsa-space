"""
Problem: Implement an AVL Tree Insertion
Statement: Build an AVL tree that automatically balances itself using tree rotations after an insertion.
"""

class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1 # New nodes are added at leaves, height 1

class AVLTree:
    # Time Complexity: O(log N) for Insertion (including re-balancing).
    # Space Complexity: O(log N) for the recursion stack.
    
    def get_height(self, root):
        if not root: return 0
        return root.height
        
    def get_balance(self, root):
        if not root: return 0
        return self.get_height(root.left) - self.get_height(root.right)
        
    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        
        # Perform rotation
        y.right = z
        z.left = T3
        
        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        return y # New root
        
    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        
        # Perform rotation
        y.left = z
        z.right = T2
        
        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        return y # New root

    def insert(self, root, val):
        # 1. Standard BST Insert
        if not root:
            return AVLNode(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
            
        # 2. Update height of ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        # 3. Get the balance factor to check whether it became unbalanced
        balance = self.get_balance(root)
        
        # 4. If unbalanced, there are 4 cases:
        
        # Case 1: Left Left (Requires Right Rotation)
        if balance > 1 and val < root.left.val:
            return self.right_rotate(root)
            
        # Case 2: Right Right (Requires Left Rotation)
        if balance < -1 and val > root.right.val:
            return self.left_rotate(root)
            
        # Case 3: Left Right
        if balance > 1 and val > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
            
        # Case 4: Right Left
        if balance < -1 and val < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
            
        return root

    def preorder(self, root, res=None):
        if res is None: res = []
        if not root: return res
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)
        return res

# Example usage
if __name__ == "__main__":
    avl = AVLTree()
    root = None
    
    # Inserting in sorted order would normally create a Degenerate Linked List.
    # The AVL tree will automatically rotate to keep it balanced!
    for val in [10, 20, 30, 40, 50, 25]:
        root = avl.insert(root, val)
        
    # Preorder traversal reveals the new balanced root is 30
    print("Preorder after AVL balancing:", avl.preorder(root)) 
    # Expected: [30, 20, 10, 25, 40, 50]