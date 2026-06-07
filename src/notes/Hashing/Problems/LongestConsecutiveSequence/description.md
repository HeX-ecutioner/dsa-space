# Longest Consecutive Sequence

**Difficulty:** Medium

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in **$O(N)$** time.

## Example 1:
**Input:** `nums = [100,4,200,1,3,2]`
**Output:** `4`
**Explanation:** The longest consecutive elements sequence is `[1, 2, 3, 4]`. Therefore its length is 4.

## Example 2:
**Input:** `nums = [0,3,7,2,5,8,4,6,0,1]`
**Output:** `9`

## Approach
A naive approach would be sorting the array, which takes $O(N \log N)$ time. To achieve $O(N)$ time, we must use a **Hash Set**.

1. Insert all numbers into a Hash Set. This gives us $O(1)$ lookups.
2. Iterate through the numbers. For each number `n`, check if it is the **start of a sequence**.
   - A number is the start of a sequence ONLY IF its left neighbor (`n - 1`) is NOT in the Hash Set.
3. If it is the start of a sequence, use a `while` loop to keep checking if `n + 1`, `n + 2`, etc., exist in the set.
4. Keep track of the current sequence length, and update the `longest` sequence length seen so far.

By only starting the `while` loop for numbers that are the *beginning* of a sequence, we guarantee that each number in the array is visited at most twice (once in the `for` loop, once in the `while` loop). This yields an $O(N)$ time complexity.

## Complexity
- **Time Complexity:** $O(N)$. Although there is a `while` loop inside a `for` loop, the `while` loop only runs for the start of sequences, meaning we visit each element at most twice.
- **Space Complexity:** $O(N)$ to store the array elements in the Hash Set.
