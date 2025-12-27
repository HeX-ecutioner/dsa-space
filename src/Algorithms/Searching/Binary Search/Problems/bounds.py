# Implementations of lower_bound (first index with value >= x) and upper_bound (first index with value > x)
from typing import List


def lower_bound(arr: List[int], x: int) -> int:
    """
    Returns the smallest index i such that arr[i] >= x.
    If all elements are < x, returns len(arr).

    Implementation detail:
    - We use the half-open interval pattern [low, high)
      with initial low=0, high=len(arr).
    - Invariant: the answer is in [low, high).
    - Termination when low == high; that's the answer.
    """
    low, high = 0, len(arr)
    while low < high:
        mid = low + (high - low) // 2
        # If arr[mid] is less than x, answer must be to the right
        if arr[mid] < x:
            low = mid + 1
        else:
            # arr[mid] >= x: mid could be answer, keep it in the interval
            high = mid
    # low == high; either in-bounds index or len(arr)
    return low


def upper_bound(arr: List[int], x: int) -> int:
    """
    Returns the smallest index i such that arr[i] > x.
    If no such index exists, returns len(arr).

    Uses identical half-open pattern as lower_bound, but condition uses <=.
    """
    low, high = 0, len(arr)
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] <= x:
            # we need strictly greater, so ignore mid and left
            low = mid + 1
        else:
            high = mid
    return low


# Demo when run directly
if __name__ == "__main__":
    arr = [1, 2, 2, 2, 3, 5]
    print("array:", arr)
    print("lower_bound(arr, 2) ->", lower_bound(arr, 2))  # expect 1
    print("upper_bound(arr, 2) ->", upper_bound(arr, 2))  # expect 4
