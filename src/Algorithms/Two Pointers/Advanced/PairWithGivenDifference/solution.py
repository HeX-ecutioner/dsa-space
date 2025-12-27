# Pair With Given Difference using two pointers (sorted array)
# Problem: Find if there exists pair (i,j) such that nums[j] - nums[i] == k (k>=0).
from typing import List

def has_pair_with_diff(nums: List[int], k: int) -> bool:
    """
    Sort the array, then use two pointers i and j (i<j):
    - If diff < k -> move j forward
    - If diff > k -> move i forward
    - If diff == k -> found
    Time: O(n log n) for sorting or O(n) if already sorted.
    """
    nums.sort()
    i, j = 0, 1
    n = len(nums)
    while i < n and j < n:
        if i == j:
            j += 1
            continue
        diff = nums[j] - nums[i]
        if diff == k:
            return True
        elif diff < k:
            j += 1
        else:
            i += 1
    return False

# Example:
# has_pair_with_diff([1,5,3,4], 2) -> True (3 and 5 or 1 and 3)
