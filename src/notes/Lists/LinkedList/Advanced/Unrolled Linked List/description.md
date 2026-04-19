# UNROLLED LINKED LIST — HYBRID DATA STRUCTURE

An Unrolled Linked List is a variation of a linked list where each node
stores multiple elements (like a small array), instead of just one.

## Idea:
- Each node contains a block (array) of elements
- Nodes are linked like a normal linked list
- Reduces pointer overhead and improves cache performance

## Why it exists:
- Normal linked lists → poor cache locality
- Arrays → expensive insert/delete in middle
- Unrolled LL → combines benefits of both

## Time Complexity (Average):
- Search: O(n)
- Insert: O(n)
- Delete: O(n)

## Space:
- Better than linked list (fewer pointers)

## Used in:
- Text editors
- Memory-efficient systems