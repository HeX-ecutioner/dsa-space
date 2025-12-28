# Rabin–Karp Algorithm

## Description
Rabin–Karp is a string matching algorithm based on **hashing**.
Instead of comparing characters directly, it compares hash values of substrings. It is especially useful when searching for **multiple patterns** in a text.

## Core Idea
1. Compute a hash for the pattern
2. Compute rolling hashes for substrings of the text
3. Compare hashes instead of characters
4. Verify characters only when hashes match

## Example
Text:    "GEEKS FOR GEEKS"
Pattern: "GEEK"

Hashes are computed for:
"GEEK", "EEKS", "EKS ", "KS F", ...

Only matching hashes trigger character comparison.

## Algorithm Steps
1. Choose a base and modulus
2. Compute initial hashes for pattern and first window
3. Slide window one character at a time using rolling hash
4. On hash match, verify characters

### Time Complexity:
- Average: O(n + m)
- Worst-case (collisions): O(n · m)

### Space Complexity: O(1)

## Notes
- Probabilistic due to hash collisions
- Collisions are rare with good hashing
- Used in plagiarism detection and substring search engines