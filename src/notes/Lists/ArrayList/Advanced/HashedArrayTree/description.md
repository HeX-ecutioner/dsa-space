# 🌳 Hashed Array Tree (HAT)

## Overview
A Hashed Array Tree is a dynamic array implementation that mitigates the massive $O(N)$ copying penalty of a standard ArrayList. 

## How It Works
Instead of copying everything into a single, massive new array when it gets full, a HAT maintains a **top-level directory (array)** of pointers that point to **smaller, fixed-size data chunks (arrays)**.
* When it runs out of space, it simply allocates a new small chunk and adds its pointer to the directory.
* Elements are never copied or moved once placed.

## The Advantage
It maintains $O(1)$ random access using math (division to find the chunk, modulo to find the index inside the chunk) while drastically reducing the wasted memory and copying time of standard doubling arrays.