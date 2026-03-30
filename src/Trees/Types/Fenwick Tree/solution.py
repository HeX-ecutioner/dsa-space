"""
Problem: Implement a Fenwick Tree (Binary Indexed Tree)
Statement: Implement a BIT to support O(log N) point updates and prefix sum queries using bitwise isolated lowest set bits.
"""

class FenwickTree:
    # Time Complexity: Update O(log N), Query O(log N)
    # Space Complexity: O(N)
    
    def __init__(self, size):
        # 1-based indexing is required for Fenwick tree bitwise math to work
        self.tree = [0] * (size + 1)

    def update(self, i, delta):
        """ Add 'delta' to element at index 'i' (1-based index) """
        # Add delta, then move to the next responsible node by ADDING the lowest set bit
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i) # i & (-i) isolates the lowest set bit

    def query(self, i):
        """ Returns the sum from index 1 to i """
        total = 0
        # Add current node, then move to parent by SUBTRACTING the lowest set bit
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)
        return total
        
    def range_query(self, left, right):
        """ Returns sum from left to right inclusive (1-based indices) """
        return self.query(right) - self.query(left - 1)

# Example usage
if __name__ == "__main__":
    arr = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
    bit = FenwickTree(len(arr))
    
    # Initialize the BIT
    for i in range(len(arr)):
        bit.update(i + 1, arr[i])
        
    print("Prefix sum up to index 5:", bit.query(5)) # 3 + 2 - 1 + 6 + 5 = 15
    print("Range sum from 2 to 6:", bit.range_query(2, 6)) # 2 - 1 + 6 + 5 + 4 = 16