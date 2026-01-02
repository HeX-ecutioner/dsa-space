"""
Multi-Level Queue Implementation in Python

A Multi-Level Queue is a scheduling data structure that maintains
MULTIPLE QUEUES, each representing a different priority level.

Key characteristics:
- Each queue follows FIFO order
- Higher-priority queues are always served before lower-priority queues
- Processes are permanently assigned to one queue (no movement between levels)

Unlike:
- Simple Queue        → single FIFO line
- Priority Queue      → priority per element
- Round Robin Queue   → time slicing

Multi-Level Queue:
- Priority is decided by WHICH queue, not by individual elements

Common use cases:
- Operating System CPU scheduling
- Network packet scheduling
- Task schedulers with priority classes
- Real-time systems
"""

from collections import deque
class MultiLevelQueue: # Multi-Level Queue implementation using multiple FIFO queues

    def __init__(self, levels):
        """
        Initialize the multi-level queue.
        levels: number of priority levels (0 = highest priority)
        """
        self.levels = levels
        self.queues = [deque() for _ in range(levels)]

    # -------------------------------
    # Enqueue Operation
    # -------------------------------
    def enqueue(self, item, priority):
        """
        Insert an item into the queue corresponding to its priority level.
        priority: 0 (highest) to levels-1 (lowest)
        """
        if priority < 0 or priority >= self.levels:
            raise ValueError("Invalid priority level")

        self.queues[priority].append(item)

    # -------------------------------
    # Dequeue Operation
    # -------------------------------
    def dequeue(self):
        # Remove and return an item from the highest-priority non-empty queue
        for level in range(self.levels):
            if self.queues[level]:
                return self.queues[level].popleft()

        raise IndexError("Multi-Level Queue Underflow: All queues are empty")

    # -------------------------------
    # Peek Operation
    # -------------------------------
    def peek(self):
        # Return the next item to be dequeued without removing it
        for level in range(self.levels):
            if self.queues[level]:
                return self.queues[level][0]

        raise IndexError("Multi-Level Queue is empty")

    # -------------------------------
    # Helper Methods
    # -------------------------------
    def is_empty(self):
        # Check if all queues are empty
        return all(len(q) == 0 for q in self.queues)

    def current_state(self):
        # Return the current state of all queues. Useful for debugging
        return {
            f"Priority {i}": list(self.queues[i])
            for i in range(self.levels)
        }

# Example usage:
if __name__ == "__main__":
    print("=== Multi-Level Queue ===")

    # Create a multi-level queue with 3 priority levels
    # 0 → High priority
    # 1 → Medium priority
    # 2 → Low priority
    mlq = MultiLevelQueue(levels=3)

    # Enqueue tasks
    mlq.enqueue("System Task", priority=0)
    mlq.enqueue("User Task 1", priority=1)
    mlq.enqueue("Background Task", priority=2)
    mlq.enqueue("User Task 2", priority=1)
    mlq.enqueue("Interrupt Handler", priority=0)

    print("State:", mlq.current_state())

    # Dequeue tasks (higher priority first)
    print("Dequeued:", mlq.dequeue())  # System Task
    print("Dequeued:", mlq.dequeue())  # Interrupt Handler
    print("Dequeued:", mlq.dequeue())  # User Task 1
    print("Dequeued:", mlq.dequeue())  # User Task 2
    print("Dequeued:", mlq.dequeue())  # Background Task

    print("Is Empty:", mlq.is_empty())