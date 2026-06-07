# Nim Game

**Difficulty:** Easy

You are playing the following Nim Game with your friend:
- Initially, there is a heap of stones on the table.
- You and your friend will alternate taking turns, and **you go first**.
- On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
- The one who removes the last stone is the winner.

Given `n`, the number of stones in the heap, return `true` if you can win the game assuming both you and your friend play optimally, otherwise return `false`.

## Example 1:
**Input:** `n = 4`
**Output:** `false`
**Explanation:** These are the possible outcomes:
1. You remove 1 stone. Your friend removes 3 stones, including the last one. Your friend wins.
2. You remove 2 stones. Your friend removes 2 stones, including the last one. Your friend wins.
3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
In all outcomes, your friend wins.

## Example 2:
**Input:** `n = 1`
**Output:** `true`

## Approach: Mathematical Deduction
This is the most basic form of a Game Theory problem. Instead of using complex Minimax, we can deduce a mathematical pattern by working backwards from the winning condition.

1.  If there are 1, 2, or 3 stones, you win immediately by taking them all.
2.  If there are 4 stones, no matter if you take 1, 2, or 3 stones, you leave your opponent with 3, 2, or 1 stone. As seen in step 1, anyone facing 1, 2, or 3 stones wins. Therefore, facing 4 stones is a guaranteed **Loss**.
3.  If there are 5, 6, or 7 stones, you can just take enough to leave exactly 4 stones for your opponent. Since facing 4 stones is a guaranteed loss, you guarantee a win for yourself.
4.  If there are 8 stones, any move you make (leaving 5, 6, or 7) gives your opponent a winning position. So, 8 is a guaranteed **Loss**.

The pattern is clear: If the number of stones is a multiple of 4 (`n % 4 == 0`), you will always lose. Otherwise, you can always win by forcing your opponent into a multiple of 4.

## Complexity
- **Time Complexity:** $O(1)$
- **Space Complexity:** $O(1)$
