# Search in rotated sorted arrays (no duplicates / with duplicates)
from typing import List


def search_rotated_no_dup(arr: List[int], target: int) -> int:
    """
    Search for target in a rotated sorted array that has NO duplicates.
    Returns index if found, else -1.

    Key idea:
    - For any mid, one side (left or right) is strictly sorted.
    - Check if target lies within that sorted side. If yes, narrow to that side;
      otherwise search the other side.
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid

        # If left half is sorted
        if arr[low] <= arr[mid]:
            # If target is in left half
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # Right half must be sorted
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


def search_rotated_with_dup(arr: List[int], target: int) -> int:
    """
    Search for target in rotated sorted array that MAY contain duplicates.

    Problem with duplicates:
    - If arr[low] == arr[mid] == arr[high], we cannot deduce which half is sorted.
    - Strategy: shrink the interval by one from both sides (low++, high--) and continue.
      This makes worst-case degrade to O(n) when many duplicates exist, but it handles
      the general case correctly.

    Returns index if found, else -1.
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid

        # Ambiguous case due to duplicates
        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1
        elif arr[low] <= arr[mid]:
            # Left half is sorted (or equal but not both ends)
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # Right half is sorted
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


# Demo when run directly
if __name__ == "__main__":
    a_no_dup = [6, 7, 8, 1, 2, 3, 4, 5]
    print("no-dup array:", a_no_dup)
    print("search 3 ->", search_rotated_no_dup(a_no_dup, 3))  # expected index of 3

    a_with_dup = [2, 2, 2, 3, 4, 2]
    print("with-dup array:", a_with_dup)
    print("search 3 ->", search_rotated_with_dup(a_with_dup, 3))  # expected index of 3
