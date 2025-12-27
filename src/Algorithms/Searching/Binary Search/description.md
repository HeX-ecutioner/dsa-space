# Binary Search

## Description
Binary Search is an efficient algorithm for finding a target value
in a **sorted** array. It repeatedly divides the search interval in half,
discarding the half that cannot contain the target.

This file includes:
- A classic iterative binary search implementation with a demonstration `main`.
- An "Advanced Problems" section listing common interview variants to practice.

---

## Example
arr = [1, 3, 4, 6, 8, 9, 12]
search 6 -> index 3
search 2 -> -1 (not found)

---

## Algorithm Steps
1. Set low = 0, high = n-1.
2. While low <= high:
   - mid = low + (high - low) // 2
   - If arr[mid] == target → return mid
   - If arr[mid] < target → low = mid + 1
   - Else → high = mid - 1
3. If loop finishes, target not present → return -1

## Pseudocode
```yaml
low = 0; high = n-1
while low <= high:
mid = low + (high - low) // 2
if arr[mid] == target: return mid
if arr[mid] < target: low = mid + 1
else: high = mid - 1
return -1
```

## Time Complexity
- O(log n)

## Space Complexity
- O(1)

---

## Advanced Problems (Included in the folder)
- Find the **first (leftmost)** occurrence of target in a sorted array with duplicates.
- Find the **last (rightmost)** occurrence of target.
- **Lower bound / Upper bound** implementations (first >= x / first > x).
- **Search in a rotated sorted array** (no duplicates & with duplicates).
- **Binary Search on Answer** (minimize/maximize threshold over monotonic predicate).
- **Kth smallest element in a sorted matrix** (use binary search on value).
- **Find peak element** using binary-search-like checks.
- **Integer square root** using binary search.