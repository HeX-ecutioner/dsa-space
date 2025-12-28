# Knuth–Morris–Pratt (KMP)

## Description
KMP is an optimized string matching algorithm that eliminates **redundant comparisons**
performed by naive pattern matching.

It achieves this by preprocessing the pattern to capture information about its internal structure.

## Core Insight
When a mismatch occurs, the pattern itself contains information about how far it can be shifted
without re-checking previously matched characters.

This information is stored in the **LPS array** (Longest Prefix which is also Suffix).


## Example
Pattern: "ABABCABAB"
LPS:     [0,0,1,2,0,1,2,3,4]

When a mismatch happens at a certain index, KMP uses the LPS array to decide
the next comparison position instantly.


## Algorithm Steps
### Preprocessing (Pattern)
1. Build LPS array for the pattern
2. LPS[i] = length of longest proper prefix of P[0..i] that is also a suffix

### Searching
1. Compare text and pattern characters
2. On match, advance both pointers
3. On mismatch, use LPS to shift pattern without moving text pointer back


### Time Complexity:
- Preprocessing: O(m)
- Searching: O(n)

### Space Complexity: O(m)

## Notes
- Guarantees linear time
- Deterministic (no probability of failure)
- One of the most important string algorithms in DSA