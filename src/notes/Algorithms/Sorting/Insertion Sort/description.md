# Insertion Sort

## Description
Insertion Sort is a simple and intuitive sorting algorithm.

It works the same way you sort playing cards in your hands:
- You pick one card at a time,
- Compare it with the cards in your sorted hand,
- Shift larger cards to the right,
- Insert the card into the correct position.

This makes Insertion Sort very efficient for:
- Small arrays
- Nearly sorted arrays

---

## Example

Input:
[12, 11, 13, 5, 6]

Process (simplified):
Take 11 → insert before 12  
Take 13 → already in correct place  
Take 5 → shift 12, 11, 13 → insert at start  
Take 6 → insert between 5 and 11  

Output:
[5, 6, 11, 12, 13]

---

## Algorithm Steps
1. Treat the first element as sorted.
2. Pick the next element (the "key").
3. Compare key with elements in the sorted portion.
4. Shift larger elements to the right.
5. Insert the key into its correct position.
6. Repeat for all elements.

---

## Pseudocode
```yaml
for i from 1 to n-1:
key = arr[i]
j = i - 1
while j >= 0 and arr[j] > key:
arr[j+1] = arr[j]
j = j - 1
arr[j+1] = key
```

---

## Time Complexity
- **Worst Case:** O(n²)  
- **Average Case:** O(n²)  
- **Best Case:** O(n) (when array is already sorted)

## Space Complexity
- **O(1)** — In-place algorithm.

---

## Notes
- Much faster than Bubble Sort and Selection Sort on nearly sorted input.  
- Used as a final stage in more advanced algorithms (e.g., Hybrid Sorts).  
- Important for understanding element shifting and insertion logic.  