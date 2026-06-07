# Game Theory

Game theory is the study of mathematical models of strategic interactions among rational agents. In the context of computer science, algorithms, and technical interviews, "Game Theory" generally refers to **Combinatorial Games**.

## Combinatorial Games

A combinatorial game is a two-player game with perfect information (no hidden elements like cards in a deck) and no chance (no dice rolls). 
Examples include Chess, Checkers, Tic-Tac-Toe, and Nim. 
In DSA problems, these games often involve numbers or stones.

### Key Assumptions in DSA Game Theory:
1.  **Two Players:** Usually named Alice and Bob (or Player 1 and Player 2).
2.  **Sequential Play:** Players take turns. They do not move simultaneously.
3.  **Perfect Information:** Both players know the entire state of the game at all times.
4.  **Optimal Play:** This is the most crucial assumption. Both players play flawlessly to maximize their chances of winning. If a winning strategy exists, the player will find it and use it. They will never make a mistake that lets the other player win if they could prevent it.
5.  **Zero-Sum:** One player's gain is exactly the other player's loss. There is usually a winner and a loser (sometimes a draw).
6.  **Finite:** The game must end after a finite number of moves (usually ending when a player cannot make a valid move).

## Impartial vs. Partisan Games

### Impartial Games
In an impartial game, the set of allowable moves depends *only* on the current state of the game, and not on whose turn it is.
*   **Example:** Nim. A pile of stones is on the table. Either player can take stones from a pile. The rules are the same regardless of whether it's Alice's or Bob's turn.
*   **Analysis:** Impartial games can often be deeply analyzed mathematically using the **Sprague-Grundy Theorem** and XOR sums.

### Partisan Games
In a partisan game, the available moves depend on whose turn it is.
*   **Example:** Chess. Only the white player can move white pieces, and only the black player can move black pieces.
*   **Analysis:** Partisan games typically require tree-search algorithms like **Minimax** and **Alpha-Beta Pruning**, often optimized with Dynamic Programming (Memoization).

## The Concept of "Winning State" and "Losing State"

A game state can be classified into two types, assuming optimal play:

1.  **Winning State (W):** A state is a winning state if there exists *at least one* valid move that transitions the game into a Losing State for the opponent. If a player is in a Winning State, they have a strategy to force a win.
2.  **Losing State (L):** A state is a losing state if *every* valid move transitions the game into a Winning State for the opponent. If a player is in a Losing State, no matter what they do, the opponent can force a win.

This recursive definition is the foundation of Minimax algorithms and Dynamic Programming solutions for game theory problems.
