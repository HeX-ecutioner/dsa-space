# Sprague-Grundy Theorem

The **Sprague-Grundy Theorem** is a mathematical powerhouse for solving **Impartial Games** played under normal play convention (the last player to move wins). 

It states that *every* finite impartial game is mathematically equivalent to a single heap of a game called **Nim**.

## The Game of Nim
Nim is the quintessential impartial game. There are multiple piles of stones. On a player's turn, they can select exactly one pile and remove any number of stones from it (at least 1, up to the whole pile). The player unable to move (because all piles are empty) loses.

**The Nim-Sum:**
The winning strategy for Nim relies on the **XOR sum** (bitwise exclusive OR, denoted by $\oplus$) of the sizes of all piles.
`Nim-Sum = pile_1 ^ pile_2 ^ ... ^ pile_n`

- **Theorem:** If the Nim-Sum is `0`, the game is in a **Losing State** (the current player will lose if the opponent plays optimally).
- **Theorem:** If the Nim-Sum is `> 0`, the game is in a **Winning State** (the current player can force a win).

## Grundy Numbers (Nimbers)
What if the game isn't Nim? The Sprague-Grundy theorem says we can calculate a "Grundy Number" (or Nim-value) for *any* state of *any* impartial game. This number acts exactly like a pile of stones in Nim.

The Grundy Number $G(S)$ of a state $S$ is defined recursively using the **MEX** (Minimum Excluded) function.

### The MEX Function
$MEX(Set)$ is the smallest non-negative integer that is *not* present in the Set.
- $MEX(\{0, 1, 3\}) = 2$
- $MEX(\{1, 2, 3\}) = 0$
- $MEX(\emptyset) = 0$

### Calculating the Grundy Number
1. The Grundy number of a terminal state (where no moves are possible) is $0$.
2. The Grundy number of any state $S$ is the $MEX$ of the Grundy numbers of all states reachable from $S$ in a single valid move.
   $$G(S) = MEX( \{ G(S_1), G(S_2), ..., G(S_k) \} )$$

## Solving Composite Games
If you are playing a game that is essentially multiple independent sub-games played simultaneously (e.g., multiple different boards, and on your turn you pick one board and make a move), you can determine the winner of the entire composite game by:
1. Calculating the Grundy Number $G(s_i)$ for the current state of *each* sub-game.
2. XOR-ing all these Grundy numbers together.
   $$Total = G(s_1) \oplus G(s_2) \oplus ... \oplus G(s_n)$$
3. If $Total > 0$, the first player wins. If $Total == 0$, the second player wins.
