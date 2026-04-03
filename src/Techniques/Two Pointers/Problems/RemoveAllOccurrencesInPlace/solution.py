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

# Example usage:
arr = [3, 2, 2, 3, 4]
val_to_remove = 3
new_length = remove_element(arr, val_to_remove)
print(f"New length: {new_length}, Modified array: {arr[:new_length]}")
# The order of elements can be changed. It doesn't matter what you leave beyond the new length