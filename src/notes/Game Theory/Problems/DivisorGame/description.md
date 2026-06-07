# Divisor Game

**Difficulty:** Easy

Alice and Bob take turns playing a game, with Alice starting first.
Initially, there is a number `n` on the chalkboard. On each player's turn, that player makes a move consisting of:
- Choosing any `x` with `0 < x < n` and `n % x == 0`.
- Replacing the number `n` on the chalkboard with `n - x`.

Also, if a player cannot make a move, they lose the game. Return `true` if and only if Alice wins the game, assuming both players play optimally.

## Example 1:
**Input:** `n = 2`
**Output:** `true`
**Explanation:** Alice chooses 1, and Bob has no more moves.

## Example 2:
**Input:** `n = 3`
**Output:** `false`
**Explanation:** Alice chooses 1, Bob chooses 1, and Alice has no more moves.

## Approach: Mathematical Deduction
Let's analyze the winning (W) and losing (L) states:
- `n = 1`: No valid `x` exists. Player loses. (L)
- `n = 2`: Can pick `x = 1`, leaving `n = 1` for the opponent. (W)
- `n = 3`: Only divisor is `x = 1`, leaving `n = 2` for the opponent. (L)
- `n = 4`: Can pick `x = 1` (leaves 3, an L state for opponent). So 4 is a W.

**Theorem:** If `n` is EVEN, the current player wins. If `n` is ODD, the current player loses.

**Proof:**
1.  If `n` is EVEN, you can always choose `x = 1` (since 1 divides everything). This leaves `n - 1`, which is ODD, for your opponent.
2.  If `n` is ODD, its only divisors are ODD. (Odd % Even is never 0). So `x` must be odd.
3.  `n - x` will be `ODD - ODD = EVEN`. Thus, any move from an ODD number forces the next state to be EVEN.
4.  By mathematical induction, since the base case `n=1` is a loss, and any odd number guarantees passing an even number to the opponent (who will then pass back an odd number), starting with an odd number is a guaranteed loss. Starting with an even number guarantees a win (you just keep passing odd numbers to the opponent until they hit 1).

## Complexity
- **Time Complexity:** $O(1)$
- **Space Complexity:** $O(1)$
