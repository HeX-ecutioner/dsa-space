# Merge Two Sorted Arrays (in-place if space provided OR return merged array)
# Problem: Given two sorted arrays a and b, merge them into a single sorted array.
# Approach: Use two pointers to traverse both arrays; build result.
from typing import List

def merge_sorted(a: List[int], b: List[int]) -> List[int]:
    """
    Returns a new merged sorted list containing all elements from a and b.
    Time: O(n+m), Space: O(n+m)
    """
    i, j = 0, 0
    merged = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    # append any leftovers
    if i < len(a):
        merged.extend(a[i:])
    if j < len(b):
        merged.extend(b[j:])
    return merged

# Example:
# merge_sorted([1,3,5], [2,4,6]) -> [1,2,3,4,5,6]
