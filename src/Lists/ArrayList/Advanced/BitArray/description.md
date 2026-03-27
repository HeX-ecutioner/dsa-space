# 🧬 Bit Array (Bitset)

## Overview
A Bit Array is an incredibly space-efficient data structure used to store a large sequence of boolean values (True/False or 1/0). Instead of using a full byte (or multiple bytes) for a single boolean, it packs up to 32 or 64 boolean values into a single integer.

## How It Works
It relies heavily on **bitwise operators**:
* **Left Shift (`<<`)**: Used to target a specific bit position.
* **Bitwise OR (`|`)**: Used to set a bit to 1.
* **Bitwise AND (`&`)**: Used to check if a bit is 1.

## When to Use It
* Bloom Filters.
* Sieve of Eratosthenes (finding prime numbers).
* Extremely memory-constrained environments where millions of flags are needed.