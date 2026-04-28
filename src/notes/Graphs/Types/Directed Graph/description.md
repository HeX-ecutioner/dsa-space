# Directed Graph (Digraph)

A Directed Graph is a set of vertices connected by edges, where the edges have a specific direction.

## Properties
- Edges are ordered pairs $(u, v)$ meaning the edge goes from vertex $u$ to vertex $v$.
- **In-degree**: Number of edges coming into a vertex.
- **Out-degree**: Number of edges going out of a vertex.
- A directed graph can have mutual edges (an edge from $u$ to $v$, and another from $v$ to $u$), which differs from an undirected graph where a single edge implies bidirectionality.

## Adjacency List Representation
If there is a directed edge from $u \to v$, $v$ is added to the adjacency list of $u$, but $u$ is NOT added to the adjacency list of $v$ (unless $v \to u$ also exists).

## Applications
- Web page links
- State machines
- Task dependencies (Topological sorting)
- Social network followers (e.g., Twitter, Instagram)
