# Problem: Find minimum absolute difference window or smallest distance between any pair from arrays
from typing import List
import sys

def min_diff_between_arrays(A: List[int], B: List[int]) -> int:
    """
    Use two pointers i,j on sorted A,B to find minimal |A[i]-B[j]|.
    Time: O(len(A)+len(B))
    """
    i, j = 0, 0
    best = sys.maxsize
    while i < len(A) and j < len(B):
        best = min(best, abs(A[i] - B[j]))
        # move pointer with smaller value
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    return best

# Example usage:
print(min_diff_between_arrays([1,3,15,11,2], [23,127,235,19,8])) # Output: 8
print(min_diff_between_arrays([10,20,14,16,18], [30,23,54,33,96])) # Output: 10