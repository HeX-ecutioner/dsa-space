# Bloom Filters

A **Bloom Filter** is a space-efficient **probabilistic data structure** used to test whether an element is a member of a set. 

It is designed to be incredibly fast and use very little memory, but it comes with a unique trade-off: **False Positives are possible, but False Negatives are impossible.**

*   If a Bloom filter says "Key is NOT in the set", it is **100% definitely not in the set**.
*   If a Bloom filter says "Key IS in the set", it **might be in the set** (or it might be a false positive).

## How it Works

### 1. Structure
A Bloom filter consists of:
- A bit array of size `m`, all initially set to `0`.
- `k` different, independent hash functions.

### 2. Insertion
To insert an element (e.g., "apple"):
1. Pass "apple" through all `k` hash functions.
2. Each hash function produces an index from `0` to `m-1`.
3. Set the bit at each of these `k` indices in the bit array to `1`.

### 3. Lookup (Searching)
To check if an element (e.g., "banana") is in the set:
1. Pass "banana" through the same `k` hash functions.
2. Check the bits at the resulting `k` indices.
3. If **any** of the bits are `0`, "banana" is DEFINITELY NOT in the set.
4. If **all** `k` bits are `1`, "banana" is PROBABLY in the set.

*(Why "probably"? Because those bits might have been set to 1 by the insertion of other, different elements. This is a false positive.)*

### 4. Deletion
You **cannot delete** from a standard Bloom Filter. If you try to change a 1 to a 0, you might accidentally "delete" another element that hashed to that same bit. (There are variations like *Counting Bloom Filters* that support deletion).

## Use Cases
Bloom filters are heavily used in System Design and large-scale applications to save expensive operations (like disk reads or network calls):

- **Databases (Cassandra, HBase):** Before doing an expensive disk seek to find a row, the database checks a Bloom filter in RAM. If it says "Not Present", the disk read is skipped entirely.
- **Web Browsers:** Google Chrome used Bloom filters to check if a URL was in its "malicious URL" database before making a network request.
- **CDNs (Content Delivery Networks):** Akamai uses Bloom filters to avoid caching "one-hit wonder" assets, only caching them if they've been seen before.

## Time and Space Complexity
- **Time Complexity:** `O(k)` for both insertion and search. Because `k` is a small constant, this is effectively **O(1)**.
- **Space Complexity:** Extremely small. You can store information about millions of elements using just a few megabytes.
