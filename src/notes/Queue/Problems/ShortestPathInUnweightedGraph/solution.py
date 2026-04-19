# Problem: Given an unweighted graph and a starting node, find the shortest distance from the starting node to all other nodes

from collections import deque

def shortest_path_unweighted(graph, start):
    """
    Returns the shortest distance from start node
    to all other nodes in an unweighted graph.

    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    distance = {start: 0}
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for neighbor in graph.get(node, []):
            if neighbor not in distance:
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)

    return distance

# Example usage:
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: [4],
    4: []
}
print(shortest_path_unweighted(graph, 0)) # Output: {0: 0, 1: 1, 2: 1, 3: 2, 4: 3}