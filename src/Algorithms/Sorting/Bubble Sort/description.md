# Bubble Sort

## Description
Bubble Sort is a simple comparison-based sorting algorithm. It repeatedly steps through the array, compares adjacent elements, and swaps them if they are in the wrong order.

After each full pass through the array, the largest unsorted element "bubbles up" to its correct position at the end of the array.

Bubble Sort is one of the easiest algorithms to understand, making it a great starting point for learning sorting.

## Example

Input:
[5, 1, 4, 2, 8]

Pass 1:
[1, 4, 2, 5, 8]

Pass 2:
[1, 2, 4, 5, 8]

Pass 3:
[1, 2, 4, 5, 8]  (no swap → sorted)

Output:
[1, 2, 4, 5, 8]


## Algorithm Steps
1. Iterate from index 0 to n-1  
2. Compare each pair of adjacent elements  
3. If they are in the wrong order, swap them  
4. After each pass, the largest remaining element settles at the end  
5. Stop early if no swaps occur (optimization)


## Pseudocode
```yaml
repeat n-1 times:
swapped = false
for j from 0 to n-i-2:
if arr[j] > arr[j+1]:
swap(arr[j], arr[j+1])
swapped = true
if not swapped:
break
```

## Time Complexity
- **Worst Case:** O(n²)  
- **Average Case:** O(n²)  
- **Best Case:** O(n) (when the array is already sorted, with early-stop optimization)

## Space Complexity
- **O(1)** — Bubble Sort is an in-place sorting algorithm.

## Notes
- Bubble Sort is not used in production due to poor performance.  
- However, it is excellent for understanding element swapping and sorting fundamentals.  
- The early-stop optimization makes it much faster on nearly-sorted arrays.
