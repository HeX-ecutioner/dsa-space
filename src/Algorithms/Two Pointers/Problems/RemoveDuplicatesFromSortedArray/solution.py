# Problem: Given sorted array, remove duplicates in-place and return new length
from typing import List

def remove_duplicates(nums: List[int]) -> int:
    """
    Approach: Modify nums in-place so that each unique element appears only once.
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

# Example usage:
arr = [1, 1, 2, 2, 3]
new_length = remove_duplicates(arr)
print(f"New length: {new_length}, Modified array: {arr[:new_length]}")