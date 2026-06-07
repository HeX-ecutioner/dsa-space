# Isomorphic Strings

**Difficulty:** Easy

Given two strings `s` and `t`, determine if they are isomorphic.
Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

## Example 1:
**Input:** `s = "egg", t = "add"`
**Output:** `true`

## Example 2:
**Input:** `s = "foo", t = "bar"`
**Output:** `false`
*(Explanation: 'o' cannot map to both 'a' and 'r')*

## Example 3:
**Input:** `s = "paper", t = "title"`
**Output:** `true`

## Approach
We need to establish a **1-to-1 mapping** (bijection) between characters in `s` and characters in `t`.
To do this effectively, we can use two Hash Maps:
1.  `mapST`: maps characters from `s` to `t`.
2.  `mapTS`: maps characters from `t` to `s`.

We iterate through both strings simultaneously:
- If a character in `s` has already been mapped in `mapST`, verify that it maps to the current character in `t`. If not, return `false`.
- If a character in `t` has already been mapped in `mapTS`, verify that it maps to the current character in `s`. If not, return `false`.
- If neither is mapped, establish the mapping in both maps.

## Complexity
- **Time Complexity:** $O(N)$ where $N$ is the length of the string. We iterate through the strings once.
- **Space Complexity:** $O(1)$. The hash maps store at most 256 key-value pairs (for extended ASCII), which is bounded by a constant.
