# Interval List Intersection using two pointers on interval lists
# Problem: Given two lists of disjoint sorted intervals, return their intersection.
from typing import List

def interval_intersection(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """
    Use two pointers i,j for lists A and B.
    For intervals A[i]=[a1,a2], B[j]=[b1,b2], intersection is [max(a1,b1), min(a2,b2)] if valid.
    Advance pointer with smaller endpoint.
    Time: O(len(A)+len(B))
    """
    i, j = 0, 0
    res = []
    while i < len(A) and j < len(B):
        a1, a2 = A[i]
        b1, b2 = B[j]
        # check intersection
        start = max(a1, b1)
        end = min(a2, b2)
        if start <= end:
            res.append([start, end])
        # move the pointer with smaller end
        if a2 < b2:
            i += 1
        else:
            j += 1
    return res

# Example:
# A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# -> intersections combined appropriately.
