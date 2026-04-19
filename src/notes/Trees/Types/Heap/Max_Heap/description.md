# Max Heap

## Overview
A Max Heap is identical to a Min Heap in structure (a Complete Binary Tree stored in an Array), but its ordering rule is inverted: the value of each parent node must be strictly **greater than or equal to** the values of its children. 

## The Core Invariant
The absolute **largest** element in the tree is always sitting at the root (index `0` of the array).

## Python Note
Python's built-in `heapq` library only provides a Min Heap. To use it as a Max Heap in competitive programming, developers multiply the inserted numbers by `-1` before pushing, and `-1` again after popping.