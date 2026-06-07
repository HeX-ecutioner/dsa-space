# Group Anagrams

**Difficulty:** Medium

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

## Example 1:
**Input:** `strs = ["eat","tea","tan","ate","nat","bat"]`
**Output:** `[["bat"],["nat","tan"],["ate","eat","tea"]]`

## Example 2:
**Input:** `strs = [""]`
**Output:** `[[""]]`

## Approach
To group items together using a Hash Map, we need a unique "Key" for each group. For anagrams, what is the shared characteristic?
1.  **Sorted String:** If we sort "eat", "tea", and "ate", they all become "aet". We can use this sorted string as the Hash Map key, and append the original string to a list of values.
2.  **Character Count Array:** Sorting takes $O(K \log K)$ per string (where $K$ is the string length). A more optimal way is to create a frequency array `[1, 0, 0, 0, 1 ...]` for the 26 lowercase English letters. We can convert this array to a tuple (since tuples are hashable in Python, unlike lists) and use it as the Hash Map key.

## Complexity (Using Frequency Array)
- **Time Complexity:** $O(N \times K)$ where $N$ is the number of strings and $K$ is the maximum length of a string. We count the characters of each string once.
- **Space Complexity:** $O(N \times K)$ to store the result in the Hash Map. The keys themselves take $O(26) = O(1)$ space.
