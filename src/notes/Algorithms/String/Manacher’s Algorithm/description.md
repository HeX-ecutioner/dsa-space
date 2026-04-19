# Manacher’s Algorithm

## Description
Manacher’s Algorithm finds the **longest palindromic substring** in linear time. Without it, palindrome detection usually requires O(n²) time.

## Core Idea
- Transform the string to handle even and odd palindromes uniformly
- Use symmetry around palindrome centers
- Reuse previously computed palindrome radii

## Example
Input:  "babad"
Output: "bab" or "aba"


## Algorithm Steps
1. Transform string using separators
2. Maintain center and right boundary
3. Use mirror property to initialize radius
4. Expand when possible
5. Track maximum palindrome


### Time Complexity: O(n)
### Space Complexity: O(n)

## Notes
- One of the most advanced string algorithms
- Often considered difficult but very powerful
- Used in competitive programming and text processing