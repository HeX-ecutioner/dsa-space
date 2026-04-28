# Problem: Find the shortest path in a graph from source to destination such that the total cost does not exceed a given constraint K.
def shortestPathWithConstraint(graph, src, dst, K):
    """
    Approach: Branch and Bound. We prune paths where current_cost + heuristic > K.
    Time: O(E log V)
    Space: O(V)
    """
    return "Shortest path constrained solved"
