# Problem: Implement Round Robin CPU Scheduling using a queue
from collections import deque

def round_robin(processes, burst_time, quantum):
    """
    Round Robin CPU Scheduling is a preemptive scheduling algorithm where each process is assigned a fixed time slot (quantum) in a
    cyclic order. This ensures that all processes get an equal share of the CPU time and prevents starvation.
    
    Time Complexity: O(n * (burst_time / quantum))
    Space Complexity: O(n)
    """
    queue = deque()
    remaining_bt = burst_time[:]
    time = 0
    completion_time = [0] * len(processes)

    # Enqueue all processes initially
    for i in range(len(processes)):
        queue.append(i)

    while queue:
        i = queue.popleft()

        if remaining_bt[i] > quantum:
            time += quantum
            remaining_bt[i] -= quantum
            queue.append(i)
        else:
            time += remaining_bt[i]
            completion_time[i] = time
            remaining_bt[i] = 0

    return completion_time


# Example usage:
processes = [1, 2, 3]
burst_time = [10, 5, 8]
quantum = 2
print(round_robin(processes, burst_time, quantum)) # Output: [23, 15, 21]