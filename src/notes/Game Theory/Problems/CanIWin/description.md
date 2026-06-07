# Can I Win

**Difficulty:** Medium

In the "100 game" two players take turns adding, to a running total, any integer from `1` to `10`. The player who first causes the running total to **reach or exceed** 100 wins.
What if we change the game so that players **cannot** re-use integers?
For example, two players might take turns drawing from a common pool of numbers from `1` to `maxChoosableInteger` without replacement until they reach a `desiredTotal`.

Given two integers `maxChoosableInteger` and `desiredTotal`, return `true` if the first player to move can force a win, assuming both players play optimally. Otherwise, return `false`.

## Example 1:
**Input:** `maxChoosableInteger = 10`, `desiredTotal = 11`
**Output:** `false`
**Explanation:** 
No matter which integer the first player chooses, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player chooses 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and getting a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.

## Approach: Minimax + Memoization with Bitmasking
Since `maxChoosableInteger` is small (usually $\le 20$), we can use an integer as a **Bitmask** to represent the state of the pool of available numbers. 
- If the $i$-th bit is `0`, the number $i$ is available.
- If the $i$-th bit is `1`, the number $i$ has been used.

We use a recursive function `can_win(state, current_total)`:
1.  **Base Cases:** 
    - If the sum of all numbers is less than `desiredTotal`, nobody can win. Return `false`.
    - If `current_total >= desiredTotal`, the *previous* player won, so the *current* player loses.
2.  **Minimax Step:** Iterate through all available numbers (where the bit is `0`).
    - Make a move (set the bit to `1` and add the number to `current_total`).
    - Ask the opponent to play: `can_win(new_state, current_total + number)`.
    - If the opponent **loses** in that new state, it means picking this number guarantees a win for us! Return `true`.
3.  If we try *all* available numbers and the opponent wins in every scenario, then we return `false`.

## Complexity
- **Time Complexity:** $O(2^M \times M)$ where $M$ is `maxChoosableInteger`. There are $2^M$ possible bitmask states, and in each state, we iterate up to $M$ times.
- **Space Complexity:** $O(2^M)$ for the memoization cache.
