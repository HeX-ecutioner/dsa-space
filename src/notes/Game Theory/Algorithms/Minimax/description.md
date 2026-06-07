# Minimax Algorithm

Minimax is a recursive algorithm used for decision-making in Game Theory. It provides an optimal move for the player assuming that the opponent is also playing optimally. It is widely used for two-player turn-based games such as Tic-Tac-Toe, Chess, and Go.

## The Core Concept: Maximizing and Minimizing

The algorithm simulates all possible moves in a game to build a **Game Tree**. 
- The root of the tree is the current state.
- The branches represent possible moves.
- The leaves represent the end states of the game (Win, Lose, or Draw).

The two players are given specific roles:
1.  **Maximizer:** Wants to get the highest possible score (e.g., +1 for a win, +infinity for a dominant position).
2.  **Minimizer:** Wants to get the lowest possible score (e.g., -1 for a win for them, -infinity).

Since the game is zero-sum, the Maximizer's win is the Minimizer's loss.

### How it traverses the Game Tree
1.  **Generate the Tree:** Generate all possible game states down to the terminal nodes (the end of the game).
2.  **Evaluate Leaves:** Assign a heuristic evaluation score to the terminal nodes (e.g., +10 if Maximizer wins, -10 if Minimizer wins, 0 for draw).
3.  **Backtrack:**
    - If it's the **Maximizer's** turn at a specific node, they will look at their children and choose the move that leads to the **maximum** score.
    - If it's the **Minimizer's** turn at a specific node, they will look at their children and choose the move that leads to the **minimum** score.
4.  This process bubbles up from the leaves to the root. The value at the root node is the best possible score the Maximizer can achieve if both players play perfectly.

## Pseudo-code

```python
def minimax(position, depth, isMaximizingPlayer):
    # Base case: game is over or we reached the depth limit
    if depth == 0 or game_over(position):
        return evaluate(position)

    if isMaximizingPlayer:
        maxEval = -infinity
        for child in get_children(position):
            eval = minimax(child, depth - 1, False)
            maxEval = max(maxEval, eval)
        return maxEval

    else:
        minEval = +infinity
        for child in get_children(position):
            eval = minimax(child, depth - 1, True)
            minEval = min(minEval, eval)
        return minEval
```

## Complexity
- **Time Complexity:** $O(b^d)$ where $b$ is the branching factor (average number of valid moves per state) and $d$ is the depth of the tree. This exponential growth makes plain Minimax incredibly slow for complex games like Chess.
- **Space Complexity:** $O(d)$ for the recursive call stack.

To make Minimax practical for deep games, we must use techniques like **Alpha-Beta Pruning** and **Memoization (Dynamic Programming)** to cut down the search space.
