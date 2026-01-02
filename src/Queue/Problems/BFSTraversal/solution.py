from collections import deque

def bfs_traversal(graph, start):
    """
    Perform Breadth-First Search (BFS) traversal of a graph starting from the given start node using a queue.

    The graph is represented as an adjacency list.

    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    visited = set() # to track visited nodes
    queue = deque([start]) # queue for BFS
    traversal = [] # store BFS order

    visited.add(start)

    while queue:
        node = queue.popleft()
        traversal.append(node)

        # Visit all unvisited neighbors
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

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
print(bfs_traversal(graph, 0)) # Output: [0, 1, 2, 3, 4, 5]