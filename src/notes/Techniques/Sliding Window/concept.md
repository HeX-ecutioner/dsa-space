# 🪟 Sliding Window

The **Sliding Window** technique is an essential pattern for solving array or string problems that involve finding a continuous subset (a "window") that satisfies a certain condition. 

By maintaining a "window" of elements and sliding it across the data structure, we can optimize problems that would otherwise require nested loops (O(n²)) down to a linear pass (O(n)).

---

## 1️⃣ What is the Sliding Window Technique?

A "window" is simply a range of elements defined by a start and end index. 
Instead of recalculating the property of the window from scratch every time it moves, we:
- **Add** the effect of the new element entering the window from the right.
- **Remove** the effect of the old element leaving the window from the left.

This turns O(n) repetitive calculations per window into O(1) updates.

---

## 2️⃣ Core Variations

### Fixed-Size Window
The window size `k` remains constant throughout the traversal.
- Move the right pointer by 1.
- Move the left pointer by 1.
- Example: Maximum sum of any contiguous subarray of size `k`.

### Variable-Size Window
The window size expands or shrinks based on a specific condition.
- Expand the right pointer to include elements until a condition is met (or violated).
- Shrink the left pointer to restore the condition.
- Example: Longest substring with at most `k` distinct characters.

---

## 3️⃣ When to Apply Sliding Window

Think of this technique when:
1. The problem involves **contiguous sequences** (substrings, subarrays).
2. You need to find a **max/min/longest/shortest** value of that sequence.
3. You need to calculate something over a **fixed or variable length** window.
4. You are looking for an optimal sequence that satisfies a specific constraint.

It is NOT suitable for subsequences (where elements don't need to be contiguous).

---

## 4️⃣ Summary
Mastering sliding window allows you to seamlessly track states across continuous sequences, reducing time complexity significantly. It's heavily tested in interviews and forms the backbone of string manipulation and array processing logic.
