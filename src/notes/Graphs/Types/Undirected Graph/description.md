# Undirected Graph

An Undirected Graph is a graph in which edges have no orientation.

## Properties
- An edge $(u, v)$ is identical to the edge $(v, u)$.
- They denote mutual or symmetric relationships.
- The maximum number of edges in a simple undirected graph with $V$ vertices is $V(V-1)/2$.
- The **Degree** of a vertex is the total number of edges connected to it. By the Handshaking Lemma, the sum of all degrees in the graph is $2 \times E$.

## Adjacency List Representation
If there is an edge between $u$ and $v$, $v$ is added to $u$'s list AND $u$ is added to $v$'s list.

## Applications
- Mutual friendships (Facebook)
- Computer network topology (Ethernet)
- Road maps (assuming two-way roads)
