# Network Flow

Network Flow algorithms determine the maximum possible flow from a source node to a sink node in a flow network. A flow network is a directed graph where each edge has a capacity.

## Key Terminology
- **Source ($S$)**: The node where flow originates.
- **Sink ($T$)**: The node where flow terminates.
- **Capacity ($C$)**: The maximum amount of flow an edge can handle.
- **Flow ($F$)**: The current amount of flow passing through an edge.
- **Residual Graph**: A graph showing the remaining capacity on each edge and allowing "undo" operations by pushing flow backwards.
- **Augmenting Path**: A path from $S$ to $T$ in the residual graph where every edge has residual capacity > 0.

## Max-Flow Min-Cut Theorem
The maximum flow from source to sink is exactly equal to the capacity of the minimum cut (the cheapest set of edges that, if removed, would disconnect the sink from the source).

## Algorithms
### 1. Ford-Fulkerson Method
- Repeatedly finds an augmenting path using DFS or BFS and pushes flow along it until no more paths exist.
- **Complexity**: $O(E \times \text{max\_flow})$. (Can be slow or even infinite for irrational capacities if not careful).

### 2. Edmonds-Karp Algorithm
- An implementation of Ford-Fulkerson that uses BFS to find the shortest augmenting path (in terms of number of edges).
- **Complexity**: $O(V \times E^2)$.

### 3. Dinic's Algorithm
- Highly optimized. Uses BFS to build a "Level Graph" and then uses DFS to push multiple blocking flows simultaneously.
- **Complexity**: $O(V^2 \times E)$. For bipartite matching, it runs in $O(E \sqrt{V})$.
