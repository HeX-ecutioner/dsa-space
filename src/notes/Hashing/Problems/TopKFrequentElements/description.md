# Top K Frequent Elements

**Difficulty:** Medium

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

## Example 1:
**Input:** `nums = [1,1,1,2,2,3]`, `k = 2`
**Output:** `[1,2]`

## Example 2:
**Input:** `nums = [1]`, `k = 1`
**Output:** `[1]`

## Approach
This problem can be solved in a few ways. The first step for all of them is to use a **Hash Map** to count the frequencies of each element ($O(N)$ time).

1.  **Heap / Priority Queue:** After counting frequencies, push all (count, number) pairs into a Max-Heap (or a Min-Heap of size `k`). Popping from the heap takes $O(\log k)$. Overall time: $O(N \log k)$.
2.  **Bucket Sort (Optimal):** Because the maximum possible frequency of an element is $N$ (the length of the array), we can create an array of "buckets" where the index is the frequency, and the value is a list of numbers with that frequency.
    - `buckets = [ [] for i in range(len(nums) + 1) ]`
    - Iterate through the hash map and place numbers into their respective frequency bucket.
    - Finally, iterate through the buckets *backwards* (from highest frequency to lowest) and gather the top `k` elements.

## Complexity (Bucket Sort Approach)
- **Time Complexity:** $O(N)$. Counting frequencies takes $O(N)$. Placing into buckets takes $O(N)$. Iterating backwards to find top $k$ takes $O(N)$. Total = $O(N)$.
- **Space Complexity:** $O(N)$ for the Hash Map and the buckets array.
