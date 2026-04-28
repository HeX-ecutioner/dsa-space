# Problem: A vertex cover of an undirected graph is a subset of its vertices such that for every edge (u, v), either u or v is in the subset. Find the minimum vertex cover.
def minVertexCover(graph):
    """
    Approach: Branch and Bound. Keep track of the current minimum cover.
    Time: O(2^V)
    Space: O(V)
    """
    V = len(graph)
    min_cover_size = V

    def isCover(visited):
        for u in range(V):
            for v in range(V):
                if graph[u][v] == 1 and not visited[u] and not visited[v]:
                    return False
        return True

    def bnb(v, visited, count):
        nonlocal min_cover_size
        if count >= min_cover_size:
            return
        if v == V:
            if isCover(visited):
                min_cover_size = min(min_cover_size, count)
            return

        visited[v] = True
        bnb(v + 1, visited, count + 1)
        
        visited[v] = False
        bnb(v + 1, visited, count)

    bnb(0, [False] * V, 0)
    return min_cover_size
