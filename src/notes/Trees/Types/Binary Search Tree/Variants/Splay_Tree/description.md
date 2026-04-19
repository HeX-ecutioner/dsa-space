# Splay Tree

## Overview
A Splay Tree is a self-adjusting Binary Search Tree. It does not enforce strict mathematical balance (like AVL or Red-Black). Instead, it uses a heuristic: **recently accessed elements are moved to the root** so they can be accessed faster next time.

## How it works (Splaying)
Whenever a node is searched, inserted, or deleted, a "Splay" operation is performed. This operation uses rotations (Zig, Zig-Zig, and Zig-Zag) to pull that specific node all the way up to the root of the tree.

## When to use it
Excellent for building **Caches** or situations with a highly skewed access pattern (the "80/20 rule", where 80% of lookups request the same 20% of data).

## Complexity
* **Time:** Amortized `O(log N)`. However, a single operation can take `O(N)` in the worst case if the tree happens to be currently skewed.