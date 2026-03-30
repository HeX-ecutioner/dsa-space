# B+ Tree

## Overview
A B+ Tree is an extension of the B-Tree and is the industry standard for Relational Databases (like MySQL, PostgreSQL).

## The Difference from B-Trees
1. **Data only in Leaves:** Internal nodes *only* store keys for routing. Actual data (or database row pointers) are strictly stored in the leaf nodes.
2. **Linked Leaves:** Every leaf node has a pointer to the next leaf node, forming a **Linked List at the bottom layer**.

## Why? (Range Queries)
If you run `SELECT * FROM users WHERE age BETWEEN 20 AND 30`, a B+ tree finds `20` in `O(log N)` time, and then simply walks right along the linked list to collect the rest of the ages in `O(1)` time each, without traversing back up the tree!