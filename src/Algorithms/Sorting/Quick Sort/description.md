# Quick Sort

## Description
Quick Sort is a fast, in-place, Divide & Conquer sorting algorithm.
It works by selecting a pivot, partitioning the array around that pivot,
and recursively sorting the left and right sides.

Unlike Merge Sort, Quick Sort does not need extra memory for merging,
making it very efficient in practice.

---

## How It Works
1. Choose a pivot element (commonly the last element).
2. Partition the array:
   - Elements smaller than the pivot go to the left.
   - Elements greater than the pivot go to the right.
3. Recursively sort the left half.
4. Recursively sort the right half.
5. The array becomes sorted without any merging step.

---

## Example

Input:
[10, 7, 8, 9, 1, 5]

Choose pivot = 5  
Partition → [1] [5] [10, 7, 8, 9]

Then:
Left side: [1] is already sorted  
Right side: sort [10, 7, 8, 9] recursively

Output:
[1, 5, 7, 8, 9, 10]

---

## Algorithm Steps
1. If array range has 0 or 1 elements → already sorted.
2. Partition the array around a pivot.
3. Recursively apply Quick Sort to:
   - The left portion
   - The right portion

---

## Pseudocode
```yaml
quick_sort(arr, low, high):
if low < high:
pivot_index = partition(arr, low, high)
quick_sort(arr, low, pivot_index - 1)
quick_sort(arr, pivot_index + 1, high)

partition(arr, low, high):
pivot = arr[high]
i = low - 1
for j from low to high - 1:
if arr[j] < pivot:
i++
swap(arr[i], arr[j])
swap(arr[i+1], arr[high])
return i + 1
```

---

## Time Complexity
Worst Case: O(n²)  
(Occurs when pivot is always smallest or largest, e.g., sorted array)

Average Case: O(n log n)  
Best Case: O(n log n)

## Space Complexity
O(log n) due to recursion stack  
(Quick Sort is in-place except for recursion)

---

## Notes
- Extremely fast in practice, especially with good pivot selection.
- Used widely in real-world systems.
- Python's built-in `sort()` does NOT use Quick Sort; it uses Timsort.
- Quick Sort's performance depends heavily on pivot strategy.
