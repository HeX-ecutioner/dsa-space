# Stone Game

**Difficulty:** Medium

Alice and Bob play a game with piles of stones. There are an **even number of piles** arranged in a row, and each pile has a **positive integer** number of stones `piles[i]`.

The objective of the game is to end with the most stones. The total number of stones across all piles is **odd**, so there are no ties.

Alice and Bob take turns, with **Alice starting first**. Each turn, a player takes the entire pile of stones from either the beginning or the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alice and Bob play optimally, return `true` if Alice wins the game, or `false` if Bob wins.

## Example 1:
**Input:** `piles = [5,3,4,5]`
**Output:** `true`
**Explanation:** 
Alice starts and can take 5 (left) or 5 (right). Let's say she takes 5 (left), leaving `[3, 4, 5]`.
Bob can take 3 or 5. Let's say he takes 5, leaving `[3, 4]`.
Alice takes 4, leaving `[3]`. Bob takes 3.
Alice's score: `5 + 4 = 9`. Bob's score: `5 + 3 = 8`. Alice wins.

## Approach
This problem is fundamentally identical to **Predict The Winner**. We *could* use a Minimax DP approach to solve it. 

However, because of the specific constraints of the problem, there is an $O(1)$ mathematical trick:
1.  There is an **even** number of piles.
2.  The total sum is **odd** (no ties).
3.  Alice goes first.

Because there are an even number of piles, Alice can arbitrarily divide the array into "even-indexed" piles and "odd-indexed" piles. 
Before she makes her first move, she can simply calculate the sum of all even-indexed piles and the sum of all odd-indexed piles.
- If the sum of even-indexed piles is greater, she can take the first pile (`piles[0]`, an even index), forcing Bob to take an odd-indexed pile. Then she takes the next even-indexed pile, and so on. She will collect *all* even-indexed piles.
- If the sum of odd-indexed piles is greater, she can take the last pile (`piles[n-1]`, an odd index), forcing Bob to take an even-indexed pile. She will collect *all* odd-indexed piles.

Since the total sum is odd, one of these sums (even or odd) *must* be strictly greater than the other. Thus, **Alice can always force a win.**

## Complexity
- **Time Complexity:** $O(1)$ (using the math trick) or $O(N^2)$ (using DP).
- **Space Complexity:** $O(1)$ (using the math trick) or $O(N^2)$ (using DP).
