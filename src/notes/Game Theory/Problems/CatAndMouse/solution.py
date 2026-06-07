from collections import deque
from typing import List

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        MOUSE_TURN, CAT_TURN = 1, 2
        DRAW, MOUSE_WINS, CAT_WINS = 0, 1, 2
        
        # degree[m][c][t] = number of valid moves from state (m, c, t)
        degree = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
        
        # result[m][c][t] = status of state (m, c, t)
        result = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
        
        for m in range(n):
            for c in range(n):
                degree[m][c][MOUSE_TURN] = len(graph[m])
                # Cat cannot move to hole 0
                degree[m][c][CAT_TURN] = len(graph[c]) - (1 if 0 in graph[c] else 0)
                
        queue = deque()
        
        # 1. Enqueue terminal states
        for i in range(n):
            for t in (MOUSE_TURN, CAT_TURN):
                # Mouse reached hole (Mouse wins)
                result[0][i][t] = MOUSE_WINS
                queue.append((0, i, t, MOUSE_WINS))
                
                # Cat caught Mouse (Cat wins), hole is excluded because Mouse wins instantly if at 0
                if i > 0:
                    result[i][i][t] = CAT_WINS
                    queue.append((i, i, t, CAT_WINS))
                    
        # Helper to get predecessors of a state
        def get_predecessors(m, c, t):
            if t == MOUSE_TURN:
                # If it's Mouse's turn now, the previous turn was Cat's
                for prev_c in graph[c]:
                    if prev_c != 0:
                        yield (m, prev_c, CAT_TURN)
            else:
                # If it's Cat's turn now, the previous turn was Mouse's
                for prev_m in graph[m]:
                    yield (prev_m, c, MOUSE_TURN)
                    
        # 2. Retrograde Analysis (Bottom-Up BFS)
        while queue:
            m, c, t, status = queue.popleft()
            
            for prev_m, prev_c, prev_t in get_predecessors(m, c, t):
                if result[prev_m][prev_c][prev_t] == DRAW: # If unresolved
                    # If the next state is a win for the player whose turn it is NOW
                    # (e.g., Mouse wins and it was Mouse's turn) -> They will definitely make this move
                    if (prev_t == MOUSE_TURN and status == MOUSE_WINS) or \
                       (prev_t == CAT_TURN and status == CAT_WINS):
                        result[prev_m][prev_c][prev_t] = status
                        queue.append((prev_m, prev_c, prev_t, status))
                    else:
                        # The next state is a losing state for the current player
                        # Decrement out-degree. If it reaches 0, ALL choices lead to a loss.
                        degree[prev_m][prev_c][prev_t] -= 1
                        if degree[prev_m][prev_c][prev_t] == 0:
                            # If all options lead to a loss, this state is a losing state
                            losing_status = CAT_WINS if prev_t == MOUSE_TURN else MOUSE_WINS
                            result[prev_m][prev_c][prev_t] = losing_status
                            queue.append((prev_m, prev_c, prev_t, losing_status))
                            
        return result[1][2][MOUSE_TURN]

# --- Example Usage ---
# sol = Solution()
# graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
# print(sol.catMouseGame(graph)) # Output: 0 (Draw)
