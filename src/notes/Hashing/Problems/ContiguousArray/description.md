# Contiguous Array

**Difficulty:** Medium

Given a binary array `nums` (containing only `0`s and `1`s), return the maximum length of a contiguous subarray with an equal number of `0` and `1`.

## Example 1:
**Input:** `nums = [0,1]`
**Output:** `2`
*(Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1)*

## Example 2:
**Input:** `nums = [0,1,0]`
**Output:** `2`
*(Explanation: [0, 1] or [1, 0] are the longest contiguous subarrays)*

## Approach: Prefix Sum + Hash Map
This problem is a clever variation of the **Subarray Sum Equals K** problem.
We can convert this problem into finding a subarray with a sum of `0` by treating all `0`s as `-1`s.

1. Treat `0` as `-1`, and `1` as `1`.
2. Keep a running `count` (which acts as our prefix sum).
3. If the `count` is `0`, it means from the beginning of the array to the current index, there are an equal number of 0s and 1s.
4. If the `count` returns to a value we've seen before, it means the subarray *between* the first time we saw that count and the current index must sum to `0` (which means equal 0s and 1s).
5. We use a Hash Map to store the `{count : first_seen_index}`. 
   - We only store the *first* time we see a count because we want the *longest* possible subarray.
6. For every index, we check if the current `count` is in the Hash Map. If it is, the length of the valid subarray is `current_index - hash_map[count]`. We update our max length.

*(Initialize the Hash Map with `{0: -1}` to properly calculate length for subarrays starting at index 0).*

## Complexity
- **Time Complexity:** $O(N)$ as we iterate through the array once and perform $O(1)$ Hash Map operations.
- **Space Complexity:** $O(N)$ to store the prefix sum indices in the Hash Map.
