# Longest Substring Without Repeating Characters

**Difficulty:** Medium

Given a string `s`, find the length of the longest substring without repeating characters.

## Example 1:
**Input:** `s = "abcabcbb"`
**Output:** `3`
*(Explanation: The answer is "abc", with the length of 3.)*

## Example 2:
**Input:** `s = "bbbbb"`
**Output:** `1`
*(Explanation: The answer is "b", with the length of 1.)*

## Example 3:
**Input:** `s = "pwwkew"`
**Output:** `3`
*(Explanation: The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.)*

## Approach: Sliding Window + Hash Map
We can use the **Sliding Window** technique with two pointers (`left` and `right`) to represent the current substring. We will expand the `right` pointer as long as we don't encounter duplicate characters.

To quickly check for duplicates, we use a **Hash Map** that stores `{character : last_seen_index}`.

1.  Initialize `left = 0`, `max_len = 0`, and an empty `char_index_map`.
2.  Iterate `right` from 0 to the end of the string.
3.  If `s[right]` is already in `char_index_map`, it means we found a repeating character!
    - We must shrink our window. We move `left` directly to the right of the *last seen index* of this character (`char_index_map[s[right]] + 1`).
    - *Crucial detail:* We only move `left` forward. If the last seen index is *before* our current `left` pointer (meaning it's outside our current window), we ignore it. So, `left = max(left, char_index_map[s[right]] + 1)`.
4.  Update the `char_index_map` with the current `right` index.
5.  Update `max_len = max(max_len, right - left + 1)`.

## Complexity
- **Time Complexity:** $O(N)$ where $N$ is the length of the string. The `right` pointer iterates through the string exactly once, and Hash Map lookups are $O(1)$.
- **Space Complexity:** $O(\min(N, M))$ where $M$ is the size of the charset (e.g., 26 for lowercase letters, 128 for ASCII). The Hash Map will store at most $M$ characters.
