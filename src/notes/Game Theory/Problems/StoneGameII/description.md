# Stone Game II

**Difficulty:** Medium

Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each pile has a positive integer number of stones `piles[i]`. The objective of the game is to end with the most stones. 

Alice and Bob take turns, with Alice starting first. Initially, `M = 1`.
On each player's turn, that player can take all the stones in the first `X` remaining piles, where `1 <= X <= 2M`. Then, we set `M = max(M, X)`.

The game continues until all the stones have been taken. Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

## Example 1:
**Input:** `piles = [2,7,9,4,4]`
**Output:** `10`
**Explanation:**  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 

## Approach: Minimax + Dynamic Programming
This problem removes the $O(1)$ trick from Stone Game I by changing the rules of how many piles can be taken. We must use Minimax with DP.

Unlike previous problems where we tracked the "Score Difference", here we are asked for the **exact score** Alice can achieve.

Let `dp(idx, M)` be the maximum stones the *current player* can get starting from `piles[idx]` with the current value of `M`.

1.  **Base Case:** If `idx >= len(piles)`, there are no stones left, return 0.
2.  **Greedy Optimization:** If `idx + 2*M >= len(piles)`, the current player can just take all the remaining piles. The answer is `sum(piles[idx:])`.
3.  **Minimax Transition:** The current player tries to take `X` piles (from `1` to `2M`). 
    - The stones they gain is `sum(piles[idx : idx+X])`.
    - The opponent will then play optimally starting from `idx+X` with a new `M = max(M, X)`, gaining `dp(idx+X, max(M, X))` stones.
    - So, the current player's total score will be the *total remaining stones* MINUS what the opponent can get.
    - `current_player_score = total_remaining_stones[idx:] - dp(idx+X, max(M, X))`
    - We want to maximize this `current_player_score` over all choices of `X`.

## Complexity
- **Time Complexity:** $O(N^3)$. There are $N \times N$ states in the memo cache (idx can be up to N, M can be up to N). Inside the DP function, the loop runs up to $2M$ times, which in the worst case is $O(N)$.
- **Space Complexity:** $O(N^2)$ for the memoization cache.
