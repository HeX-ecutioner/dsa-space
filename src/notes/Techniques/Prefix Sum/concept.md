# ➕ Prefix Sum

The **Prefix Sum** technique involves precomputing the cumulative sum of an array to answer range sum queries or perform range updates efficiently.

Instead of recalculating the sum of a subarray iteratively, we can do it in constant O(1) time by subtracting precomputed prefix sums.

---

## 1️⃣ What is the Prefix Sum Technique?

Given an array `arr` of size `N`, a prefix sum array `P` of size `N+1` is defined such that:
- `P[0] = 0`
- `P[i] = P[i-1] + arr[i-1]` for `i > 0`

The sum of elements in a range `[L, R]` (0-indexed) can be found instantly using:
**Sum(L, R) = P[R+1] - P[L]**

---

## 2️⃣ Core Concepts

### 1D Prefix Sum
Used for ranges in a single array.
- Calculate: `P[i] = P[i-1] + arr[i-1]`
- Query `[L, R]`: `P[R+1] - P[L]`

### 2D Prefix Sum
Used for submatrices in a 2D grid.
- Calculate: `P[i][j] = grid[i-1][j-1] + P[i-1][j] + P[i][j-1] - P[i-1][j-1]`
- Query top-left `(r1, c1)` to bottom-right `(r2, c2)`:
  `Sum = P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]`

### Prefix Sum + Hash Map
When tracking properties of subarrays (like "Subarray Sum Equals K"), we can store the occurrences of each prefix sum in a hash map.
- If `current_sum - k` exists in our hash map, it means there is a subarray ending at the current index that sums to `k`.

---

## 3️⃣ When to Apply Prefix Sum

Think of this technique when:
1. You need to repeatedly calculate the **sum, XOR, or product** of a continuous range.
2. The problem involves finding a **contiguous subarray** that matches a target sum, target average, or specific modulo.
3. You are doing **Range Updates**. (e.g., Difference Arrays).

---

## 4️⃣ Summary
Prefix Sum is a simple but incredibly powerful technique. By spending O(N) time and space upfront, it reduces any range sum query from O(N) to O(1).
