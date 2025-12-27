# Max Consecutive Ones with K flips (sliding-window hybrid)
from typing import List

def longest_ones(nums: List[int], k: int) -> int:
    """
    Returns length of longest subarray with at most k zeros (i.e., can flip k zeros to ones).
    Approach: sliding window with two pointers expanding right and shrinking left when zeros > k.
    Time: O(n), Space: O(1)
    """
    left = 0
    zeros = 0
    best = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        best = max(best, right - left + 1)
    return best

# Example:
# longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2) -> 6
