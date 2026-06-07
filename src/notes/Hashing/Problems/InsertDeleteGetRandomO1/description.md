# Insert Delete GetRandom O(1)

**Difficulty:** Medium

Implement the `RandomizedSet` class:
- `RandomizedSet()` Initializes the `RandomizedSet` object.
- `bool insert(int val)` Inserts an item `val` into the set if not present. Returns `true` if the item was not present, `false` otherwise.
- `bool remove(int val)` Removes an item `val` from the set if present. Returns `true` if the item was present, `false` otherwise.
- `int getRandom()` Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the **same probability** of being returned.

You must implement the functions of the class such that each function works in **average $O(1)$** time complexity.

## Approach
This is a classic systems-design-style algorithmic problem.
- To achieve $O(1)$ `insert` and `remove`, a **Hash Map** is required.
- To achieve $O(1)$ `getRandom`, an **Array (List)** is required because we need to randomly index into contiguous memory (`arr[random_index]`). You cannot randomly access a Hash Map in $O(1)$.

So, we must combine both!
1.  **List (`nums`)**: Stores the actual values.
2.  **Hash Map (`val_to_index`)**: Stores the mapping of `{value : index_in_nums_list}`.

### How to achieve O(1) Removal?
Removing from the middle of an array takes $O(N)$ because elements must shift left.
**The Trick:** 
1. Swap the element we want to delete with the *last* element in the array.
2. Update the hash map with the new index of the swapped element.
3. Pop the last element from the array (which is $O(1)$).
4. Delete the target element from the hash map.

## Complexity
- **Time Complexity:** $O(1)$ average for all three operations.
- **Space Complexity:** $O(N)$ where $N$ is the number of elements in the set, since we store them in both a list and a hash map.
