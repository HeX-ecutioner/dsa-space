# Remove All Occurrences of a Value In-Place
# Problem: Given array and value val, remove all instances of val in-place and return new length.
from typing import List

def remove_element(nums: List[int], val: int) -> int:
    """
    Use two pointers: write pointer for next kept position, read pointer scans.
    Time: O(n), Space: O(1)
    """
    write = 0
    for read in range(len(nums)):
        if nums[read] != val:
            nums[write] = nums[read]
            write += 1
    return write

# Example:
# arr = [3,2,2,3], val=3 -> returns 2, arr becomes [2,2,...]
