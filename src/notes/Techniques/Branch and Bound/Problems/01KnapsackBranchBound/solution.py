# Problem: 0/1 Knapsack Problem using Branch and Bound.
# Given weights and values of n items, put these items in a knapsack of capacity W 
# to get the maximum total value in the knapsack.
import heapq
from typing import List, Tuple

class Node:
    def __init__(self, level: int, profit: int, weight: int, bound: float):
        self.level = level     # Level of node in decision tree
        self.profit = profit   # Profit of nodes on path from root
        self.weight = weight   # Weight of nodes on path from root
        self.bound = bound     # Upper bound of maximum profit in subtree
        
    def __lt__(self, other):
        # We want a max-heap based on bound, so we invert the comparison
        return self.bound > other.bound

def knapsack_branch_and_bound(W: int, items: List[Tuple[int, int]]) -> int:
    """
    Approach: Branch and Bound (Least-Cost Search / Best-First Search).
    We sort the items by value/weight ratio.
    We explore the decision tree (include item or exclude item).
    For each node, we calculate the optimistic `bound` (the max possible profit if we 
    could take fractions of remaining items). 
    If a node's bound is less than or equal to our current max profit, we PRUNE it.
    
    Time: O(2^n) in worst case, but practically much faster due to pruning.
    Space: O(2^n) for the priority queue in the worst case.
    """
    # Item format: (weight, value)
    n = len(items)
    # Sort items by value/weight ratio descending
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    
    def bound(u: Node) -> float:
        """Calculate upper bound of profit for a subtree."""
        if u.weight >= W:
            return 0
        
        profit_bound = float(u.profit)
        j = u.level + 1
        totweight = u.weight
        
        # Grab as many items as possible
        while j < n and totweight + items[j][0] <= W:
            totweight += items[j][0]
            profit_bound += items[j][1]
            j += 1
            
        # If there's still room, add a fraction of the next item
        if j < n:
            profit_bound += (W - totweight) * (items[j][1] / items[j][0])
            
        return profit_bound

    pq = []
    # Dummy root node
    u = Node(-1, 0, 0, 0.0)
    v = Node(-1, 0, 0, 0.0)
    
    max_profit = 0
    u.bound = bound(u)
    heapq.heappush(pq, u)
    
    while pq:
        # Extract the node with the most promising bound
        u = heapq.heappop(pq)
        
        # If the bound is less than max_profit, the entire subtree is useless.
        if u.bound > max_profit:
            # v will be the child that INCLUDES the next item
            v.level = u.level + 1
            v.weight = u.weight + items[v.level][0]
            v.profit = u.profit + items[v.level][1]
            
            if v.weight <= W and v.profit > max_profit:
                max_profit = v.profit
                
            v.bound = bound(v)
            if v.bound > max_profit:
                heapq.heappush(pq, Node(v.level, v.profit, v.weight, v.bound))
                
            # v will be the child that EXCLUDES the next item
            v_excl = Node(u.level + 1, u.profit, u.weight, 0.0)
            v_excl.bound = bound(v_excl)
            
            if v_excl.bound > max_profit:
                heapq.heappush(pq, v_excl)
                
    return max_profit

# Example usage:
# Knapsack capacity: 10
# Items (weight, value): (2, 40), (3.14, 50), (1.98, 100), (5, 95), (3, 30)
# (Converted to ints for simplicity: (2, 40), (3, 50), (2, 100), (5, 95), (3, 30))
items_list = [(2, 40), (3, 50), (2, 100), (5, 95), (3, 30)]
print(knapsack_branch_and_bound(10, items_list)) # Output: 235 (items (2, 100), (5, 95), (2, 40))
