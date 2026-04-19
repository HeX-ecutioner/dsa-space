# AVL Tree

## Overview
An AVL Tree (named after inventors Adelson-Velsky and Landis) is a **Self-Balancing Binary Search Tree**. It enforces the rule that the tree must always remain a "Balanced Binary Tree".

## How it works
Every node keeps track of a `height` variable. After every insertion or deletion, the tree calculates the **Balance Factor** (`Height(Left) - Height(Right)`). 
If the balance factor falls outside of `[-1, 0, 1]`, the tree automatically performs **Rotations** (Left, Right, Left-Right, or Right-Left) to fix the balance.

## Why use it?
It guarantees that Search, Insert, and Delete operations will **always** run in `O(log N)` time, completely eliminating the risk of Degenerate (Skewed) trees.