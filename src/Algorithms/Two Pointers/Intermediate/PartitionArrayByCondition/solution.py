# Partition Array by Condition (two pointers)
# Problem: Partition array so elements satisfying condition are on left (stable not required).
# Example: partition by even/odd, negatives/positives
from typing import List, Callable

def partition_by_condition(nums: List[int], cond: Callable[[int], bool]) -> None:
    """
    In-place partition nums so that elements with cond(x)==True come before others.
    Two-pointer approach: left at 0, right at n-1. Swap when left fails cond and right satisfies cond.
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        if cond(nums[left]):
            left += 1
        elif not cond(nums[right]):
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

# Example:
# nums = [3,1,2,4], cond = lambda x: x%2==0 -> after partition, evens on left, odds on right (order unspecified)
