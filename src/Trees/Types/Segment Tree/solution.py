"""
Problem: Implement a Segment Tree (Range Sum Query)
Statement: Build a Segment tree from an array that supports O(log N) point updates and O(log N) range sum queries.
"""

class SegmentTree:
    # Time Complexity: Build O(N), Update O(log N), Query O(log N)
    # Space Complexity: O(N) - Tree array size is 4*N in the worst case.
    
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        if self.n > 0:
            self._build(data, 0, 0, self.n - 1)

    def _build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            
            self._build(data, left_child, start, mid)
            self._build(data, right_child, mid + 1, end)
            
            # Internal node holds the sum of its children
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def update(self, index, val):
        self._update(0, 0, self.n - 1, index, val)

    def _update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            
            if start <= idx <= mid:
                self._update(left_child, start, mid, idx, val)
            else:
                self._update(right_child, mid + 1, end, idx, val)
                
            self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def query(self, L, R):
        return self._query(0, 0, self.n - 1, L, R)

    def _query(self, node, start, end, L, R):
        # 1. Range completely outside
        if R < start or end < L:
            return 0
        # 2. Range completely inside
        if L <= start and end <= R:
            return self.tree[node]
        # 3. Range partially overlaps
        mid = (start + end) // 2
        p1 = self._query(2 * node + 1, start, mid, L, R)
        p2 = self._query(2 * node + 2, mid + 1, end, L, R)
        return p1 + p2

# Example usage
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    seg_tree = SegmentTree(arr)
    
    print("Sum of values in range [1, 3]:", seg_tree.query(1, 3)) # 3 + 5 + 7 = 15
    
    seg_tree.update(1, 10) # Update index 1 from 3 to 10
    print("Sum of range [1, 3] after update:", seg_tree.query(1, 3)) # 10 + 5 + 7 = 22