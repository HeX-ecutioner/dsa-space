# Problem: Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value. Implement using BFS branch and bound.
import collections
def knapsack_bfs(W, items):
    """
    Approach: Branch and Bound using BFS and a queue.
    Time: O(2^N)
    Space: O(2^N)
    """
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    n = len(items)
    
    def bound(level, weight, profit):
        if weight >= W: return 0
        p_bound = profit
        j = level + 1
        totweight = weight
        while j < n and totweight + items[j][0] <= W:
            totweight += items[j][0]
            p_bound += items[j][1]
            j += 1
        if j < n:
            p_bound += (W - totweight) * (items[j][1]/items[j][0])
        return p_bound

    q = collections.deque([(-1, 0, 0)]) 
    max_profit = 0
    while q:
        level, weight, profit = q.popleft()
        if level == n - 1: continue
        
        next_w = weight + items[level+1][0]
        next_p = profit + items[level+1][1]
        if next_w <= W and next_p > max_profit:
            max_profit = next_p
        
        if bound(level+1, next_w, next_p) > max_profit:
            q.append((level+1, next_w, next_p))
            
        if bound(level+1, weight, profit) > max_profit:
            q.append((level+1, weight, profit))
            
    return max_profit
