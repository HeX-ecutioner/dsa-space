# Segment Tree

## Overview
A Segment Tree is a binary tree used for storing information about intervals or segments. It allows querying which segments contain a given point, or querying sums/minimums over a range of an array.

## Why use it?
If you have an array and want to find the sum from index `L` to `R`, it takes `O(N)`. If you update an index, it takes `O(1)`.
A Segment Tree balances this: it allows **both** updating an element and querying a range sum/min/max in strict **`O(log N)`** time.

## Structure
* The root represents the whole array `[0, N-1]`.
* Each child splits the array in half (e.g., `[0, mid]` and `[mid+1, N-1]`).
* Leaves represent single elements.