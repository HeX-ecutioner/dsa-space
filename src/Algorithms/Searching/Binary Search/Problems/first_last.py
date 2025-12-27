# Find first (leftmost) and last (rightmost) occurrence of a target in a sorted array (with duplicates)
from typing import List


def first_occurrence(arr: List[int], target: int) -> int:
    """
    Returns the index of the first (leftmost) occurrence of `target` in `arr`.
    If target is not present, returns -1.

    Explanation of approach:
    - We perform a binary search (O(log n)).
    - When we find arr[mid] == target, we don't immediately return; instead:
        * record mid as a candidate (ans = mid)
        * continue searching the LEFT half (high = mid - 1) to see if there is an earlier occurrence
    - If arr[mid] < target, we must search right (low = mid + 1).
    - If arr[mid] > target, we search left (high = mid - 1).
    """
    low, high = 0, len(arr) - 1
    ans = -1  # holds best candidate for leftmost index

    # Loop invariant: if target exists, it's within [low, high]; otherwise low > high and loop ends
    while low <= high:
        # mid computed to avoid overflow in languages where it matters
        mid = low + (high - low) // 2

        # Three possibilities:
        if arr[mid] == target:
            # Found a match; record and move left to find leftmost
            ans = mid
            high = mid - 1  # continue searching left half
        elif arr[mid] < target:
            # Target must be in right half
            low = mid + 1
        else:
            # arr[mid] > target => search left half
            high = mid - 1

    return ans


def last_occurrence(arr: List[int], target: int) -> int:
    """
    Returns the index of the last (rightmost) occurrence of `target` in `arr`.
    If target is not present, returns -1.

    Approach mirrors first_occurrence, but when we find a match we search RIGHT half.
    """
    low, high = 0, len(arr) - 1
    ans = -1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            ans = mid
            low = mid + 1  # continue searching right half for a later occurrence
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return ans


# Short demonstration if run directly
if __name__ == "__main__":
    example = [1, 2, 2, 2, 3, 4, 5]
    print("array:", example)
    print("first occurrence of 2 ->", first_occurrence(example, 2))  # expected 1
    print("last  occurrence of 2 ->", last_occurrence(example, 2))  # expected 3
