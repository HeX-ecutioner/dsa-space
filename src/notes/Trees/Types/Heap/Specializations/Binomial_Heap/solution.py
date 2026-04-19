"""
Problem: Binomial Heap Node Concept
Statement: Demonstrate the structure of a Binomial Tree Node and how they link together.
"""

class BinomialNode:
    # A Binomial Node uses the "Left-Child, Right-Sibling" representation
    def __init__(self, val):
        self.val = val
        self.degree = 0      # Number of children
        self.parent = None   # Pointer to parent
        self.child = None    # Pointer to the FIRST child
        self.sibling = None  # Pointer to the NEXT sibling right next to it

def link_binomial_trees(y, z):
    """
    Core Operation: Links two Binomial Trees of the SAME degree.
    Makes tree 'y' a child of tree 'z' (assuming z.val < y.val for Min-Heap).
    """
    y.parent = z
    y.sibling = z.child
    z.child = y
    z.degree += 1
    return z

if __name__ == "__main__":
    # Suppose we have two order-0 trees (just single nodes)
    tree1 = BinomialNode(10)
    tree2 = BinomialNode(5)
    
    # We link them to form an order-1 tree (2 nodes). The smaller becomes the root.
    root = link_binomial_trees(tree1, tree2)
    
    print("Root value:", root.val) # 5
    print("Root degree:", root.degree) # 1
    print("Root's child value:", root.child.val) # 10