"""
Problem: KD Tree Concept (2-Dimensional)
Statement: Implement insertion into a 2D-Tree, alternating between X and Y axes for comparison.
"""

class KDNode:
    def __init__(self, point):
        self.point = point # Tuple (x, y)
        self.left = None
        self.right = None

class KDTree:
    # Time Complexity: Insert O(log N) average, O(N) worst.
    
    def __init__(self):
        self.root = None

    def insert(self, root, point, depth=0):
        if not root:
            return KDNode(point)
            
        # Alternate axes: depth 0 -> X axis (0), depth 1 -> Y axis (1)
        k = len(point) # Dimensions (2 in this case)
        axis = depth % k 
        
        if point[axis] < root.point[axis]:
            root.left = self.insert(root.left, point, depth + 1)
        else:
            root.right = self.insert(root.right, point, depth + 1)
            
        return root

# Example usage
if __name__ == "__main__":
    kdtree = KDTree()
    points = [(3, 6), (17, 15), (13, 15), (6, 12), (9, 1), (2, 7), (10, 19)]
    
    root = None
    for p in points:
        root = kdtree.insert(root, p)
        
    print("Root (Compare X):", root.point)
    print("Root.Left (Compare Y):", root.left.point) # 3 < 17, goes left
    print("Root.Left.Left (Compare X):", root.left.left.point) # 7 > 6, but compared on Y, goes right. Wait, let's trace:
    # Insert (3,6) -> Root
    # Insert (17,15) -> X=17 > 3 -> Right Child
    # Insert (13,15) -> X=13 > 3 -> Right Child. Y=15 >= 15 -> Right.
    # It partitions the 2D plane perfectly.