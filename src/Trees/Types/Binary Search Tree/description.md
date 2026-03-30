# Binary Search Tree (BST)

## Overview
A Binary Search Tree is a binary tree with a strict ordering property. It makes searching for an element highly efficient by acting like a binary search algorithm in tree form.

## The Core Invariant (Rules)
For EVERY node in the tree:
1. All values in its **Left Subtree** are strictly less than the node's value.
2. All values in its **Right Subtree** are strictly greater than the node's value.
3. Both left and right subtrees must also be valid BSTs.

## Complexity
* **Time:** `O(log N)` for Search, Insert, and Delete (Average Case). `O(N)` if the tree becomes degenerate.
* **Space:** `O(log N)` average recursion depth, `O(N)` worst case.