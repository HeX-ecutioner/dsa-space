# Open Addressing

Open addressing is a collision resolution technique in hash tables where all elements are stored *directly within the hash table array itself*. There are no separate data structures like linked lists (as used in separate chaining).

When a collision occurs (two keys hash to the same index), we probe (search) for the next available empty slot in the array.

## Core Operations

### Insertion
1. Compute the hash index for the key.
2. If the slot is empty, insert the key-value pair there.
3. If the slot is occupied, probe the array for the next empty slot using a specific probing sequence.
4. Insert the element in the first empty slot found.

### Searching
1. Compute the hash index.
2. If the slot contains the key, return the value.
3. If the slot is empty, the key is NOT in the table.
4. If the slot is occupied by a *different* key, probe the array following the exact same sequence used during insertion.
5. Stop when the key is found, or an empty slot is encountered (meaning the key doesn't exist).

### Deletion
Deletion is tricky in Open Addressing. If you simply empty a slot, you might break the probing sequence for other elements that were inserted after a collision at that slot.
**Solution:** Use a special marker (often called a "Tombstone" or "Deleted" flag).
1. Search for the key.
2. Instead of emptying the slot, mark it as "Deleted".
3. When searching, treat "Deleted" slots as occupied (keep probing).
4. When inserting, "Deleted" slots can be overwritten.

## Probing Techniques

### 1. Linear Probing
The simplest probing method. We check the slots sequentially: `index`, `index + 1`, `index + 2`, etc. (wrapping around to the start of the array if we reach the end).
*   **Formula:** `P(i) = (hash(key) + i) % M`, where `i` is the probe number (0, 1, 2...)
*   **Problem:** Suffers from **Primary Clustering**. Blocks of occupied slots tend to grow together, leading to longer and longer probe sequences and degrading performance.

### 2. Quadratic Probing
Instead of probing linearly, the interval between probes increases quadratically.
*   **Formula:** `P(i) = (hash(key) + c1*i + c2*i^2) % M` (Often simply `P(i) = (hash(key) + i^2) % M`)
*   **Problem:** Solves Primary Clustering but can suffer from **Secondary Clustering** (keys that hash to the same initial index follow the exact same probing sequence).

### 3. Double Hashing
Uses a secondary hash function to determine the step size for probing.
*   **Formula:** `P(i) = (hash1(key) + i * hash2(key)) % M`
*   **Advantage:** The best of the three. It avoids both primary and secondary clustering because the probe sequence depends on the key itself, not just the initial hash index.

## Load Factor limitations
For Open Addressing, the Load Factor (λ) *must* be strictly less than 1.0 (the table cannot store more elements than its array size). Practically, performance degrades sharply when λ > 0.7, so resizing is crucial.
