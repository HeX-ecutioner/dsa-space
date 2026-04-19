# SKIP LIST — PROBABILISTIC LINKED DATA STRUCTURE

A Skip List is an advanced linked structure that allows O(log n) average time
for search, insertion, and deletion.

## Idea:
Instead of one linked list, we maintain multiple "levels":
- Level 0 → normal linked list
- Higher levels → skip over elements (like express lanes)

## Key Insight:
Each node randomly appears in higher levels, forming a layered structure.

## Why it works:
Randomization keeps the structure balanced (like a tree, but simpler).

## Time Complexity (Average):
- Search: O(log n)
- Insert: O(log n)
- Delete: O(log n)

## Space Complexity:
- O(n log n) due to multiple pointers

## Used in:
- Redis
- Databases
- Ordered sets/maps