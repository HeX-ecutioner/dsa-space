# Linear Search variants (three useful problems)
from typing import List

# Find the first index of 'target' in arr. Returns the index (0-based) or -1 if not found
def linear_find_index(arr: List[int], target: int) -> int:
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1

# Count how many times 'target' appears in arr. Useful for frequency problems or verifying simple counts before using hashing
def linear_count_occurrences(arr: List[int], target: int) -> int:
    count = 0
    for x in arr:
        if x == target:
            count += 1
    return count

# Return the first element (value) in arr that is > threshold. This demonstrates scanning with a predicate
def linear_first_greater(arr: List[int], threshold: int) -> int:
    for x in arr:
        if x > threshold:
            return x
    return None  # Return None if no such element exists
