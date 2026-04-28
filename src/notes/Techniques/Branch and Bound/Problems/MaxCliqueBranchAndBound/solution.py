# Problem: Find the Maximum Clique in an undirected graph.
def maxClique(graph):
    """
    Approach: Branch and Bound (Bron-Kerbosch algorithm variant or simple backtracking).
    Time: O(3^(V/3))
    Space: O(V)
    """
    V = len(graph)
    max_clique_size = 0

    def is_clique(nodes):
        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                if graph[nodes[i]][nodes[j]] == 0:
                    return False
        return True

    def backtrack(idx, current_clique):
        nonlocal max_clique_size
        if len(current_clique) + (V - idx) <= max_clique_size:
            return

        if idx == V:
            if is_clique(current_clique):
                max_clique_size = max(max_clique_size, len(current_clique))
            return

        backtrack(idx + 1, current_clique + [idx])
        backtrack(idx + 1, current_clique)

    backtrack(0, [])
    return max_clique_size
