"""
Problem: Range Sum Query - Immutable
Statement: Given an integer array nums, handle multiple queries of the following type: Calculate the sum of the elements of nums between indices left and right inclusive.
"""

class NumArray:
    # Time Complexity: O(n) for initialization, O(1) per query.
    # Space Complexity: O(n) to store the prefix sum array.
    
    def __init__(self, nums):
        # Create a prefix sum array where prefix[i] is the sum of elements from index 0 to i-1
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left, right):
        # The sum from left to right is the prefix sum up to right+1 MINUS the prefix sum up to left
        return self.prefix[right + 1] - self.prefix[left]

if __name__ == "__main__":
    numArray = NumArray([-2, 0, 3, -5, 2, -1])
    print("Sum range (0, 2):", numArray.sumRange(0, 2)) # Expected: 1
    print("Sum range (2, 5):", numArray.sumRange(2, 5)) # Expected: -1