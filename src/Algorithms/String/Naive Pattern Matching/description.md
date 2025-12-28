# Naive Pattern Matching

## Description
Naive Pattern Matching is the most straightforward string searching technique.
It attempts to match a pattern at **every possible position** in the text.

This algorithm does **no preprocessing** and makes no assumptions about the data.
It exists primarily to establish a baseline for more advanced string algorithms.

## Core Idea
Given:
- Text T of length n
- Pattern P of length m

Try to align P with T starting at index 0, then index 1, then index 2, and so on,
comparing characters one by one until:
- A mismatch occurs, or
- The full pattern is matched

## Example
Text:    "ABABDABACDABABCABAB"
Pattern: "ABABCABAB"

Matching attempts occur at indices:
0, 1, 2, 3, ... until a full match is found.

## Algorithm Steps
1. For each index i from 0 to n - m:
2. Compare T[i + j] with P[j] for j = 0 to m - 1
3. If all characters match, record i as a match

### Time Complexity
- Worst case: O(n · m)
- Best case: O(n)

### Space Complexity: O(1)

## Notes
- Extremely simple to implement
- Inefficient for large inputs
- Serves as the conceptual foundation for KMP and Rabin–Karp