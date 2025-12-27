# Remove Duplicates from Sorted Array (in-place)
# Problem: Given sorted array, remove duplicates in-place and return new length.
# Approach: Two pointers: `write` position and `read` scanner.
from typing import List

def remove_duplicates(nums: List[int]) -> int:
    """
    Modify nums in-place so that each unique element appears only once.
    Return the new length.
    Time: O(n), Space: O(1)
    """
    if not nums:
        return 0

    write = 1  # next position to write unique element
    for read in range(1, len(nums)):
        # when a new value is found, write it and advance write
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write

# Example:
# nums = [1,1,2] -> returns 2, nums becomes [1,2,...]
