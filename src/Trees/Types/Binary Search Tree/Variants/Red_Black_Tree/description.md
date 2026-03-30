# Red-Black Tree

## Overview
A Red-Black Tree is a self-balancing Binary Search Tree (BST) that uses color "labels" (red or black) on each node to ensure the tree remains approximately balanced. It is the underlying data structure for many standard libraries (e.g., C++ `std::map`, Java `TreeMap`).

## The 5 Invariants (Rules)
1. Every node is either **Red** or **Black**.
2. The root is always **Black**.
3. All leaves (NIL/Null nodes) are **Black**.
4. If a node is **Red**, both its children must be **Black** (No two adjacent red nodes on a path).
5. Every path from a given node to any of its descendant NIL nodes contains the **same number of Black nodes**.

## Complexity
* **Time:** `O(log N)` for Search, Insert, and Delete. 
* **Trade-off vs. AVL:** Red-Black trees are slightly less strictly balanced than AVL trees. This means searching is *slightly* slower, but insertions/deletions are *faster* because they require fewer rotations on average.