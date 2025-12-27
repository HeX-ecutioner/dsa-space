# Binary Search demonstration (standard iterative + a simple main)
from typing import List

# Classic iterative binary search on a *sorted* array. Returns index of 'target' if found, else -1
def binary_search(arr: List[int], target: int) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2 # To prevent potential overflow
        if arr[mid] == target:
            return mid # Target found
        elif arr[mid] < target:
            low = mid + 1 # Adjust search range
        else:
            high = mid - 1 # Adjust search range
    return -1 # Target not found

# Recursive version of binary search
def binary_search_rec(arr: List[int], target: int, low: int, high: int) -> int:
    if low > high:
        return -1  # Base case: not found

    mid = low + (high - low) // 2 
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_rec(arr, target, mid + 1, high) 
    else:
        return binary_search_rec(arr, target, low, mid - 1)

# Example demonstrating usage and printing result
if __name__ == "__main__":
    nums = [1, 3, 4, 6, 8, 9, 12]
    targets = [6, 2, 12]

    print("Iterative Binary Search Results:")
    for t in targets:
        idx = binary_search(nums, t)
        print(f"  target={t} -> index={idx}")

    print("\nRecursive Binary Search Results:")
    for t in targets:
        idx = binary_search_rec(nums, t, 0, len(nums) - 1)
        print(f"  target={t} -> index={idx}")
