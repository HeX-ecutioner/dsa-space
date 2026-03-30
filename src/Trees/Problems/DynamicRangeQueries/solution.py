"""
Problem: Range Sum Query - Mutable (LeetCode 307)
Statement: Implement the NumArray class using a Segment Tree to support O(log N) point updates and O(log N) range sum queries.
"""

class NumArray:
    # Time Complexity: Build O(N), Update O(log N), Query O(log N)
    # Space Complexity: O(N) for the segment tree array

    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        
        # Build the tree: insert leaves in the second half of the array
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
            
        # Build the tree: calculate parents in the first half
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, val):
        # Move to the leaf node
        pos = index + self.n
        self.tree[pos] = val
        
        # Bubble up and update the parent nodes
        while pos > 1:
            left = pos
            right = pos
            if pos % 2 == 0:
                right = pos + 1
            else:
                left = pos - 1
                
            pos //= 2
            self.tree[pos] = self.tree[left] + self.tree[right]

    def sumRange(self, left, right):
        # Move to the leaf nodes
        l = left + self.n
        r = right + self.n
        total = 0
        
        while l <= r:
            # If left pointer is a right child, add it and move right
            if l % 2 == 1:
                total += self.tree[l]
                l += 1
            # If right pointer is a left child, add it and move left
            if r % 2 == 0:
                total += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
            
        return total

# Example usage
if __name__ == "__main__":
    nums = [1, 3, 5]
    numArray = NumArray(nums)
    print("Sum range [0, 2]:", numArray.sumRange(0, 2)) # Expected: 9
    
    numArray.update(1, 2) # nums becomes [1, 2, 5]
    print("Sum range [0, 2] after update:", numArray.sumRange(0, 2)) # Expected: 8