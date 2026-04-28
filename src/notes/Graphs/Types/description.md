# Types of Graphs

Graphs come in many different forms depending on the properties of their edges and structural constraints. Understanding graph classification is crucial for selecting the right algorithm.

## 1. Directed vs Undirected

### Undirected Graph
An undirected graph is a graph in which edges have no orientation. An edge `(u, v)` is identical to the edge `(v, u)`.
* **Applications**: Social networks (mutual friendships), physical computer networks (ethernet cables).

### Directed Graph (Digraph)
A directed graph is a set of vertices connected by edges, where the edges have a direction associated with them. An edge `(u, v)` implies a connection from `u` to `v`, but not necessarily the other way around.
* **Applications**: Web page linking, Twitter followers, one-way streets.

## 2. Weighted vs Unweighted

### Unweighted Graph
All edges are treated equally (often assumed to have a weight of 1). The shortest path between two nodes is simply the path with the fewest number of edges.
* **Applications**: Finding degrees of separation, basic connectivity.

### Weighted Graph
Each edge is assigned a numerical value called a weight or cost. The shortest path between two nodes minimizes the total sum of the edge weights. Weights can be positive, negative, or zero (though some algorithms fail with negative cycles).
* **Applications**: Road networks (distance/time), flight routes (cost), computer networks (latency).

## 3. Structural Variations

### Directed Acyclic Graph (DAG)
A directed graph with absolutely no directed cycles.
* **Significance**: DAGs are the only graphs that can be topologically sorted. They naturally represent dependencies.
* **Applications**: Build systems (Makefiles), task scheduling, resolving software dependencies, data processing pipelines.

### Bipartite Graph
A graph whose vertices can be divided into two disjoint sets $U$ and $V$ such that every edge connects a vertex in $U$ to one in $V$. There are no edges connecting vertices within the same set.
* **Significance**: A graph is bipartite if and only if it does not contain any odd-length cycles. It is 2-colorable.
* **Applications**: Matching problems (job applicants to jobs, students to classes).

### Complete Graph
A graph in which every pair of distinct vertices is connected by a unique edge.
* **Edges**: An undirected complete graph with $N$ vertices has exactly $N(N-1)/2$ edges.
* **Notation**: Denoted as $K_n$.

### Tree (as a Graph)
An undirected, connected, acyclic graph.
* **Properties**: Removing any edge disconnects the graph; adding any edge creates a cycle. Any two vertices are connected by exactly one simple path.

### Planar Graph
A graph that can be drawn on a 2D plane in such a way that no edges cross each other.
* **Significance**: Euler's Formula for planar graphs: $V - E + F = 2$ (where F is the number of faces).

### Multigraph
A graph that is permitted to have multiple edges (parallel edges) between the same pair of vertices.
* **Applications**: Multiple distinct flights between the same two cities.
