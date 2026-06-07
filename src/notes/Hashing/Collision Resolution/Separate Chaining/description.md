# Separate Chaining

Separate Chaining is a widely used collision resolution technique where the hash table is an array of pointers (or references) to linked lists (or other data structures like BSTs). 

When multiple keys hash to the same index, their key-value pairs are simply appended to the linked list located at that index.

## Core Operations

### Insertion
1. Compute the hash index for the key: `index = hash(key) % capacity`
2. Go to `array[index]`.
3. Traverse the linked list at that index.
   - If the key already exists, update its value.
   - If the key does not exist, insert the new key-value pair as a new node (usually at the head of the list for O(1) insertion).

### Searching
1. Compute the hash index.
2. Go to `array[index]`.
3. Traverse the linked list, comparing the target key with the key in each node.
4. Return the value if found, or `null` if the end of the list is reached.

### Deletion
1. Compute the hash index.
2. Go to `array[index]`.
3. Traverse the linked list. If the node containing the key is found, remove it using standard linked list deletion logic (updating the `next` pointer of the previous node).

## Pros and Cons

**Advantages:**
- **Simple implementation:** Deletion is straightforward, unlike Open Addressing where tombstones are needed.
- **Robust against high Load Factors:** The hash table never truly "fills up". Even if the load factor (λ) exceeds 1.0, the table continues to function (though performance degrades to O(λ)).
- **Less sensitive to clustering:** Unlike linear probing, chaining doesn't suffer from primary clustering.

**Disadvantages:**
- **Cache performance:** Linked list nodes are dynamically allocated and scattered across the heap. This leads to poor CPU cache locality compared to Open Addressing, which uses a contiguous array.
- **Memory overhead:** Every element requires an extra pointer (the `next` reference) for the linked list node.

## Modern Optimizations
In modern implementations like Java's `java.util.HashMap`, Separate Chaining is used, but with a clever optimization:
If a single bucket (linked list) gets too long (e.g., > 8 elements), the linked list is dynamically transformed into a **Balanced Binary Search Tree (Red-Black Tree)**. 
This guarantees that the worst-case search time degrades to **O(log N)** instead of **O(N)**, protecting the application against malicious Hash Denial-of-Service attacks.
