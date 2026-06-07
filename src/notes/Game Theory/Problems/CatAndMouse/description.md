# Cat and Mouse

**Difficulty:** Hard

A game on an undirected graph is played by two players, Mouse and Cat, who alternate turns.
The graph is given as follows: `graph[a]` is a list of all nodes `b` such that `ab` is an edge of the graph.
The mouse starts at node `1` and goes first, the cat starts at node `2` and goes second, and there is a hole at node `0`.
During each player's turn, they must travel along one edge of the graph that meets where they are. For example, if the Mouse is at node 1, it must travel to any node in `graph[1]`.
The Cat cannot travel to the hole (node 0).

The game can end in three ways:
- If ever the Cat occupies the same node as the Mouse, the Cat wins.
- If ever the Mouse reaches the hole, the Mouse wins.
- If ever a position is repeated (i.e., the players are in the same positions as a previous turn, and it is the same player's turn to move), the game is a draw.

Given a `graph`, return `1` if the mouse wins the game, `2` if the cat wins the game, or `0` if the game is a draw.

## Approach: Minimax on a Graph (Topological Sort / Retrograde Analysis)
This is an incredibly difficult graph + game theory problem because it introduces the concept of a **Draw** via cycles, which standard DP/Memoization handles very poorly (infinite recursion).

To handle cycles, we must work *backwards* from the terminal states. This is called **Retrograde Analysis** or **Bottom-Up Minimax**.

1.  **State Definition:** A state is `(mouse_pos, cat_pos, turn)`. `turn` is 1 for Mouse, 2 for Cat.
2.  **Degree Count:** Count the out-degree of every state (how many valid moves a player can make from that state). Cat cannot move to 0.
3.  **Terminal States:** Add all known terminal states to a Queue.
    - `(0, c, turn) -> MOUSE_WINS`
    - `(m, m, turn) -> CAT_WINS` (where m != 0)
4.  **Retrograde BFS:** Process the Queue. For a known winning/losing state `curr`, look at its predecessors `prev`:
    - If `curr` is a WINNING state for the player whose turn it is in `prev` (e.g., Mouse won, and `prev` was Mouse's turn), then `prev` becomes a WINNING state. Add `prev` to queue.
    - If `curr` is a LOSING state for the player whose turn it is in `prev`, we decrement the out-degree of `prev`. If the out-degree reaches 0, it means *all* moves from `prev` lead to a loss, so `prev` is definitively a LOSING state. Add `prev` to queue.
5.  If the queue is empty and the initial state `(1, 2, 1)` hasn't been resolved, it means neither player can force a win, and the game is trapped in a cycle (Draw, return 0).

## Complexity
- **Time Complexity:** $O(N^3)$. There are $N \times N \times 2$ states. In the worst case, we process edges for all states.
- **Space Complexity:** $O(N^2)$ to store the states, degrees, and queue.
