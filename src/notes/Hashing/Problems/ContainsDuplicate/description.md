# Contains Duplicate

**Difficulty:** Easy

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

## Example 1:
**Input:** `nums = [1,2,3,1]`
**Output:** `true`

## Example 2:
**Input:** `nums = [1,2,3,4]`
**Output:** `false`

## Example 3:
**Input:** `nums = [1,1,1,3,3,4,3,2,4,2]`
**Output:** `true`

## Approach
A naive approach would be to sort the array and check adjacent elements ($O(N \log N)$ time).
However, using a Hash Set gives us the optimal solution. We iterate through the array, and for each element:
1. Check if it is already in the Hash Set. If it is, we found a duplicate, return `true`.
2. If it is not, add it to the Hash Set.
3. If the loop finishes without finding any duplicates, return `false`.

*(Python trick: You can also simply compare `len(set(nums))` to `len(nums)`)*.

## Complexity
- **Time Complexity:** $O(N)$ - We iterate over the array once. Hash Set lookups and insertions are $O(1)$ on average.
- **Space Complexity:** $O(N)$ - In the worst case (all elements distinct), the Hash Set will store $N$ elements.
