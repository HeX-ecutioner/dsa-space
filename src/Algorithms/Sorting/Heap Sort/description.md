# Heap Sort

## Description
Heap Sort is an efficient, comparison-based sorting algorithm that uses
a binary heap data structure. It builds a max heap from the input and
then repeatedly extracts the maximum element, placing it at the end of
the array.

Heap Sort is always O(n log n) and sorts the array in place.

---

## Why Heap Sort Matters
- Always performs in **O(n log n)** time.
- Uses a **binary heap**, an essential data structure.
- Helps you understand priority queues and heap-based algorithms.
- Works entirely in-place (unlike Merge Sort).

---

## Example

Input:
[12, 11, 13, 5, 6, 7]

Max heap constructed:
[13, 11, 12, 5, 6, 7]

Extract 13 → place at end  
Heapify remaining  
Extract 12 → place at end  
...

Output:
[5, 6, 7, 11, 12, 13]

---

## Algorithm Steps
1. Build a max heap from the array.
2. Swap the root (max element) with the last element.
3. Decrease heap size by 1.
4. Heapify the root to restore max-heap property.
5. Repeat until all elements are placed in correct order.

---

## Pseudocode
```yaml
heap_sort(arr):
build max heap
for i from n-1 down to 1:
swap(arr[0], arr[i])
heapify(arr, size = i, root = 0)
```
```yaml
heapify(arr, size, i):
largest = i
left = 2i + 1
right = 2i + 2

if left < size and arr[left] > arr[largest]:
    largest = left
if right < size and arr[right] > arr[largest]:
    largest = right

if largest != i:
    swap(arr[i], arr[largest])
    heapify(arr, size, largest)
```

---

## Time Complexity
Worst Case:   O(n log n)  
Average Case: O(n log n)  
Best Case:    O(n log n)

## Space Complexity
O(1) (in-place)

---

## Notes
- Very consistent performance.
- Not stable (reordering of equal elements may change).
- Foundation for priority queues.
- Good algorithm to transition from sorting → heaps topic.