# Problem: Determine if a graph can be colored with at most m colors such that no two adjacent vertices of the graph are colored with same color.
def graphColoring(graph, m):
    """
    Approach: Branch and Bound / Backtracking.
    Time: O(m^V)
    Space: O(V)
    """
    V = len(graph)
    color = [0] * V

    def isSafe(v, c):
        for i in range(V):
            if graph[v][i] == 1 and color[i] == c:
                return False
        return True

    def graphColorUtil(v):
        if v == V: return True
        for c in range(1, m + 1):
            if isSafe(v, c):
                color[v] = c
                if graphColorUtil(v + 1):
                    return True
                color[v] = 0
        return False

    return graphColorUtil(0)
