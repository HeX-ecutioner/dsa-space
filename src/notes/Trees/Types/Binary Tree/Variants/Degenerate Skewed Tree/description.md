# Degenerate (Skewed) Tree

## Overview
A Degenerate Tree (or Skewed Tree) is a tree where every internal node has exactly one child. 

## The Nightmare Scenario
This is the absolute worst-case scenario for a Binary Tree. Structurally, it has degraded into a simple **Linked List**.

## Complexity
Because it behaves like a Linked List, traversing it or searching for a value drops from logarithmic `O(log N)` to linear `O(N)` time. Avoiding this shape is the entire reason Self-Balancing Trees (AVL/Red-Black) were invented.