# Minimum Window Substring

**Difficulty:** Hard

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

## Example 1:
**Input:** `s = "ADOBECODEBANC"`, `t = "ABC"`
**Output:** `"BANC"`
*(Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.)*

## Example 2:
**Input:** `s = "a"`, `t = "a"`
**Output:** `"a"`

## Example 3:
**Input:** `s = "a"`, `t = "aa"`
**Output:** `""`

## Approach: Sliding Window + Hash Maps
This is a quintessential Hard problem that relies heavily on Hash Maps to track character frequencies within a Sliding Window.

1.  **Count Target:** Use a Hash Map (`countT`) to store the frequency of every character in `t`.
2.  **Tracking State:** Use a variable `have` to track how many unique characters in our current window meet the frequency requirement, and `need` which is the total number of unique characters in `t`.
3.  **Expand Window:** Iterate a `right` pointer across `s`. Add `s[right]` to a `window` Hash Map.
    - If `s[right]` is a required character and its frequency in `window` matches its frequency in `countT`, increment `have`.
4.  **Shrink Window:** While `have == need` (meaning our window is currently valid):
    - Update our `res` (minimum window bounds) if the current window is smaller.
    - Attempt to shrink the window from the left by removing `s[left]` from the `window` map and incrementing `left`.
    - If `s[left]` was a required character and its frequency drops *below* what is required in `countT`, decrement `have`.
5.  Return the substring using the bounds found.

## Complexity
- **Time Complexity:** $O(S + T)$ where $S$ and $T$ are the lengths of the strings. In the worst case, both `left` and `right` traverse the string `s` once.
- **Space Complexity:** $O(S + T)$ in the worst case if all characters are unique, as we store character frequencies in two Hash Maps.
