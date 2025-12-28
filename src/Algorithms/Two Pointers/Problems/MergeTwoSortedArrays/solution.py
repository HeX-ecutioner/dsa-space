# Problem: Given two sorted arrays a and b, merge them into a single sorted array.
from typing import List

def merge_sorted(a: List[int], b: List[int]) -> List[int]:
    """
    Returns a new merged sorted list containing all elements from a and b.
    Time: O(n+m), Space: O(n+m)
    Approach: Use two pointers to traverse both arrays; build result.
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

# Example usage:
print(merge_sorted([1,3,5], [2,4,6])) # Output: [1,2,3,4,5,6]
print(merge_sorted([10, 20, 30], [15, 25, 35])) # Output: [10,15,20,25,30,35]