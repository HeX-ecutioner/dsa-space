# Two Sum

**Difficulty:** Easy

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

## Example 1:
**Input:** `nums = [2,7,11,15]`, `target = 9`
**Output:** `[0,1]`
**Explanation:** Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

## Example 2:
**Input:** `nums = [3,2,4]`, `target = 6`
**Output:** `[1,2]`

## Approach
Instead of a brute-force $O(N^2)$ approach where we check every pair, we can use a Hash Map to reduce the time complexity to $O(N)$.

As we iterate through the array, for every element `num`, we calculate its `complement` ($target - num$). 
If the complement is already in the hash map, we've found our pair! If not, we add the current `num` and its index to the hash map and continue.

## Complexity
- **Time Complexity:** $O(N)$, because we traverse the list containing $N$ elements exactly once. Each hash map lookup costs $O(1)$ on average.
- **Space Complexity:** $O(N)$, because the extra space required depends on the number of items stored in the hash map, which stores at most $N$ elements.
