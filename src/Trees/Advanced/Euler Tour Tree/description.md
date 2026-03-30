# Euler Tour Tree (Tree Flattening)

## Overview
An Euler Tour Tree isn't a physical tree structure; it is a **technique** used to flatten a tree into a 1D array. 

## How it works
You run a DFS on the tree. You append a node to an array when you **enter** it, and you append it again when you **exit** it (or backtrack from it). 
This records the "Entry Time" and "Exit Time" for every node.

## Why is this brilliant?
Once flattened, every subtree in the original tree perfectly aligns as a contiguous subarray. You can then use a **Segment Tree** or **Fenwick Tree** on this flat array to perform `O(log N)` range updates on entire subtrees!