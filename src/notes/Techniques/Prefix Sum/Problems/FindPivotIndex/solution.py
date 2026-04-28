# Problem: Given an array of integers nums, calculate the pivot index of this array.
# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
from typing import List

def pivot_index(nums: List[int]) -> int:
    """
    Approach: Prefix Sum.
    We can calculate the total sum of the array first.
    Then, as we iterate through the array, we maintain a running `left_sum`.
    At any index `i`, the `right_sum` is simply: `total_sum - left_sum - nums[i]`.
    
    If `left_sum == right_sum`, we have found our pivot index!
    
    Time: O(n) - One pass to calculate total sum, and another pass to find the pivot.
    Space: O(1) - Constant extra space used.
    """
    total_sum = sum(nums)
    left_sum = 0
    
    for i, num in enumerate(nums):
        # Calculate right sum
        right_sum = total_sum - left_sum - num
        
        if left_sum == right_sum:
            return i
            
        # Add the current number to the left sum for the next iteration
        left_sum += num
        
    return -1

# Example usage:
print(pivot_index([1,7,3,6,5,6])) # Output: 3 (Left sum: 1+7+3 = 11. Right sum: 5+6 = 11)
print(pivot_index([1,2,3]))       # Output: -1 (No pivot index exists)
print(pivot_index([2,1,-1]))      # Output: 0 (Left sum: 0. Right sum: 1 + -1 = 0)
