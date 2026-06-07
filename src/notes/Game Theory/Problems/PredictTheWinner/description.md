# Predict the Winner

**Difficulty:** Medium

You are given an integer array `nums`. Two players are playing a game with this array: player 1 and player 2.
Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of `0`. At each turn, the player takes one of the numbers from either end of the array (i.e., `nums[0]` or `nums[nums.length - 1]`) which reduces the size of the array by `1`. The player adds the chosen number to their score. The game ends when there are no more elements in the array.
Return `true` if Player 1 can win the game. If the scores are tied, player 1 is still the winner.

## Example 1:
**Input:** `nums = [1,5,2]`
**Output:** `false`
**Explanation:** Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return `false`.

## Approach: Minimax with Dynamic Programming (Memoization)

This is a classic Minimax scenario. We need to find the maximum possible score Player 1 can achieve assuming Player 2 also plays perfectly.

Instead of keeping track of both players' scores, we can reframe the problem: 
We calculate the **Score Difference** (`Player 1 Score - Player 2 Score`). 
- When it's Player 1's turn, they want to **maximize** this difference.
- When it's Player 2's turn, they want to **minimize** this difference (which is the same as maximizing their own score relative to Player 1, i.e., adding a negative value to the difference).

Let `dp(left, right)` be the maximum score difference a player can achieve using the subarray `nums[left...right]`.
If a player picks `nums[left]`, their score increases by `nums[left]`, and the opponent will get the optimal score from the remaining array `dp(left + 1, right)`. Thus, the net difference is `nums[left] - dp(left + 1, right)`.

The state transition is:
`dp(left, right) = max(nums[left] - dp(left + 1, right), nums[right] - dp(left, right - 1))`

If the final `dp(0, n-1) >= 0`, Player 1 wins or ties.

## Complexity
- **Time Complexity:** $O(N^2)$. There are $O(N^2)$ possible states `(left, right)`, and each state takes $O(1)$ to compute.
- **Space Complexity:** $O(N^2)$ for the memoization cache.
