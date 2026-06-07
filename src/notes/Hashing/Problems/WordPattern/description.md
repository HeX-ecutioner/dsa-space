# Word Pattern

**Difficulty:** Easy

Given a `pattern` and a string `s`, find if `s` follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `s`.

## Example 1:
**Input:** `pattern = "abba", s = "dog cat cat dog"`
**Output:** `true`

## Example 2:
**Input:** `pattern = "abba", s = "dog cat cat fish"`
**Output:** `false`

## Example 3:
**Input:** `pattern = "aaaa", s = "dog cat cat dog"`
**Output:** `false`

## Approach
This problem is almost perfectly identical to **Isomorphic Strings**. The only difference is that instead of mapping characters to characters, we are mapping characters (from `pattern`) to whole words (from `s`).

1. Split string `s` into an array of words.
2. If the length of the `pattern` does not equal the number of words, return `false`.
3. Use two Hash Maps (`charToWord` and `wordToChar`) to ensure a 1-to-1 bijection.
4. Iterate through the pattern and words simultaneously, validating the mappings just like in Isomorphic Strings.

## Complexity
- **Time Complexity:** $O(N)$ where $N$ is the length of `s` (to split the string) plus the length of the pattern.
- **Space Complexity:** $O(M)$ where $M$ is the number of unique words in `s` (stored in the Hash Map).
