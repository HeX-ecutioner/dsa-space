# Design HashSet

**Difficulty:** Easy

Design a HashSet without using any built-in hash table libraries.

Implement `MyHashSet` class:
- `void add(key)` Inserts the value `key` into the HashSet.
- `bool contains(key)` Returns whether the value `key` exists in the HashSet or not.
- `void remove(key)` Removes the value `key` in the HashSet. If `key` does not exist in the HashSet, do nothing.

## Approach: Open Addressing vs Separate Chaining
Like `Design HashMap`, we must handle collisions. We can use Separate Chaining (Linked Lists). But for a HashSet where we only store keys (no values), we can also use an array of Binary Search Trees, or simply an array of lists/arrays.

For this implementation, let's use an **Array of Arrays (or Lists)** to demonstrate a slightly different variation of Separate Chaining.

1.  We initialize an array `buckets` of a specific size (e.g., 1000).
2.  The hash function is `hash(key) = key % 1000`.
3.  Each bucket will hold a list of keys.
4.  **Add:** Compute the hash. If the bucket is empty, initialize a list. If the key is not already in that list, append it.
5.  **Contains:** Compute the hash. Check if the bucket has been initialized and if the key exists within the list.
6.  **Remove:** Compute the hash. If the key exists in the list, remove it.

*(Note: If the range of keys is small and known in advance, say $0$ to $10^6$, you could literally just use a boolean array of size $10^6+1$ and set `arr[key] = True`. However, true hashing handles arbitrary or massive keys).*

## Complexity
- **Time Complexity:** $O(N / K)$ where $N$ is the total number of keys and $K$ is the number of buckets (1000). Assuming uniform distribution, list traversal is $O(1)$.
- **Space Complexity:** $O(K + M)$ where $K$ is the number of buckets and $M$ is the number of unique elements added.
