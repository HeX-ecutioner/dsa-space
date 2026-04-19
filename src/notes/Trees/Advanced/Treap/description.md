# Treap (Tree + Heap)

## Overview
A Treap is a randomized Binary Search Tree. It assigns a **random priority** to every node upon insertion. 

## The Dual Invariant
1. **BST Property:** Keys strictly follow left < parent < right.
2. **Heap Property:** Priorities strictly follow parent > children (Max Heap).

## Why randomization?
By assigning random priorities and rotating the tree to satisfy the Heap property, the tree structure becomes completely randomized. Mathematical probability guarantees that a randomly shaped BST has an average height of `O(log N)`, effectively making it a self-balancing tree without the nightmare logic of AVL/Red-Black rotations.