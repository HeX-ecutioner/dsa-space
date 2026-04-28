class EulerianCircuit:
    @staticmethod
    def hierholzer_directed(vertices, adj):
        """
        Hierholzer's Algorithm to find an Eulerian Path/Circuit in a Directed Graph.
        Assumes the graph has a valid Eulerian Path/Circuit.
        """
        # Calculate in-degrees and out-degrees
        in_degree = {i: 0 for i in range(vertices)}
        out_degree = {i: len(adj.get(i, [])) for i in range(vertices)}
        
        for u in range(vertices):
            for v in adj.get(u, []):
                in_degree[v] += 1
                
        # Find starting node
        start_node = 0
        for i in range(vertices):
            if out_degree[i] - in_degree[i] == 1:
                start_node = i
                break
            if out_degree[i] > 0:
                start_node = i
                
        # Stack for DFS and list for path
        stack = [start_node]
        path = []
        
        # Use a copy of adj so we can pop edges
        adj_copy = {i: list(adj.get(i, [])) for i in range(vertices)}
        
        while stack:
            curr = stack[-1]
            if adj_copy[curr]:
                next_node = adj_copy[curr].pop()
                stack.append(next_node)
            else:
                path.append(stack.pop())
                
        # Path is built backwards
        return path[::-1]

class HamiltonianPath:
    @staticmethod
    def tsp_dp_bitmask(vertices, graph):
        """
        Solves the Travelling Salesperson Problem (Shortest Hamiltonian Cycle)
        using DP with Bitmasking.
        Time: O(N^2 * 2^N), Space: O(N * 2^N)
        """
        memo = {}
        
        def dp(mask, pos):
            # Base case: all nodes visited
            if mask == (1 << vertices) - 1:
                return graph[pos][0] or float('inf') # Return to start
                
            if (mask, pos) in memo:
                return memo[(mask, pos)]
                
            ans = float('inf')
            
            # Try to visit unvisited nodes
            for nxt in range(vertices):
                if (mask & (1 << nxt)) == 0 and graph[pos][nxt] != 0:
                    ans = min(ans, graph[pos][nxt] + dp(mask | (1 << nxt), nxt))
                    
            memo[(mask, pos)] = ans
            return ans
            
        # Start at node 0, mask = 1 (node 0 visited)
        res = dp(1, 0)
        return res if res != float('inf') else -1

# Test Execution
if __name__ == "__main__":
    print("Eulerian Path Example:")
    V_euler = 3
    adj_euler = {0: [1], 1: [2], 2: [0]}
    print(EulerianCircuit.hierholzer_directed(V_euler, adj_euler))
    
    print("\nTSP (Shortest Hamiltonian Cycle) Example:")
    # Complete graph with 4 nodes
    V_tsp = 4
    graph_tsp = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    print("Min cost:", HamiltonianPath.tsp_dp_bitmask(V_tsp, graph_tsp))
