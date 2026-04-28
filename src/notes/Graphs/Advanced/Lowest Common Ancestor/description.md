# Lowest Common Ancestor (LCA) in Graphs / Trees

The Lowest Common Ancestor of two nodes $u$ and $v$ in a rooted tree or Directed Acyclic Graph (DAG) is the lowest node $w$ that has both $u$ and $v$ as descendants (where we allow a node to be a descendant of itself).

While this is fundamentally a tree problem, it frequently arises in advanced graph problems where a graph is condensed into a tree (like a BFS tree, DFS tree, or heavily-lightly decomposed tree).

## 1. Binary Lifting (Standard DP Approach)
The most common online method to answer multiple LCA queries efficiently.
- **Precomputation**: $O(N \log N)$
- **Query**: $O(\log N)$
- **Concept**: Each node stores a pointer to its $2^0, 2^1, 2^2, \dots, 2^{\lfloor \log N \rfloor}$-th ancestor. To find the LCA of $u$ and $v$, we first lift the deeper node to the same depth as the other. If they match, that is the LCA. Otherwise, we lift both nodes simultaneously in large jumps, without overshooting the LCA.

## 2. Euler Tour + Range Minimum Query (RMQ)
Reduces the LCA problem to an RMQ problem.
- **Precomputation**: $O(N \log N)$ (using a Sparse Table) or $O(N)$ (using a Segment Tree).
- **Query**: $O(1)$ (Sparse Table) or $O(\log N)$ (Segment Tree).
- **Concept**: Perform an Euler Tour (DFS) of the tree, recording the sequence of visited nodes and their depths. The LCA of $u$ and $v$ is the node with the minimum depth in the Euler tour array between the first occurrence of $u$ and the first occurrence of $v$.

## 3. Tarjan's Offline LCA Algorithm
- **Time Complexity**: $O(N + Q \times \alpha(N))$ where $Q$ is the number of queries.
- **Concept**: Uses Disjoint Set Union (DSU) to process all queries at once (offline) while performing a single DFS. Very efficient, but queries must be known in advance.
