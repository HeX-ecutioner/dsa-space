# Problem: Given an integer array nums, handle multiple queries of the following type:
# Calculate the sum of the elements of nums between indices left and right inclusive.
from typing import List

class NumArray:
    """
    Approach: 1D Prefix Sum.
    Instead of iterating from left to right for every query (which takes O(N) per query),
    we precalculate the cumulative sum up to each index.
    
    prefix[i] will store the sum of nums[0] to nums[i-1].
    To find the sum between `left` and `right`, we just do:
    prefix[right + 1] - prefix[left]
    
    Time: O(N) to initialize, O(1) per query.
    Space: O(N) to store the prefix sum array.
    """
    def __init__(self, nums: List[int]):
        # We make the prefix array 1 element larger to handle queries starting at index 0 easily
        self.prefix_sums = [0] * (len(nums) + 1)
        
        # Precompute the prefix sums
        for i in range(len(nums)):
            self.prefix_sums[i + 1] = self.prefix_sums[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # sumRange(L, R) = prefix[R+1] - prefix[L]
        return self.prefix_sums[right + 1] - self.prefix_sums[left]

# Example usage:
# Array: [-2, 0, 3, -5, 2, -1]
numArray = NumArray([-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2)) # Output: 1  (Sum of -2 + 0 + 3)
print(numArray.sumRange(2, 5)) # Output: -1 (Sum of 3 + -5 + 2 + -1)
print(numArray.sumRange(0, 5)) # Output: -3 (Sum of all elements)
