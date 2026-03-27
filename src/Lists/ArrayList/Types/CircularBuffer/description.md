# ⭕ Circular Buffer (Ring Buffer)

## Overview
A Circular Buffer is a fixed-size array that connects end-to-end. It is the perfect structure for implementing a **Queue** using an array.

## The Problem It Solves
In a standard array, removing an item from the front (index 0) requires shifting every other element to the left, which takes $O(N)$ time.

## How It Works
A Circular Buffer uses two pointers (`head` and `tail`). When you add or remove items, the pointers move forward. When a pointer hits the end of the array, it uses **modulo arithmetic** to wrap back around to index 0. This allows both insertions and deletions at the ends to happen in **$O(1)$ time** without any shifting.