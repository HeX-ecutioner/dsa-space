# General Tree (N-ary Tree)

## Overview
A General Tree (often called an N-ary tree) is the most flexible form of a tree data structure. Unlike Binary Trees, which restrict nodes to a maximum of two children (left and right), a node in an N-ary tree can have **any number of children**.

## Memory Representation
Because the number of children is completely dynamic, we cannot hardcode `left` and `right` pointers. Instead, every node contains a **List (or Array) of pointers** to its children.

## Real-World Applications
This is actually the most commonly used tree in daily computing!
* **File Systems:** A folder can contain 0, 1, or 100 subfolders/files.
* **The DOM (Document Object Model):** An HTML `<div>` can contain any number of child elements.
* **Organizational Charts:** A manager can have multiple direct reports.
* **JSON/XML parsing.**

## Complexity
* **Time:** `O(N)` for searching and traversal, as there is no sorting or balancing property to rely on.
* **Space:** `O(N)` to store the nodes, plus `O(H)` for the recursion stack during traversal.