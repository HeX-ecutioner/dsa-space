"""
Problem: K-D Tree Nearest Neighbor (Simplified)
Statement: Find the closest point in a 2D space to a target point using 
spatial partitioning to prune unnecessary search branches.
"""

class KDNode:
    def __init__(self, point, axis):
        self.point = point
        self.axis = axis
        self.left = None
        self.right = None

class KDTreeSearch:
    # Time Complexity: O(log N) average for search.
    # Space Complexity: O(log N) recursion stack.

    def build(self, points, depth=0):
        if not points: return None
        
        axis = depth % 2 # Alternating X (0) and Y (1)
        points.sort(key=lambda x: x[axis])
        mid = len(points) // 2
        
        node = KDNode(points[mid], axis)
        node.left = self.build(points[:mid], depth + 1)
        node.right = self.build(points[mid+1:], depth + 1)
        return node

    def find_nearest(self, root, target, best=None):
        if root is None: return best
        
        # Distance squared to avoid expensive square root calls
        def dist_sq(p1, p2):
            return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

        if best is None or dist_sq(target, root.point) < dist_sq(target, best):
            best = root.point
            
        axis = root.axis
        # Decide which side to search first
        if target[axis] < root.point[axis]:
            near_side, far_side = root.left, root.right
        else:
            near_side, far_side = root.right, root.left
            
        best = self.find_nearest(near_side, target, best)
        
        # Crucial Pruning: Only search the far side if it's mathematically 
        # possible for a closer point to exist there.
        if (target[axis] - root.point[axis])**2 < dist_sq(target, best):
            best = self.find_nearest(far_side, target, best)
            
        return best

if __name__ == "__main__":
    points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
    tree = KDTreeSearch()
    root = tree.build(points)
    target = (9, 2)
    print("Nearest neighbor to (9, 2):", tree.find_nearest(root, target)) # Expected: (8, 1)