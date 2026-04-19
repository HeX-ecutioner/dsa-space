# B-Tree

## Overview
A B-Tree is a self-balancing, **multi-way** search tree. Unlike Binary trees (2 children max), B-Trees can have hundreds of children per node. 

## The Hardware Connection
B-Trees are designed specifically for **Disk Drives (Databases / File Systems)**. Reading from a hard drive is extremely slow. B-Trees make their nodes exactly the same size as a physical "Disk Block" (e.g., 4KB). This allows the computer to read 100+ keys in a single disk rotation, drastically minimizing slow I/O operations.

## Properties
* Every node can contain multiple keys, sorted in ascending order.
* A node with `k` keys always has exactly `k + 1` children.
* All leaf nodes appear on the exact same level.