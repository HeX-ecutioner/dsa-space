# Problem: Given sorted array, find minimum absolute difference between any two elements
from typing import List
import sys

def min_diff_sorted(nums: List[int]) -> int:
    """
    Assumes nums is sorted. If not, sort first: O(n log n)
    After sorting, minimal difference is among adjacent elements.
    Time: O(n) after sort, Space: O(1)
    Approach: Adjacent elements in sorted order minimize difference -> single pass.
    """
    if len(nums) < 2:
        return 0  # or some sentinel
    min_diff = sys.maxsize
    for i in range(1, len(nums)):
        min_diff = min(min_diff, nums[i] - nums[i-1])
    return min_diff

# Example usage:
print(min_diff_sorted([1,3,4,8,13])) # Output: 1 (between 3 and 4)