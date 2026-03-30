# Min Heap

## Overview
A Min Heap is a **Complete Binary Tree** where the value of each parent node is strictly **less than or equal to** the values of its children. This means the absolute smallest element in the tree is always guaranteed to be at the root.

## Memory Representation
Because it is a Complete Binary Tree, it is almost always implemented using an **Array** (or ArrayList) rather than node pointers to save memory and optimize CPU caching.
* Parent: `(i - 1) // 2`
* Left Child: `2i + 1`
* Right Child: `2i + 2`

## Applications
* Implementing Priority Queues.
* Dijkstra's Shortest Path Algorithm.
* Sorting (HeapSort).