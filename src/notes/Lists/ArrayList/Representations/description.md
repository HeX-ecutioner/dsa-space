# ArrayList Representation

## Logical Representation

An ArrayList is a dynamic data structure that stores elements in a contiguous block of memory. It behaves like an array but can automatically resize when elements are added or removed. Elements are accessed using indices, allowing constant-time random access. Unlike linked lists, ArrayLists maintain elements in sequential memory locations, enabling efficient traversal and indexing.

## Physical Representation

ArrayLists are implemented using an underlying array that resizes dynamically when capacity is exceeded.

### Dynamic Array:
- Elements are stored in contiguous memory locations.
- Supports constant-time access using indices.
- Automatically resizes when capacity is reached (typically doubles in size).

### Resizing Behavior:
- When the array is full, a new larger array is created.
- Existing elements are copied to the new array.
- This ensures amortized constant time for insertions.

### Capacity vs Size:
- Size: Number of elements currently stored.
- Capacity: Total allocated space in the underlying array.
- Capacity is always greater than or equal to size.

## Index and Capacity Management

### ArrayLists are accessed using index-based operations:

- Index Access: Direct access using arr[i] in O(1) time.
- Append Operation:
    - If capacity is available → insert directly.
    - If full → resize array and then insert.
- Insert at Index: Elements are shifted to the right.
- Delete at Index: Elements are shifted to the left.
- Resizing: Capacity increases (commonly ×2 growth).

## ArrayList Operations Example

```
Initial ArrayList:

[]

Append 1:

[1]

Append 2:

[1, 2]

Insert 3 at index 0:

[3, 1, 2]

Delete element at index 0:

[1, 2]  // 3 is removed
```

## Index Movement and Resizing

```
Initial capacity = 2

After inserting 1: size = 1
After inserting 2: size = 2 (capacity full)

Insert 3:
→ Resize to capacity = 4
→ Copy elements
→ New array: [1, 2, 3]

Access index:
arr[0] → 1
arr[1] → 2
arr[2] → 3
```

## Key Characteristics
- Contiguous memory allocation
- Fast random access (O(1))
- Slower insert/delete in middle (O(n) due to shifting)
- Amortized O(1) append operation
- Cache-friendly due to sequential storage