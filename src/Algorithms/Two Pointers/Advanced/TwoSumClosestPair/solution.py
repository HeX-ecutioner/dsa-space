# Two Sum - Closest Pair (min absolute difference to target)
# Problem: Given sorted array and target, find pair whose sum is closest to target.
from typing import List, Tuple

def two_sum_closest(nums: List[int], target: int) -> Tuple[int,int]:
    """
    If nums not sorted, sort while remembering original indices if needed.
    Approach: two pointers left/right, track minimal abs difference.
    Time: O(n log n) to sort, O(n) two-pointer scan.
    Returns pair of values (not indices).
    """
    nums = sorted(nums)
    left, right = 0, len(nums) - 1
    best_pair = (nums[left], nums[right])
    best_diff = abs(nums[left] + nums[right] - target)
    while left < right:
        s = nums[left] + nums[right]
        diff = abs(s - target)
        if diff < best_diff:
            best_diff = diff
            best_pair = (nums[left], nums[right])
        if s > target:
            right -= 1
        else:
            left += 1
    return best_pair

# Example:
# two_sum_closest([ -1,2,1,-4 ], 1) -> (1,0 or similar depending on values)
