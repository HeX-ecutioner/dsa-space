def dfs_traversal(graph, start):
    """
    Perform Depth-First Search (DFS) traversal of a graph starting from the given start node using an explicit stack.

    The graph is represented as an adjacency list.

    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    visited = set()          # to track visited nodes
    stack = [start]          # stack for DFS
    traversal = []           # store DFS order

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            traversal.append(node)

            # Push neighbors in reverse order to mimic recursive DFS
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal

# Example usage:
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [],
    5: []
}
print(dfs_traversal(graph, 0)) # Output: [0, 1, 3, 4, 2, 5]