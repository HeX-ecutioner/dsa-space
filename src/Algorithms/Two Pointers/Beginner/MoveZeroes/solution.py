# Move Zeroes (in-place)
# Problem: Move all zeros to the end while preserving order of non-zero elements.
# Approach: Use a write pointer to collect non-zero elements and fill remainder with zeros.
from typing import List

def move_zeroes(nums: List[int]) -> None:
    """
    Modifies nums in-place: moves all zeros to the end.
    Time: O(n), Space: O(1)
    Steps:
    - Keep write pointer at 0.
    - Whenever we see non-zero at read pointer, write it at `write`, increment `write`.
    - After loop, fill indices from write..end with zeros.
    """
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1
    # fill remaining positions with zeros
    for i in range(write, len(nums)):
        nums[i] = 0

# Example:
# arr = [0,1,0,3,12] -> after move_zeroes -> [1,3,12,0,0]
