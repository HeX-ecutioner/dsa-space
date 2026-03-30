# Interval Tree

## Overview
An Interval Tree is an augmented Binary Search Tree designed to hold overlapping intervals (e.g., `[start, end]`). It allows you to efficiently query if a new interval overlaps with *any* existing intervals in $O(\log N)$ time.

## The Augmentation
Every node stores:
1. The **Interval** itself.
2. The **Max Value** of any interval endpoint in its entire subtree.

## Why the Max Value?
When searching for an overlap, the `max` value tells the algorithm if it is mathematically possible for an overlap to exist down a specific path, allowing it to instantly prune (ignore) entire subtrees, achieving the $O(\log N)$ speed.