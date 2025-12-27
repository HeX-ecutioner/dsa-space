# Radix Sort

## Description
Radix Sort is a non-comparison sorting algorithm that sorts numbers
digit by digit. It typically uses **Counting Sort** as a stable
subroutine to sort based on each digit.

Radix Sort is extremely fast when the range of digits is small
(e.g., base 10 integers). It has linear time complexity relative
to the number of digits.

---

## How Radix Sort Works
Given a list of integers:

1. Sort the numbers by the **ones** digit.
2. Sort by the **tens** digit.
3. Sort by the **hundreds** digit.
4. Continue until all digits of the largest number are processed.

Sorting each digit must be **stable** so that earlier digit orderings
are preserved — this is why Counting Sort is ideal.

---

## Example

Input:
[170, 45, 75, 90, 802, 24, 2, 66]

Pass 1 (ones place):
[170, 90, 802, 2, 24, 45, 75, 66]

Pass 2 (tens place):
[802, 2, 24, 45, 66, 170, 75, 90]

Pass 3 (hundreds place):
[2, 24, 45, 66, 75, 90, 170, 802]

Output:
[2, 24, 45, 66, 75, 90, 170, 802]

---

## Algorithm Steps
1. Find the maximum number to determine the number of digits.
2. For each digit position (1s, 10s, 100s, ...):
   - Use Counting Sort to sort the array by that digit.
3. After the final digit pass, the entire array is sorted.

---

## Pseudocode
```yaml
radix_sort(arr):
max_val = max(arr)
exp = 1
while max_val / exp > 0:
counting_sort(arr, exp)
exp *= 10
```

---

## Time Complexity
Let:
- n = number of elements
- d = number of digits
- b = base (10 for integers)

Time: **O(n · d)**  
Space: **O(n + b)**

---

## Notes
- Works best for integers and fixed-length data.
- Requires a stable inner sort (Counting Sort).
- Very fast for large datasets with limited digit size.
- Not a comparison-based sort → not limited by O(n log n).
