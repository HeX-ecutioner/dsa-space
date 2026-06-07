# Stone Game IV

**Difficulty:** Hard

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are `n` stones in a pile. On each player's turn, that player makes a move consisting of removing **any non-zero square number** of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.
Given a positive integer `n`, return `true` if and only if Alice wins the game otherwise return `false`, assuming both players play optimally.

## Example 1:
**Input:** `n = 4`
**Output:** `true`
**Explanation:** `n` is already a perfect square. Alice can take 4 stones on her first turn and win.

## Example 2:
**Input:** `n = 7`
**Output:** `false`
**Explanation:** Alice can't win.
If Alice takes 1 stone, Bob takes 4 stones, leaving 2 stones for Alice. She must take 1 stone, leaving 1 stone for Bob, who takes it and wins.
If Alice takes 4 stones, Bob takes 1 stone, leaving 2 stones for Alice. Again she loses.

## Approach: Dynamic Programming (Bottom-Up)
This is an impartial game with perfect information, perfect for DP.
A state `n` is a **Winning State (W)** if there is *at least one* move (subtracting a perfect square $k^2$) that transitions the game to a **Losing State (L)** for the opponent.
A state `n` is a **Losing State (L)** if *every* valid move leads to a Winning State for the opponent.

We can build a boolean DP array from $0$ to $n$.
- `dp[0] = False` (0 stones left means you have no moves, so you lose).
- For a number $i$ from $1$ to $n$:
  - We try all perfect squares $k^2 \le i$.
  - If we find ANY $k^2$ such that `dp[i - k*k] == False`, then `dp[i] = True` (because we can hand the opponent a losing state).
  - If for all $k^2$, `dp[i - k*k] == True`, then `dp[i] = False`.

## Complexity
- **Time Complexity:** $O(N \sqrt{N})$. For each number $i$ up to $N$, we loop through all perfect squares up to $i$, of which there are $\sqrt{i}$.
- **Space Complexity:** $O(N)$ for the DP array.
