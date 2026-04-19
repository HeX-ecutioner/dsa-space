"""
Circular Queue Implementation in Python

A circular queue is a variation of a queue where the last position is connected back to the first position, forming a circle.

Why circular queue?
- In a normal array-based queue, dequeued spaces cannot be reused.
- A circular queue efficiently reuses empty spaces by wrapping around.

Key idea:
- FIFO (First In, First Out)
- Uses modulo arithmetic (%) to move front and rear pointers.
- Prevents wasted memory.

Common use cases:
- CPU scheduling
- Memory buffering
- Streaming data
- Producer-consumer problems
"""

# Built-in Circular Queue (collections.deque)
from collections import deque # collections.deque internally supports efficient rotation and constant-time enqueue and dequeue operations

class BuiltInCircularQueue:

    def __init__(self, capacity):
        # Maximum number of elements allowed
        self.capacity = capacity
        # Deque with fixed max length behaves like a circular queue
        self.queue = deque(maxlen=capacity)

    def enqueue(self, item):
        # Insert element at the rear
        if len(self.queue) == self.capacity:
            raise OverflowError("Circular Queue Overflow: Queue is full")
        self.queue.append(item)

    def dequeue(self):
        # Remove element from the front
        if not self.queue:
            raise IndexError("Circular Queue Underflow: Queue is empty")
        return self.queue.popleft()

    def front(self):
        # View front element without removing
        if not self.queue:
            raise IndexError("Queue is empty")
        return self.queue[0]

    def rear(self):
        # View rear element without removing
        if not self.queue:
            raise IndexError("Queue is empty")
        return self.queue[-1]

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def size(self):
        # Current number of elements
        return len(self.queue)


# Manual Circular Queue implementation (array-based)
class CircularQueue:
    """
    Manual circular queue implementation using a fixed-size array.
    This version demonstrates how circular queues work internally using front and rear pointers with modulo arithmetic.
    """

    def __init__(self, capacity):
        # Fixed size of the queue
        self.capacity = capacity
        # Array to store queue elements
        self.queue = [None] * capacity
        # Front points to the first element
        self.front = -1
        # Rear points to the last element
        self.rear = -1
        # Number of elements in the queue
        self.size = 0

    # -------------------------------
    # Helper methods
    # -------------------------------
    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    # -------------------------------
    # Core operations
    # -------------------------------
    def enqueue(self, item):
        # Add element at the rear of the queue
        if self.is_full():
            raise OverflowError("Circular Queue Overflow: Queue is full")

        # First insertion
        if self.is_empty():
            self.front = self.rear = 0
        else:
            # Move rear circularly
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        # Remove element from the front of the queue
        if self.is_empty():
            raise IndexError("Circular Queue Underflow: Queue is empty")

        value = self.queue[self.front]
        self.queue[self.front] = None

        # If only one element was present
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            # Move front circularly
            self.front = (self.front + 1) % self.capacity

        self.size -= 1
        return value

    # -------------------------------
    # Peek operations
    # -------------------------------
    def peek_front(self):
        # View front element without removing
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]

    def peek_rear(self):
        # View rear element without removing
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.rear]

    # -------------------------------
    # Debugging and learning helper
    # -------------------------------
    def current_state(self):
        # Return internal state for visualization
        return {
            "queue": self.queue,
            "front_index": self.front,
            "rear_index": self.rear,
            "size": self.size,
        }


# Example usage:
if __name__ == "__main__":
    print("=== Built-in Circular Queue ===")
    cq1 = BuiltInCircularQueue(capacity=3)
    cq1.enqueue(10)
    cq1.enqueue(20)
    cq1.enqueue(30)
    print("Front:", cq1.front())
    print("Rear:", cq1.rear())
    print("Dequeue:", cq1.dequeue())
    cq1.enqueue(40)
    print("Queue Size:", cq1.size())

    print("\n=== Manual Circular Queue ===")
    cq2 = CircularQueue(capacity=4)
    cq2.enqueue(1)
    cq2.enqueue(2)
    cq2.enqueue(3)
    print("State:", cq2.current_state())
    print("Dequeue:", cq2.dequeue())
    cq2.enqueue(4)
    print("Front:", cq2.peek_front())
    print("Rear:", cq2.peek_rear())
    print("State:", cq2.current_state())
