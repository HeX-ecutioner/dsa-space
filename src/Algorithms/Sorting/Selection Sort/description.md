# Selection Sort

## Description
Selection Sort is a simple comparison-based sorting algorithm.
It divides the array into two parts:

1. The sorted portion at the beginning.
2. The unsorted portion containing the remaining elements.

During each pass:
- The smallest element from the unsorted section is selected.
- It is then swapped with the first unsorted position.

This gradually grows the sorted portion from left to right.

---

## Example

Input:
[64, 25, 12, 22, 11]

Process:
Select 11 → swap with 64  
Select 12 → swap with 25  
Select 22 → already in correct order  
...

Output:
[11, 12, 22, 25, 64]

---

## Algorithm Steps
1. Iterate from index 0 to n-1  
2. Assume the current index holds the smallest number  
3. Scan the remaining array to find the true minimum  
4. Swap the found minimum into its correct sorted position

---

## Pseudocode
```yaml
for i from 0 to n-1:
min_index = i
for j from i+1 to n-1:
if arr[j] < arr[min_index]:
min_index = j
swap(arr[i], arr[min_index])
```

---

## Time Complexity
- **Worst Case:** O(n²)  
- **Average Case:** O(n²)  
- **Best Case:** O(n²) (even if already sorted, still scans all elements)

## Space Complexity
- **O(1)** (in-place sorting)

---

## Notes
- Selection Sort performs the fewest swaps among simple sorting algorithms.  
- It is easy to understand but inefficient for large datasets.  
- Good for teaching sorting fundamentals.
