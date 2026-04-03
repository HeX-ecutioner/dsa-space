# Problem: Given a sorted array, find indices of two numbers that sum to target
from typing import List, Optional, Tuple

def two_sum_sorted(nums: List[int], target: int) -> Optional[Tuple[int,int]]:
    """
    Approach: left/right pointers move based on sum comparison.
    Returns a tuple of indices (left, right) of two numbers that sum to target.
    If not found, return None.
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return (left, right)
        elif s < target:
            left += 1
        else:
            right -= 1
    return None

# Example usage:
print(two_sum_sorted([1,2,3,4,6], 6)) # Output: (1,3) representing values 2 and 4
print(two_sum_sorted([2,5,9,11], 11)) # Output: (0,2) representing values 2 and 9