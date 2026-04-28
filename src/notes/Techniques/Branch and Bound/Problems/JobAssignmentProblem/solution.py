# Problem: Job Assignment Problem using Branch and Bound.
# Given N workers and N jobs, and a cost matrix where cost[i][j] is the cost of assigning
# worker i to job j. Find the optimal assignment of jobs to workers to minimize the total cost.
import heapq
import math
from typing import List

class Node:
    def __init__(self, worker_id: int, assigned_jobs: int, cost: int, path: List[int]):
        self.worker_id = worker_id       # Worker to be assigned next
        self.assigned_jobs = assigned_jobs # Bitmask of assigned jobs
        self.cost = cost                 # Cost incurred so far
        self.path = path                 # State path of assignments
        self.bound = 0                   # Lower bound cost

    def __lt__(self, other):
        return self.bound < other.bound

def job_assignment(cost_matrix: List[List[int]]) -> int:
    """
    Approach: Branch and Bound (Least Cost Search).
    We use a priority queue to always explore the most promising (lowest bound) node first.
    The "bound" is the current actual cost PLUS an optimistic estimate of the remaining cost.
    The optimistic estimate is calculated by simply taking the minimum cost available for 
    each unassigned worker, regardless of job conflicts.
    
    By always popping the node with the lowest bound, the FIRST time we reach a complete 
    assignment, we are guaranteed it is the optimal one!
    
    Time: O(N!) in worst case, but heavily pruned.
    Space: O(N * 2^N) space for priority queue states.
    """
    n = len(cost_matrix)
    if n == 0: return 0

    def calculate_bound(node: Node) -> int:
        """Calculate optimistic lower bound for this state."""
        bound = node.cost
        # For each remaining worker, pick their absolute cheapest available job
        for w in range(node.worker_id + 1, n):
            min_cost = math.inf
            for j in range(n):
                # If job j is NOT already assigned in the bitmask
                if not (node.assigned_jobs & (1 << j)):
                    min_cost = min(min_cost, cost_matrix[w][j])
            bound += min_cost
        return bound

    pq = []
    # Root node: before any workers are assigned
    root = Node(-1, 0, 0, [-1]*n)
    root.bound = calculate_bound(root)
    heapq.heappush(pq, root)

    while pq:
        min_node = heapq.heappop(pq)
        
        # Next worker to assign is min_node.worker_id + 1
        i = min_node.worker_id + 1
        
        # If all workers are assigned, we've found the optimal solution
        # (Because we use a min-heap based on bounds, the first complete path is optimal)
        if i == n:
            return min_node.cost
            
        # Try assigning worker `i` to every possible unassigned job `j`
        for j in range(n):
            if not (min_node.assigned_jobs & (1 << j)):
                child_path = min_node.path.copy()
                child_path[i] = j
                
                # Create a child node
                child = Node(
                    worker_id=i, 
                    assigned_jobs=min_node.assigned_jobs | (1 << j), 
                    cost=min_node.cost + cost_matrix[i][j],
                    path=child_path
                )
                child.bound = calculate_bound(child)
                
                heapq.heappush(pq, child)
                
    return 0

# Example usage:
# 4 workers, 4 jobs
costs = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]
print(job_assignment(costs)) # Output: 13 
# (Worker 0 -> Job 1 (2), Worker 1 -> Job 0 (6), Worker 2 -> Job 2 (1), Worker 3 -> Job 3 (4). Total = 13)
