# Design HashMap

**Difficulty:** Easy

Design a HashMap without using any built-in hash table libraries.

Implement the `MyHashMap` class:
- `MyHashMap()` initializes the object with an empty map.
- `void put(int key, int value)` inserts a `(key, value)` pair into the HashMap. If the `key` already exists in the map, update the corresponding `value`.
- `int get(int key)` returns the `value` to which the specified `key` is mapped, or `-1` if this map contains no mapping for the `key`.
- `void remove(int key)` removes the `key` and its corresponding `value` if the map contains the mapping for the `key`.

## Approach: Separate Chaining
Since we cannot use built-in hash map libraries, we must implement our own array of "buckets". To handle collisions (when two keys hash to the same bucket index), we will use **Separate Chaining** via Linked Lists.

1.  **Array:** Create a fixed-size array (e.g., size 1000). The index is calculated as `key % 1000`.
2.  **Linked List:** Each bucket in the array will contain a dummy head node of a Linked List.
3.  **Put:** Hash the key, traverse the linked list at that bucket. If the key exists, update the value. If not, append a new node.
4.  **Get:** Hash the key, traverse the linked list. Return the value if found, else -1.
5.  **Remove:** Hash the key, traverse the linked list. If found, bypass the node by pointing `prev.next` to `curr.next`.

## Complexity
- **Time Complexity:** $O(N / K)$ on average, where $N$ is the number of total keys and $K$ is the number of predefined buckets (1000 here). Assuming keys are evenly distributed, this is effectively $O(1)$. In the worst case (all keys hash to the same bucket), it's $O(N)$.
- **Space Complexity:** $O(K + M)$, where $K$ is the number of buckets and $M$ is the number of unique keys inserted (nodes created).
