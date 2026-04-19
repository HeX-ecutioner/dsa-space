# 🛠️ Manual Dynamic Array

## Overview
A dynamic array (like Python's `list` or Java's `ArrayList`) appears to have an infinite size, but under the hood, it is built on top of a **fixed-size static array**. This manual implementation demonstrates how that abstraction is achieved.

## Core Mechanics
1. **Size vs. Capacity:** * **Size:** The actual number of elements the user has added.
   * **Capacity:** The total number of slots available in the underlying static array.
2. **Dynamic Resizing:** When `size == capacity`, the array has run out of space. It must allocate a brand new, larger array (usually 2x the size) and copy all existing elements into it.

## Complexity
* **Time:** $O(1)$ amortized for appending. The rare $O(N)$ resize operation is mathematically spread out across all the cheap $O(1)$ operations.
* **Space:** $O(N)$ to store the elements, plus some overhead for the unused capacity.