# Binary Tree

## Overview
A Binary Tree is a hierarchical data structure in which each node has at most two children, referred to as the **left child** and the **right child**. It is the foundation for almost all advanced tree structures.

## Core Mechanics
* **Traversals:** Because trees are non-linear, we use specific traversal algorithms to visit nodes:
  * **Depth-First Search (DFS):** Preorder (Node, Left, Right), Inorder (Left, Node, Right), Postorder (Left, Right, Node).
  * **Breadth-First Search (BFS):** Level Order (level by level, left to right).

## Complexity
* **Time:** `O(N)` for searching, insertion, and traversal, as there is no specific order to the elements.
* **Space:** `O(H)` where `H` is the height of the tree (due to the recursion stack during DFS).