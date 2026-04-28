# Strongly Connected Components (SCCs)

A Strongly Connected Component of a directed graph is a maximal set of vertices such that for every pair of vertices $u, v$ in the set, there is a directed path from $u$ to $v$ and a directed path from $v$ to $u$.

## Kosaraju's Algorithm
Kosaraju's algorithm uses two passes of Depth First Search (DFS).
1. **Pass 1**: Do a standard DFS on the original graph and push nodes onto a stack based on their finishing times. (Nodes that finish last are at the top).
2. **Reverse Graph**: Compute the transpose graph (reverse all edges).
3. **Pass 2**: Pop nodes from the stack one by one. If a popped node is unvisited, start a DFS on the transposed graph. All nodes reachable from this DFS form a single SCC.
**Time Complexity**: $O(V + E)$
**Space Complexity**: $O(V)$

## Tarjan's Algorithm
Tarjan's algorithm finds SCCs in a single DFS pass.
It maintains:
- `disc`: discovery time of each node.
- `low`: lowest discovery time reachable from the node.
- `stack`: nodes currently being explored in the current SCC.
- `on_stack`: boolean array for quick lookup.
If after a DFS on a node, `disc[node] == low[node]`, it means the node is the "head" or "root" of an SCC, and all nodes above it on the stack belong to this SCC.
**Time Complexity**: $O(V + E)$
**Space Complexity**: $O(V)$

## Applications
- 2-SAT (Satisfiability) problems.
- Packaging dependencies / Cycle resolution.
- Simplifying graphs into DAGs (by condensing SCCs into single meta-nodes).
