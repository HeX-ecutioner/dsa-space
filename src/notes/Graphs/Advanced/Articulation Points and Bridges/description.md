# Articulation Points and Bridges

Identifying vulnerabilities or critical nodes/edges in a network is a common requirement in graph theory.

## Definitions
- **Articulation Point (Cut Vertex)**: A vertex whose removal (along with all incident edges) disconnects the graph, increasing the number of connected components.
- **Bridge (Cut Edge)**: An edge whose removal disconnects the graph, increasing the number of connected components.

## Tarjan's Algorithm for Bridges and APs
Both problems can be solved in a single DFS pass using the concepts of discovery times and lowest reachable times.

### Key Variables Maintained in DFS
1. `disc[u]`: The time when vertex $u$ is first visited.
2. `low[u]`: The earliest visited vertex (lowest discovery time) that can be reached from the subtree rooted at $u$ (including $u$ itself), but *excluding* the edge that brought us to $u$.

### Logic for Bridges
During DFS traversal, if we are exploring an edge $(u, v)$ (where $u$ is the parent of $v$ in the DFS tree):
- If `low[v] > disc[u]`: It means there is no back-edge from $v$ or its descendants to $u$ or any ancestor of $u$. Therefore, removing $(u, v)$ disconnects $v$ from $u$. So, $(u, v)$ is a **Bridge**.

### Logic for Articulation Points
During DFS traversal, for an edge $(u, v)$:
- If $u$ is the **root** of the DFS tree and has $\ge 2$ independent children, it is an AP.
- If $u$ is **not the root**, and `low[v] >= disc[u]`: It means the subtree rooted at $v$ has no back-edge to an ancestor of $u$. Thus, removing $u$ traps $v$. So, $u$ is an **Articulation Point**.

## Complexity
- **Time Complexity**: $O(V + E)$ since it's a single DFS pass.
- **Space Complexity**: $O(V)$ for storing `disc`, `low`, and `visited` arrays.
