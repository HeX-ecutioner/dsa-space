# Subarray Sum Equals K

**Difficulty:** Medium

Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.
A subarray is a contiguous non-empty sequence of elements within an array.

## Example 1:
**Input:** `nums = [1,1,1]`, `k = 2`
**Output:** `2`
*(Explanation: [1,1] from index 0-1, and [1,1] from index 1-2)*

## Example 2:
**Input:** `nums = [1,2,3]`, `k = 3`
**Output:** `2`

## Approach: Prefix Sum + Hash Map
Finding subarrays usually brings "Sliding Window" to mind. However, since the array can contain **negative numbers**, the sliding window approach fails (expanding the window doesn't guarantee the sum increases).

Instead, we use a **Prefix Sum** combined with a **Hash Map**.
1. We keep a running total (prefix sum) as we iterate through the array.
2. At any index `i`, the `current_sum` represents the sum from index `0` to `i`.
3. We want to find a previous index `j` such that the sum from `j` to `i` is equal to `k`.
4. Mathematically: `sum(0 to i) - sum(0 to j) = k` 
   Which means: `sum(0 to j) = current_sum - k`
5. Therefore, we just need to check if we have ever seen a prefix sum equal to `current_sum - k` in the past!
6. We use a Hash Map to store `{prefix_sum : frequency}`.

*(Don't forget to initialize the hash map with `{0: 1}` to account for subarrays that start from index 0).*

## Complexity
- **Time Complexity:** $O(N)$ as we iterate through the array exactly once, doing $O(1)$ Hash Map lookups.
- **Space Complexity:** $O(N)$ for storing prefix sums in the Hash Map.
