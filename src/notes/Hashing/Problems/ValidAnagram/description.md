# Valid Anagram

**Difficulty:** Easy

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.
An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Example 1:
**Input:** `s = "anagram", t = "nagaram"`
**Output:** `true`

## Example 2:
**Input:** `s = "rat", t = "car"`
**Output:** `false`

## Approach
There are two main optimal approaches:
1.  **Sorting:** Sort both strings and compare them. ($O(N \log N)$ time, $O(1)$ space).
2.  **Hash Map (Frequency Counting):** This is the optimal $O(N)$ time approach.
    - First, if the lengths of `s` and `t` are different, they cannot be anagrams.
    - We use a Hash Map (or an array of size 26 since it's just lowercase English letters) to count the frequencies of characters in string `s`.
    - We iterate through `s`, incrementing the count for each character.
    - We iterate through `t`, decrementing the count for each character.
    - Finally, if all counts in our map are exactly `0`, the strings are anagrams.

*(In Python, we can simply use `collections.Counter(s) == collections.Counter(t)`)*

## Complexity
- **Time Complexity:** $O(S + T)$ where $S$ and $T$ are the lengths of the strings. Building the frequency maps takes linear time.
- **Space Complexity:** $O(1)$. Although we use a hash map, it stores character counts. Since the problem usually restricts inputs to lowercase English letters, the map will have at most 26 keys. $O(26)$ is $O(1)$ constant space.
