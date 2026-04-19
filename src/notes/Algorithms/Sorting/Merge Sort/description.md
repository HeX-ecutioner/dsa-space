# Merge Sort

## Description
Merge Sort is a classic Divide & Conquer sorting algorithm.
It works by recursively splitting an array into halves, sorting each half,
and then merging the sorted halves together.

It is one of the most efficient general-purpose sorting algorithms and forms
the foundation of many real-world sorting implementations.

---

## Why Merge Sort Is Important
- Guaranteed **O(n log n)** time
- Extremely stable, predictable performance
- Excellent for teaching recursion and divide & conquer
- Ideal for sorting linked lists as well

---

## Example

Input:
[38, 27, 43, 3, 9, 82, 10]

Divide:
[38, 27, 43, 3]       [9, 82, 10]
[38, 27] [43, 3]      [9, 82] [10]
[38] [27] [43] [3]    [9] [82] [10]

Conquer (sort each tiny list):
[27, 38] [3, 43]      [9, 82] [10]

Merge:
[3, 27, 38, 43]       [9, 10, 82]
Final merge:
[3, 9, 10, 27, 38, 43, 82]

---

## Algorithm Steps
1. If the array has 0 or 1 elements, it is already sorted.
2. Divide the array into left and right halves.
3. Recursively sort both halves.
4. Merge the two sorted halves into one sorted array.

---

## Pseudocode
```yaml
merge_sort(arr):
if length of arr <= 1:
return arr
mid = length(arr) / 2
left = merge_sort(arr[0:mid])
right = merge_sort(arr[mid:])
return merge(left, right)
```
```yaml
merge(left, right):
result = []
while both lists are non-empty:
take the smaller element and append to result
append any remaining elements
return result
```

---

## Time Complexity
- **Worst Case:** O(n log n)
- **Average Case:** O(n log n)
- **Best Case:** O(n log n)

## Space Complexity
- **O(n)** due to temporary arrays used during merging

---

## Notes
- Merge Sort is **stable** (keeps equal elements in original order).
- Not in-place because it requires additional storage.
- Performs extremely well on large data sets.
- Foundation for understanding Quick Sort and many advanced algorithms.