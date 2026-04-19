# Fenwick Tree (Binary Indexed Tree / BIT)

## Overview
A Fenwick Tree solves the exact same problem as a Segment Tree (Range Queries and Point Updates in `O(log N)`), but it uses highly optimized **bitwise operations** to do it in much less space and with much less code.

## How it works
It relies on the fact that every integer can be represented as a sum of powers of 2. 
Each index `i` in the Fenwick array stores the sum of a specific range of numbers, dictated by the **Lowest Common Set Bit** of `i`.

## Trade-offs
* **Pros:** Extremely easy to code, uses strict `O(N)` memory (no `4*N` overhead like Segment Trees), incredibly fast bitwise math.
* **Cons:** Cannot easily do Range Min/Max queries, mostly restricted to Range Sums/Frequencies.