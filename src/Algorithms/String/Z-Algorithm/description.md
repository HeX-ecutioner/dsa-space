# Z-Algorithm

## Description
The Z-Algorithm computes a Z-array where each index stores the length of the longest
substring starting at that index which is also a prefix of the string. It enables fast pattern matching in linear time.

## Core Idea
For a string S:
Z[i] = length of longest substring starting at i that matches the prefix of S

Pattern matching is done by constructing:
leading pattern + '$' + text

## Example
`String: "aabxaabxcaabxaabxay"` -> 
Z-array reveals prefix matches efficiently.


## Algorithm Steps
1. Maintain a window [L, R] called the Z-box
2. If i is inside Z-box, reuse previous information
3. Expand matches when needed
4. Update Z-box accordingly


### Time Complexity: O(n)
### Space Complexity: O(n)

## Notes
- Elegant linear-time algorithm
- Often compared with KMP
- Useful beyond pattern matching (string analysis problems)