# MULTI-LEVEL LINKED LIST

A Multi-Level Linked List is a linked structure where each node can have:

* A next pointer (same level)
* A child pointer (points to another linked list)

## Structure:
Each node may lead to another list, forming a hierarchy.

Example:
1 → 2 → 3
|
7 → 8
|
11

## Key Idea

Instead of a flat structure:

* Lists can branch into sublists

## Operations

* Insert (next level)
* Insert child
* Traverse (multi-level)
* Flatten (convert into single-level list)

## Flattening

### Important operation:

* Convert multi-level structure into single linked list

### Approaches:

* DFS (depth-first)
* BFS (level-wise)

## Use Cases

* File systems
* DOM trees
* Hierarchical data representation

## Complexity

Depends on structure:

* Traversal → O(n)
* Flatten → O(n)

## Summary

Multi-Level Linked Lists introduce hierarchical relationships into linked structures, bridging the gap between lists and trees.