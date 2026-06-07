# Hashing

Hashing is a powerful data structure technique used to map data of arbitrary size (keys) to fixed-size values (hash codes or indices), typically for incredibly fast data retrieval and storage.

## Core Idea
The core idea behind hashing is to use a **Hash Function** to translate a piece of data (like a string, an object, or an integer) into a small, predictable integer. This integer serves as an index into an array (often called a Hash Table or Hash Map) where the actual data (or a reference to it) is stored.

This allows us to look up, insert, or delete data in **O(1) average time complexity**, compared to O(log N) for binary search trees or O(N) for linear searches in arrays or linked lists.

## Key Components

1. **Hash Function:** A deterministic algorithm that takes a key and produces an integer index. A good hash function is fast to compute and distributes keys evenly across the array.
2. **Hash Table (or Hash Map):** The underlying array where data is stored.
3. **Collision Resolution Strategy:** Because the number of possible keys usually vastly exceeds the size of the array, multiple keys will inevitably hash to the *same index*. This is called a **collision**. The strategy dictates how we handle this scenario (e.g., Separate Chaining, Open Addressing).

## Time and Space Complexity

| Operation | Average Case | Worst Case (Many Collisions) |
| :--- | :--- | :--- |
| **Search** | O(1) | O(N) |
| **Insert** | O(1) | O(N) |
| **Delete** | O(1) | O(N) |

**Space Complexity:** O(N), where N is the number of elements stored.

## The Load Factor

The **Load Factor (λ)** is a critical metric for hash tables.
`λ = (Number of elements stored) / (Total size of the Hash Table array)`

As the load factor increases (the table gets fuller), the probability of collisions rises, degrading the O(1) performance towards O(N). To maintain performance, hash tables dynamically resize (usually doubling the underlying array) when the load factor crosses a specific threshold (e.g., 0.75 in Java's `HashMap`).

## When to use Hashing?
- When extremely fast O(1) lookups are required.
- When finding duplicates or frequencies.
- Caching and memoization.
- Implementing sets (collections of unique elements).

## When NOT to use Hashing?
- When you need data sorted or ordered. Hash tables intrinsically destroy any natural ordering of data.
- When finding elements within a specific range (e.g., "find all users aged 20 to 30"). A Binary Search Tree is much better suited for this.
- When memory is highly constrained (hash tables often allocate more memory than strictly necessary to keep the load factor low).
