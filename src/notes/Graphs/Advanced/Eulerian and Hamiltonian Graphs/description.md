# Eulerian and Hamiltonian Graphs

These are two classical concepts in graph theory involving paths and circuits that visit specific elements of a graph exactly once.

## Eulerian Path and Circuit
Concerned with **Edges**.

- **Eulerian Path**: A path that visits every **edge** of the graph exactly once.
- **Eulerian Circuit**: An Eulerian path that starts and ends on the same vertex.

### Existence Conditions (Undirected Graph)
- **Eulerian Circuit**: All vertices with non-zero degree are connected, AND every vertex has an **even degree**.
- **Eulerian Path**: All vertices with non-zero degree are connected, AND exactly **zero or two** vertices have an **odd degree**.

### Existence Conditions (Directed Graph)
- **Eulerian Circuit**: All vertices belong to a single strongly connected component, AND every vertex has `in-degree == out-degree`.
- **Eulerian Path**: At most one vertex has `out-degree - in-degree == 1`, at most one has `in-degree - out-degree == 1`, and all others have equal in and out degrees.

### Algorithm
**Hierholzer's Algorithm**:
1. Start at a valid vertex.
2. Follow unvisited edges, pushing nodes to a stack, until you get stuck.
3. Once stuck (no unvisited outgoing edges), pop the node and add it to the final circuit.
4. Reverse the final list to get the path.
*Time Complexity: $O(V + E)$*

---

## Hamiltonian Path and Cycle
Concerned with **Vertices**.

- **Hamiltonian Path**: A path that visits every **vertex** of the graph exactly once.
- **Hamiltonian Cycle**: A Hamiltonian path that starts and ends on the same vertex.

### Complexity
Unlike Eulerian paths, determining whether a graph has a Hamiltonian Path/Cycle is **NP-Complete**. There is no known polynomial-time algorithm for general graphs.

### Common Algorithms
1. **Backtracking (DFS)**: Try all possible permutations. $O(N!)$
2. **Dynamic Programming with Bitmasking**: 
   - State: `dp(mask, u)` where `mask` represents visited nodes, and `u` is the current node.
   - Transition: Try visiting an unvisited neighbor.
   - Time Complexity: $O(N^2 \cdot 2^N)$. Space Complexity: $O(N \cdot 2^N)$. This is much faster than backtracking but only feasible for $N \le 20$.
