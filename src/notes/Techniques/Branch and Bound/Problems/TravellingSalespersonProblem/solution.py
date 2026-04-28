# Problem: Travelling Salesperson Problem (TSP) using Branch and Bound.
# Given a set of cities and the distance between every pair of cities, the problem is to find the shortest possible route that visits every city exactly once and returns to the starting point.
import math
from typing import List

def tsp_branch_and_bound(adj_matrix: List[List[int]]) -> int:
    """
    Approach: Branch and Bound.
    Brute force TSP is O(N!). With Branch and Bound, we dramatically reduce the number of 
    paths explored by maintaining a "bound" (a mathematically guaranteed minimum cost).
    
    1. We calculate an initial lower bound for the root node (e.g., sum of the two minimum 
       edges attached to each vertex, divided by 2).
    2. We explore paths (DFS or BFS). For each step, we update the current cost and the 
       new bound.
    3. If the `current_cost + new_bound` is >= our best known complete tour, we PRUNE 
       the branch. It's impossible for this path to be the shortest.
       
    Time: Worst case O(N!), but practically much faster.
    Space: O(N) for recursion stack and tracking arrays.
    """
    n = len(adj_matrix)
    final_res = math.inf
    final_path = [None] * (n + 1)
    visited = [False] * n
    
    def first_min(i: int) -> int:
        """Find the minimum edge cost from node i"""
        m = math.inf
        for k in range(n):
            if adj_matrix[i][k] < m and i != k:
                m = adj_matrix[i][k]
        return m

    def second_min(i: int) -> int:
        """Find the second minimum edge cost from node i"""
        first, second = math.inf, math.inf
        for j in range(n):
            if i == j: continue
            if adj_matrix[i][j] <= first:
                second = first
                first = adj_matrix[i][j]
            elif adj_matrix[i][j] <= second and adj_matrix[i][j] != first:
                second = adj_matrix[i][j]
        return second

    def tsp_recurse(curr_bound: float, curr_weight: int, level: int, curr_path: List[int]):
        nonlocal final_res, final_path
        
        # Base case is when we have reached level N
        if level == n:
            # Check if there is an edge from last vertex back to the first
            if adj_matrix[curr_path[level - 1]][curr_path[0]] != 0:
                curr_res = curr_weight + adj_matrix[curr_path[level - 1]][curr_path[0]]
                if curr_res < final_res:
                    final_path[:n] = curr_path[:]
                    final_path[n] = curr_path[0]
                    final_res = curr_res
            return

        # For any other level, try all vertices to build the search space tree
        for i in range(n):
            # Consider next vertex if it is not visited and there is an edge
            if adj_matrix[curr_path[level - 1]][i] != 0 and not visited[i]:
                temp_bound = curr_bound
                curr_weight += adj_matrix[curr_path[level - 1]][i]

                # Update bound depending on the level
                if level == 1:
                    curr_bound -= ((first_min(curr_path[level - 1]) + first_min(i)) / 2)
                else:
                    curr_bound -= ((second_min(curr_path[level - 1]) + first_min(i)) / 2)

                # PRUNING: Only explore if lower bound is less than the current best result
                if curr_bound + curr_weight < final_res:
                    curr_path[level] = i
                    visited[i] = True
                    tsp_recurse(curr_bound, curr_weight, level + 1, curr_path)

                # Backtrack
                curr_weight -= adj_matrix[curr_path[level - 1]][i]
                curr_bound = temp_bound
                # Reset visited array
                visited = [False] * len(visited)
                for j in range(level):
                    if curr_path[j] != -1:
                        visited[curr_path[j]] = True

    # Initial setup
    curr_bound = 0
    curr_path = [-1] * (n + 1)
    
    # Calculate initial bound
    for i in range(n):
        curr_bound += (first_min(i) + second_min(i))
    # Bound is halved because each edge is counted twice
    curr_bound = math.ceil(curr_bound / 2)

    visited[0] = True
    curr_path[0] = 0

    tsp_recurse(curr_bound, 0, 1, curr_path)
    return final_res

# Example usage:
# Adjacency matrix for 4 cities
matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print(tsp_branch_and_bound(matrix)) # Output: 80 (Path: 0 -> 1 -> 3 -> 2 -> 0)
