# XOR LINKED LIST — MEMORY-OPTIMIZED LINKED STRUCTURE

A XOR Linked List is a memory-efficient variation of a doubly linked list.

## Idea:
Instead of storing:
prev pointer + next pointer

We store:
XOR(prev_address, next_address)

## Why it works:
Using XOR properties:
A ^ B ^ A = B

If we know the previous node and the XOR value, we can compute the next node.

## Example:
If a node stores:
npx = prev ⊕ next

Then:
next = npx ⊕ prev

This allows traversal in both directions using only one pointer field.

## Advantages:

* Saves memory (only 1 pointer instead of 2)
* Theoretically efficient for memory-constrained systems

## Disadvantages:

* Extremely hard to debug
* Pointer arithmetic required (not supported in Python directly)
* Code becomes non-intuitive and error-prone
* Not compatible with modern garbage collection systems
* Rarely used in real-world applications today

## Important Note:
Python does NOT support pointer arithmetic.
To simulate memory addresses, implementations use id() and dictionaries,
which defeats the original purpose of memory optimization.

## Why Deletion Is Not Implemented in solution.py

Deletion in an XOR Linked List is significantly more complex than in
standard linked lists.

To delete a node, we must:

1. Traverse while maintaining the previous node's address
2. Recompute both adjacent nodes using XOR operations
3. Carefully update both neighbors' npx values

Even a single mistake in XOR manipulation can corrupt the entire structure.

In low-level languages (like C/C++), this is manageable but still error-prone.

### In Python:

* There is no true pointer arithmetic
* We rely on id() simulation
* Manual memory tracking is required

### This makes deletion:
- Unnecessarily complex
- Misaligned with Python's design philosophy
- Not representative of real-world usage

### Design Decision:
To keep the implementation:

* Educational
* Readable
* Aligned with practical learning

Deletion is intentionally omitted from the code and documented here instead.

## When Should You Care About XOR Linked Lists?

Primarily:

* For understanding pointer-level memory tricks
* For deepening low-level thinking
* For academic completeness in data structures

Not for:

* Interviews
* Production systems
* Practical Python development

## Summary

The XOR Linked List is a clever but largely theoretical data structure that demonstrates how memory can be optimized using bitwise operations. Its value lies not in usage, but in the mental model it builds: thinking in terms of memory, addresses, and transformations.