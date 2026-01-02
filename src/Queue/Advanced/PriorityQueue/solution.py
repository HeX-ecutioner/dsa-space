"""
Priority Queue Implementation in Python

In a priority queue, each element is associated with a priority, based on which elements are removed, rather than insertion order.

Key idea:
- Higher priority elements are processed before lower priority ones
- If priorities are equal, order depends on implementation

Unlike:
- Queue  → FIFO order
- Stack  → LIFO order

Priority Queue:
- Order is determined by priority value

Common use cases:
- CPU scheduling
- Task management systems
- Dijkstra’s shortest path algorithm
- A* search
- Event-driven simulations
"""

# Built-in Priority Queue (heapq)
import heapq

class BuiltInPriorityQueue:
    """
    Priority queue implemented using Python's heapq module.
    heapq implements a MIN-HEAP:
    - The smallest priority value is removed first
    - To simulate max-heap, priorities can be negated
    """

    def __init__(self):
        # Internal heap list
        self.heap = []

    def push(self, priority, item):
        # Insert item with given priority
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        # Remove and return item with highest priority (lowest value)
        if not self.heap:
            raise IndexError("Priority Queue Underflow: Queue is empty")
        return heapq.heappop(self.heap)

    def peek(self):
        # View highest-priority element without removing it
        if not self.heap:
            raise IndexError("Priority Queue is empty")
        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        # Number of elements in the priority queue
        return len(self.heap)


# Manual Priority Queue implementation (array-based)
class ManualPriorityQueue:
    """
    Manual priority queue implementation using a list.

    This implementation maintains the list sorted by priority
    after each insertion.

    Characteristics:
    - Insert: O(n)
    - Remove: O(1)
    - Easy to understand, but not optimal for large datasets
    """

    def __init__(self):
        # List stores (priority, item) tuples
        self.queue = []

    def is_empty(self):
        # Check if queue is empty
        return len(self.queue) == 0

    def push(self, priority, item):
        # Insert item based on priority
        element = (priority, item)

        # If queue is empty, insert directly
        if self.is_empty():
            self.queue.append(element)
            return

        # Find correct position to maintain sorted order
        i = 0
        while i < len(self.queue) and self.queue[i][0] <= priority:
            i += 1

        self.queue.insert(i, element)

    def pop(self):
        # Remove and return highest-priority element
        if self.is_empty():
            raise IndexError("Priority Queue Underflow: Queue is empty")

        # Element with smallest priority value is at front
        return self.queue.pop(0)

    def peek(self):
        # View highest-priority element without removing
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        return self.queue[0]

    def size(self):
        # Number of elements in the priority queue
        return len(self.queue)

    def current_state(self):
        # Return internal state for debugging and learning
        return self.queue


# Example usage:
if __name__ == "__main__":
    print("=== Built-in Priority Queue ===")
    pq1 = BuiltInPriorityQueue()
    pq1.push(3, "Low Priority Task")
    pq1.push(1, "High Priority Task")
    pq1.push(2, "Medium Priority Task")

    print("Peek:", pq1.peek())
    print("Pop:", pq1.pop())
    print("Pop:", pq1.pop())

    print("\n=== Manual Priority Queue ===")
    pq2 = ManualPriorityQueue()
    pq2.push(3, "Low Priority Task")
    pq2.push(1, "High Priority Task")
    pq2.push(2, "Medium Priority Task")

    print("State:", pq2.current_state())
    print("Pop:", pq2.pop())
    print("Pop:", pq2.pop())
