# Alpha-Beta Pruning

Alpha-Beta Pruning is an optimization technique for the Minimax algorithm. It dramatically reduces the number of nodes evaluated in the search tree without affecting the final result.

## The Core Concept
The algorithm maintains two values, alpha and beta, which represent the minimum score that the maximizing player is assured of and the maximum score that the minimizing player is assured of respectively.

- **Alpha ($\alpha$):** The best (highest) value that the **Maximizer** can guarantee at that level or above. Initialized to $-\infty$.
- **Beta ($\beta$):** The best (lowest) value that the **Minimizer** can guarantee at that level or above. Initialized to $+\infty$.

### The Pruning Condition
As the algorithm traverses the tree, it passes down the current $\alpha$ and $\beta$ values. 
The core pruning logic is: **If at any point $\beta \le \alpha$, we can stop evaluating the remaining children of this node.**

Why? 
- If $\beta \le \alpha$, it means that the current path we are exploring is proven to be *worse* for the current player than a path they have already found earlier in the tree. The opponent will never let us go down this path anyway because they already have a better option. Thus, there is no need to search it further.

## Pseudo-code

```python
def minimax(position, depth, alpha, beta, isMaximizingPlayer):
    # Base case
    if depth == 0 or game_over(position):
        return evaluate(position)

    if isMaximizingPlayer:
        maxEval = -infinity
        for child in get_children(position):
            eval = minimax(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            # Pruning condition
            if beta <= alpha:
                break # Prune the rest of the branches
        return maxEval

    else:
        minEval = +infinity
        for child in get_children(position):
            eval = minimax(child, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            # Pruning condition
            if beta <= alpha:
                break # Prune the rest of the branches
        return minEval
```

## Impact on Complexity
- **Worst-Case Time Complexity:** $O(b^d)$ (same as plain minimax, happens if nodes are evaluated in the worst possible order).
- **Best-Case Time Complexity:** $O(b^{d/2})$. This happens if the nodes are perfectly ordered such that the best moves are always evaluated first. This effectively doubles the depth we can search in the same amount of time.

*Takeaway:* Move ordering is critical when using Alpha-Beta pruning. If you check the "likely best" moves first, you trigger pruning much earlier, saving massive amounts of computation.
