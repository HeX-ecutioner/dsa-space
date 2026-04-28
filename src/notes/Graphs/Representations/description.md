# Graph Representation

## Logical Representation
A **Graph** is a non-linear data structure that consists of a finite set of vertices (or nodes) and a set of edges connecting these vertices. It represents a "many-to-many" relationship. Mathematically, a graph $G$ is defined as $G = (V, E)$, where $V$ is the set of vertices and $E$ is the set of edges.

## Physical Representation
Graphs can be implemented in memory in a few primary ways. The choice of representation significantly impacts both the space required and the time complexity of various graph operations.

### 1. Adjacency Matrix
An Adjacency Matrix is a 2D array of size $V \times V$ where $V$ is the number of vertices.
Let the 2D array be `adj[][]`. A slot `adj[i][j] = 1` indicates that there is an edge from vertex $i$ to vertex $j$.

* **Undirected Graph**: The matrix is symmetric (`adj[i][j] == adj[j][i]`).
* **Weighted Graph**: The slot `adj[i][j]` holds the weight of the edge instead of just a boolean 1. (Use $\infty$ or a special sentinel value to indicate no edge).

**Advantages:**
* Edge lookup (checking if an edge exists between $u$ and $v$) is extremely fast: $O(1)$.
* Adding or removing an edge is $O(1)$.
* Convenient for dense graphs where $E$ is close to $V^2$.

**Disadvantages:**
* Consumes $O(V^2)$ space regardless of the number of edges, making it highly inefficient for sparse graphs.
* Finding all neighbors of a vertex takes $O(V)$ time.

### 2. Adjacency List (Most Common)
An Adjacency List represents the graph as an array (or hash map) of lists. The size of the array is equal to the number of vertices. Let the array be `adj[]`. The list `adj[i]` contains all the vertices $j$ such that there is an edge from vertex $i$ to vertex $j$.

* **Weighted Graph**: The list stores pairs or tuples: `(neighbor_vertex, edge_weight)`.

**Advantages:**
* Highly space-efficient for sparse graphs: Space complexity is $O(V + E)$.
* Finding all neighbors of a given vertex is fast (proportional to its degree).
* Most graph algorithms (BFS, DFS, Dijkstra's) are most efficient with adjacency lists.

**Disadvantages:**
* Checking if a specific edge $(u, v)$ exists takes $O(degree(u))$ time in the worst case.

### 3. Edge List
An Edge List simply maintains a single linear list (or array) of all the edges in the graph. Each edge is usually represented as a tuple: `(u, v)` or `(u, v, weight)`.

**Advantages:**
* Very simple to construct.
* Space-efficient: $O(E)$ space.
* Ideal for algorithms that primarily iterate over all edges and sort them, such as **Kruskal's Algorithm** for Minimum Spanning Tree.

**Disadvantages:**
* Getting the neighbors of a specific vertex is very slow: $O(E)$.
* Checking for a specific edge is $O(E)$.

### 4. Implicit Graph (State Space)
In many problems (like solving a maze or puzzles), the graph is never explicitly built in memory. Instead, the vertices are states, and the edges are generated on-the-fly via a function `get_neighbors(state)`.
* **Advantages**: Saves memory; only generates necessary parts of the graph.
* **Use Case**: Grid-based pathfinding, permutation puzzles (e.g., 8-puzzle).

## Diagrams and Traces

### Matrix vs List Trace
Consider an undirected graph with $V=4$ (labeled 0,1,2,3) and edges: (0,1), (0,2), (1,2), (2,3).

**Adjacency Matrix (`4x4`):**
```
   0  1  2  3
0 [0, 1, 1, 0]
1 [1, 0, 1, 0]
2 [1, 1, 0, 1]
3 [0, 0, 1, 0]
```

**Adjacency List:**
```
0 -> [1, 2]
1 -> [0, 2]
2 -> [0, 1, 3]
3 -> [2]
```

**Edge List:**
```
[(0,1), (0,2), (1,2), (2,3)]
```

## 📊 Representation Summary

| Feature | Adjacency Matrix | Adjacency List | Edge List |
| :--- | :--- | :--- | :--- |
| **Space Complexity** | $O(V^2)$ | $O(V + E)$ | $O(E)$ |
| **Edge Lookup $(u, v)$** | $O(1)$ | $O(degree(u))$ | $O(E)$ |
| **Add Edge** | $O(1)$ | $O(1)$ | $O(1)$ |
| **Get Neighbors of $u$** | $O(V)$ | $O(degree(u))$ | $O(E)$ |
| **Best For** | Dense Graphs, Fast lookups | Sparse Graphs, Traversals | Kruskal's, Edge sorting |
