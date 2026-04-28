# 🌳 Branch and Bound

The **Branch and Bound** technique is an algorithmic method primarily used for solving **optimization problems** (especially those involving combinatorial optimization or finding minimum/maximum values). It explores branches of a search space tree but safely prunes ("bounds") paths that are guaranteed not to yield an optimal solution.

It is heavily used when finding an exact solution is required, but a full brute force approach is too slow (e.g., NP-Hard problems like the Traveling Salesperson Problem).

---

## 1️⃣ What is Branch and Bound?

It consists of two main steps:
1. **Branching**: Recursively splitting the problem into smaller subproblems, forming a state-space tree.
2. **Bounding**: Calculating an optimistic estimate (a "bound") of the best possible solution in a branch. If this bound is worse than the best solution found so far, we prune (discard) the entire branch.

For a minimization problem:
- Keep track of the `best_solution_so_far`.
- For each node, calculate the `lower_bound` of the cost in its subtree.
- If `lower_bound >= best_solution_so_far`, don't explore this branch! (Pruning).

---

## 2️⃣ Core Concepts

- **State-Space Tree**: A tree representing all possible states or partial solutions of the problem.
- **Bounding Function**: A fast function to estimate the best possible outcome from the current state. The quality of Branch and Bound heavily depends on how tight and easy to calculate this bound is.
- **Exploration Strategies**:
  - **FIFO (Breadth-First Search)**: Explores level by level.
  - **LIFO (Depth-First Search)**: Explores deep first. Usually requires less memory.
  - **Least-Cost Search (Best-First Search)**: Uses a priority queue to always expand the node with the most promising bound.

---

## 3️⃣ When to Apply Branch and Bound

Think of this technique when:
1. You are dealing with an **Optimization Problem** (Minimizing cost, maximizing profit).
2. The problem asks for the **Exact Optimal Solution** in a large combinatorial space.
3. Brute force/Backtracking is too slow (O(N!) or O(2^N)), but you can mathematically prove that certain paths will never be optimal without exploring them.
4. Classical examples: 0/1 Knapsack (to get exact solution faster than brute force), Traveling Salesperson Problem, Job Assignment Problem.

---

## 4️⃣ Comparison with Backtracking

- **Backtracking** is for finding *all* valid solutions or *any* valid solution (e.g., Sudoku, N-Queens). It prunes when a path becomes invalid.
- **Branch and Bound** is for finding the *optimal* solution. It prunes when a path is valid but mathematically proven to be *worse* than our current best.

---

## 5️⃣ Summary
Branch and Bound empowers developers to solve NP-Hard problems exactly in reasonable time by intelligently abandoning bad options early. The secret lies entirely in formulating a strong bounding function.
