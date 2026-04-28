# 🕸️ Graph Data Structure

The **Graph** is a foundational non-linear data structure used to represent networks and complex relationships between entities. While a tree represents hierarchical relationships (a specialized type of graph), a graph models a generalized set of connections. 

Graphs are the backbone of many real-world systems, including:

- Social Networks (friends, followers)
- Maps and Navigation (GPS, shortest paths)
- Computer Networks (routers, topologies)
- Web Structures (hyperlinks between pages)
- State Machines (transitions between states)
- Dependency Resolution (package managers, task scheduling)

This chapter provides a comprehensive deep dive into graphs, covering from their fundamental concepts up to advanced topics.

# 1️⃣ Introduction & Basics

## What is a Graph?

A Graph $G$ is an ordered pair $G = (V, E)$ comprising:

- $V$: A set of **Vertices** (or nodes) representing the entities.
- $E$: A set of **Edges** (or links/lines) representing the connections between the vertices.

### 👉 Every Tree is a Graph, but not every Graph is a Tree.
A Tree is specifically an undirected, connected, acyclic graph.

---

### Graph as an Abstract Data Type (ADT)

As an ADT, a Graph defines:

- Relationships between arbitrary points
- Traversal operations (exploring the network)
- Structural and analytical operations (finding paths, cycles, components)

It is implemented physically through various memory representations like Adjacency Matrices or Adjacency Lists.

---

### Key Characteristics

- General structure with no strict hierarchy
- May contain cycles and self-loops
- Can have directed or undirected connections
- Can have weighted or unweighted connections

## 2️⃣ Graph Terminology

Understanding terminology is absolutely critical for graph theory.

- **Vertex (Node)** — Fundamental unit of the graph.
- **Edge (Link)** — A connection between two vertices.
- **Directed Edge** — An edge with a direction (from $u$ to $v$).
- **Undirected Edge** — A bi-directional edge (between $u$ and $v$).
- **Weight / Cost** — A numerical value assigned to an edge.
- **Degree** — Number of edges connected to a vertex.
    - **In-Degree**: Number of incoming edges (Directed Graphs).
    - **Out-Degree**: Number of outgoing edges (Directed Graphs).
- **Adjacent Vertices (Neighbors)** — Two vertices connected directly by an edge.
- **Path** — A sequence of vertices where each adjacent pair is connected by an edge.
- **Path Length** — The number of edges (or sum of weights) in a path.
- **Cycle** — A path that starts and ends at the same vertex, with length $\ge 3$.
- **Self-Loop** — An edge that connects a vertex to itself.
- **Connected Graph** — An undirected graph where a path exists between every pair of vertices.
- **Strongly Connected Graph** — A directed graph where a directed path exists between every pair of vertices.
- **Connected Component** — A maximal connected subgraph.
- **Subgraph** — A graph formed by a subset of the vertices and edges of another graph.
- **Forest** — A set of disjoint trees (an acyclic graph).
- **Spanning Tree** — A subgraph that is a tree and includes all the vertices of the original graph.
- **Clique** — A subset of vertices where every two distinct vertices are adjacent (Complete Subgraph).

## 3️⃣ Types of Graphs

- **Undirected Graph**: Edges have no direction.
- **Directed Graph (Digraph)**: Edges have direction.
- **Weighted Graph**: Edges have weights.
- **Unweighted Graph**: Edges have no weights (or uniform weight).
- **Cyclic Graph**: Contains at least one cycle.
- **Acyclic Graph**: Contains no cycles.
- **Directed Acyclic Graph (DAG)**: A directed graph with no cycles. Critical for topological sorting.
- **Bipartite Graph**: Vertices can be divided into two disjoint sets such that every edge connects a vertex in one set to a vertex in the other.
- **Complete Graph**: Every pair of distinct vertices is connected by a unique edge.
- **Dense Graph**: The number of edges is close to the maximal number of edges.
- **Sparse Graph**: The number of edges is much less than the maximal number of edges.

## 4️⃣ Graph Traversals

Traversing a graph means systematically visiting its vertices. Unlike trees, graphs can have cycles, so we must keep track of visited nodes to avoid infinite loops.

### Depth-First Search (DFS)
Explores as far as possible along each branch before backtracking.
- Often implemented recursively or with an explicit stack.
- Useful for: Cycle detection, Topological Sorting, finding Strongly Connected Components.

### Breadth-First Search (BFS)
Explores the neighbor nodes first, before moving to the next level neighbors.
- Implemented using a Queue.
- Useful for: Finding the shortest path on unweighted graphs, peer-to-peer networks.

## 5️⃣ Basic Operations

- **Add/Remove Vertex**: Modifies the set $V$.
- **Add/Remove Edge**: Modifies the set $E$.
- **Check Adjacency**: Checks if an edge exists between two vertices.
- **Get Neighbors**: Retrieves all vertices adjacent to a given vertex.

## 6️⃣ Structural Properties
- **Max Edges in Undirected Graph**: $N(N-1)/2$
- **Max Edges in Directed Graph**: $N(N-1)$
- **Eulerian Path**: A path that visits every edge exactly once.
- **Hamiltonian Path**: A path that visits every vertex exactly once.
- **Planarity**: A graph that can be drawn on a plane without any edges crossing.

## 7️⃣ Time & Space Complexity

Complexities depend heavily on the chosen representation: Adjacency Matrix ($O(V^2)$ space) vs. Adjacency List ($O(V+E)$ space).

### Time Complexity (Adjacency List)
| Operation | Complexity |
| :--- | :--- |
| **Add Vertex** | $O(1)$ |
| **Add Edge** | $O(1)$ |
| **Remove Vertex** | $O(V + E)$ |
| **Remove Edge** | $O(E)$ |
| **Query/Find Edge** | $O(V)$ |
| **BFS/DFS Traversal** | $O(V + E)$ |

### Space Complexity
| Representation | Complexity |
| :--- | :--- |
| **Adjacency Matrix** | $O(V^2)$ |
| **Adjacency List** | $O(V + E)$ |

## 8️⃣ Implementation Notes

### Graphs can be implemented using:
- **Adjacency Matrix**: Best for dense graphs and fast edge lookups.
- **Adjacency List**: Best for sparse graphs, traversals, and most algorithmic problems.
- **Edge List**: Useful for algorithms that sort edges (like Kruskal's MST).
- Always use a `visited` array/set to prevent infinite loops during traversal.

## 9️⃣ Summary

The Graph is the most versatile data structure in computer science. Mastering it is essential for solving complex architectural and algorithmic problems.

It is the foundation for:
- Pathfinding (Dijkstra, A*, Bellman-Ford)
- Network Flow (Ford-Fulkerson)
- Spanning Trees (Prim's, Kruskal's)

Understanding graphs transforms you from a programmer into an algorithmic thinker capable of modeling reality.
