# Advanced Graph Topics

This folder explores complex algorithms, specialized graph classes, and optimization techniques. Interviewers and competitive programming platforms heavily test these concepts.

## 1. Strongly Connected Components (SCCs)
In a directed graph, an SCC is a maximal subgraph where for every pair of vertices $(u, v)$, there is a directed path from $u$ to $v$ and a directed path from $v$ to $u$.
* **Algorithms**:
  * **Kosaraju's Algorithm**: Uses two passes of DFS and the transpose of the graph.
  * **Tarjan's Algorithm**: Uses a single DFS pass maintaining `low` and `disc` times.
* **Applications**: 2-SAT problem, analyzing network robustness.

## 2. Eulerian and Hamiltonian Paths/Circuits
* **Eulerian Path**: A trail in a finite graph that visits every **edge** exactly once. (Exists if zero or exactly two vertices have odd degree).
* **Eulerian Circuit**: An Eulerian path that starts and ends on the same vertex. (Exists if every vertex has an even degree).
  * **Algorithm**: Hierholzer's Algorithm.
* **Hamiltonian Path**: A path that visits every **vertex** exactly once.
* **Hamiltonian Cycle**: A Hamiltonian path that returns to the starting vertex.
  * **Note**: Finding a Hamiltonian Path/Cycle is NP-Complete (often solved via backtracking or dynamic programming with bitmasking).

## 3. Network Flow
Used to find the maximum flow of a "substance" through a network of pipes with given capacities.
* **Key Concept**: Max-Flow Min-Cut Theorem (the maximum flow through the network is exactly equal to the capacity of the smallest cut).
* **Algorithms**:
  * **Ford-Fulkerson**: Augmenting paths (using DFS/BFS).
  * **Edmonds-Karp**: BFS implementation of Ford-Fulkerson ($O(V E^2)$).
  * **Dinic's Algorithm**: Level graphs and blocking flows (much faster: $O(V^2 E)$).
* **Applications**: Bipartite matching, traffic routing, liquid flow optimization.

## 4. Lowest Common Ancestor (LCA)
While primarily a tree problem, LCA queries are often asked on rooted tree-graphs in advanced competitive programming.
* **Techniques**:
  * Binary Lifting ($O(\log N)$ per query).
  * Euler Tour + RMQ (Segment Tree or Sparse Table) ($O(1)$ per query).

## 5. Heavy-Light Decomposition (HLD)
A technique to decompose a tree (graph) into a set of disjoint paths, allowing operations (like path sums or max) to be performed in $O(\log^2 N)$ time.

## 6. Articulation Points and Bridges
* **Articulation Point (Cut Vertex)**: A vertex whose removal increases the number of connected components.
* **Bridge (Cut Edge)**: An edge whose removal increases the number of connected components.
* **Algorithm**: Tarjan's DFS-based approach using `discovery times` and `lowest reachable times`. Critical for analyzing network vulnerabilities.
