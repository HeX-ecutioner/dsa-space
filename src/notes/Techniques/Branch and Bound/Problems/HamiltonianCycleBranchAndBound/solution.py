# Problem: Given an undirected graph, determine whether it contains a Hamiltonian Cycle (a closed loop that visits every vertex exactly once).
def hamCycle(graph):
    """
    Approach: Branch and Bound / Backtracking.
    Time: O(N!)
    Space: O(N)
    """
    V = len(graph)
    path = [-1] * V
    path[0] = 0

    def isSafe(v, pos):
        if graph[path[pos - 1]][v] == 0:
            return False
        if v in path:
            return False
        return True

    def hamCycleUtil(pos):
        if pos == V:
            if graph[path[pos - 1]][path[0]] == 1:
                return True
            else:
                return False

        for v in range(1, V):
            if isSafe(v, pos):
                path[pos] = v
                if hamCycleUtil(pos + 1):
                    return True
                path[pos] = -1
        return False

    return hamCycleUtil(1)
