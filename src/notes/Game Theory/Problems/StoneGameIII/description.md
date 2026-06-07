# Stone Game III

**Difficulty:** Hard

Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array `stoneValue`.

Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take `1`, `2`, or `3` stones from the first remaining stones in the row.

The score of each player is the sum of values of the stones taken. The score of each player is 0 initially.
The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

Assume Alice and Bob play optimally.
Return `"Alice"` if Alice will win, `"Bob"` if Bob will win, or `"Tie"` if they will end the game with the same score.

## Example 1:
**Input:** `stoneValue = [1,2,3,7]`
**Output:** `"Bob"`
**Explanation:** Alice will always lose. Her best move will be to take three piles and the score become 6. Now the array of stones is `[7]`. Bob takes 7. Alice score is 6, Bob score is 7. Bob wins.

## Approach: Minimax DP (Score Difference)
This is very similar to `Predict The Winner`. We want to calculate the maximum **score difference** the current player can achieve starting from index `i`.

Let `dp(i)` be the maximum score difference the current player can get starting from index `i`.
On their turn, a player can take 1, 2, or 3 stones.
- If they take 1 stone: They gain `stoneValue[i]`. The opponent plays from `i+1` and gets a score difference of `dp(i+1)`. So the current player's net difference is `stoneValue[i] - dp(i+1)`.
- If they take 2 stones: Net difference is `stoneValue[i] + stoneValue[i+1] - dp(i+2)`.
- If they take 3 stones: Net difference is `stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp(i+3)`.

We want to maximize this net difference over the 3 possible choices.

If `dp(0) > 0`, Alice wins. If `dp(0) < 0`, Bob wins. If `dp(0) == 0`, it's a Tie.

## Complexity
- **Time Complexity:** $O(N)$ where $N$ is the number of stones. There are $N$ states, and each state calculates the maximum of 3 transitions ($O(1)$ work).
- **Space Complexity:** $O(N)$ for the memoization cache.
