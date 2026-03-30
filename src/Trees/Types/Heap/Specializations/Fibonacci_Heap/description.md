# Fibonacci Heap

## Overview
The Fibonacci Heap is the pinnacle of theoretical priority queues. It is a collection of trees (similar to a Binomial Heap), but it operates on "Lazy Evaluation". It doesn't consolidate its trees or enforce strict degrees until you actively call `pop_min()`.

## The God-Tier Complexity
Because it delays doing work until absolutely necessary, it achieves breathtaking amortized time complexities:
* **Insert:** $O(1)$
* **Merge two heaps:** $O(1)$
* **Decrease Key:** $O(1)$ amortized
* **Pop Min:** $O(\log N)$ amortized

## Use Case
It is the mathematically optimal data structure for **Dijkstra's Algorithm** for shortest paths in massive, dense graphs. However, the hidden constant factors are so high that standard Binary Heaps are usually faster in practical real-world software.