# Linear Search

## Description
Linear Search (a.k.a. sequential search) scans elements one-by-one
until it finds a match or reaches the end. It's the simplest search method
and works on unsorted data.

This folder contains three practical variants:
1. Find index of target
2. Count occurrences of target
3. Find first element greater than a threshold (predicate scan)

---

## Example
arr = [4, 2, 7, 2, 9]

- Find index of 7 -> 2
- Count occurrences of 2 -> 2
- First element > 5 -> 7

---

## Algorithm Steps
1. Start from the first element.
2. For each element, check condition (== target or > threshold).
3. If condition matches, return result.
4. If loop ends, return sentinel (e.g., -1 or None).

## Pseudocode
```yaml
for i from 0 to n-1:
if arr[i] matches condition:
return result
return not-found
```

## Time Complexity
- Worst/Average/Best: O(n) (best-case O(1) if first element matches)

## Space Complexity
- O(1) (in-place scanning)

## Notes
- Use linear search on small arrays or unsorted data.
- For repeated queries on the same array, prefer building a hash map for O(1) queries.