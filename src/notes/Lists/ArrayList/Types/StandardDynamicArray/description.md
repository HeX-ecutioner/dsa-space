# 📦 Standard Dynamic Array

## Overview
The Standard Dynamic Array is the default implementation of a list in modern programming (e.g., Java's `ArrayList`, C++ `std::vector`, Python's `list`).

## Core Vibe
It is an abstraction over contiguous memory that prioritizes **read speed**. Because memory is continuous, calculating the exact memory address of any index is instant.

## Key Performance Metrics
* **Index Lookup:** $O(1)$
* **Append (End):** Amortized $O(1)$
* **Insert/Delete (Middle):** $O(N)$ - requires shifting elements.
* **Cache Locality:** Excellent. The CPU can load chunks of the array into its fastest memory, making iteration drastically faster than linked lists.