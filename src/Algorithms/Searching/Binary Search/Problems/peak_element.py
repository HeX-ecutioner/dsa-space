# Find any peak element in an array where a peak means strictly greater than neighbors
from typing import List

def find_peak_element(nums: List[int]) -> int:
    """
    Find index of any peak element. A peak is an element strictly greater than its neighbors.
    For i = 0 or i = n-1 endpoints, treat out-of-bounds as negative infinity, so endpoints can be peaks.

    Key observation:
    - If nums[mid] < nums[mid+1], there is a rising slope; a peak must exist to the right.
    - Otherwise, there is a peak at mid or to the left.
    - This yields a binary-search-like approach that finds a peak in O(log n).
    """
    n = len(nums)
    if n == 0:
        return -1
    low, high = 0, n - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] < nums[mid + 1]:
            # slope rising to the right, so peak is to the right
            low = mid + 1
        else:
            # slope falling, so a peak is at mid or to the left
            high = mid
    # low == high points to a peak index
    return low


if __name__ == "__main__":
    arr = [1, 2, 1, 3, 5, 6, 4]
    idx = find_peak_element(arr)
    print("array:", arr)
    print("peak index:", idx, "value:", arr[idx])
