"""
Deque (Double-Ended Queue) Implementation in Python

A deque (pronounced "deck") is a linear data structure that allows insertion
and removal of elements from BOTH ends efficiently.

Unlike:
- Stack  → insert/remove from one end (LIFO)
- Queue  → insert at rear, remove from front (FIFO)

Deque allows:
- add/remove from FRONT
- add/remove from REAR

This flexibility makes deque useful for:
- Sliding window problems
- Palindrome checking
- Undo/Redo systems
- Task scheduling
- BFS and level-order traversal
"""

# 1. Built-in Deque implementation (collections.deque)
from collections import deque

class BuiltInDeque:
    # Deque implemented using Python's built-in collections.deque. This is the most efficient and recommended deque implementation in Python
    def __init__(self):
        # Initialize an empty deque
        self.deque = deque()

    def add_front(self, item):
        # Insert element at the front of the deque
        self.deque.appendleft(item)

    def add_rear(self, item):
        # Insert element at the rear of the deque
        self.deque.append(item)

    def remove_front(self):
        # Remove and return element from the front
        if not self.deque:
            raise IndexError("Deque Underflow: Deque is empty")
        return self.deque.popleft()

    def remove_rear(self):
        # Remove and return element from the rear
        if not self.deque:
            raise IndexError("Deque Underflow: Deque is empty")
        return self.deque.pop()

    def peek_front(self):
        # Return front element without removing it
        if not self.deque:
            raise IndexError("Deque is empty")
        return self.deque[0]

    def peek_rear(self):
        # Return rear element without removing it
        if not self.deque:
            raise IndexError("Deque is empty")
        return self.deque[-1]

    def is_empty(self):
        return len(self.deque) == 0

    def size(self):
        return len(self.deque)


# Manual Deque implementation (circular array)
class ManualDeque:
    """
    Manual deque implementation using a circular array.
    This implementation demonstrates how a deque works internally using fixed-size memory and pointer arithmetic.
    """

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.deque = [None] * capacity
        self.front = -1
        self.rear = 0
        self.size = 0

    # -------------------------------
    # Helper methods
    # -------------------------------
    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    # -------------------------------
    # Insertion Operations
    # -------------------------------
    def add_front(self, item):
        if self.is_full():
            raise OverflowError("Deque Overflow: Deque is full")

        # First insertion
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1 + self.capacity) % self.capacity

        self.deque[self.front] = item
        self.size += 1

    def add_rear(self, item):
        if self.is_full():
            raise OverflowError("Deque Overflow: Deque is full")

        # First insertion
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity

        self.deque[self.rear] = item
        self.size += 1

    # -------------------------------
    # Deletion Operations
    # -------------------------------
    def remove_front(self):
        """Remove element from the front"""
        if self.is_empty():
            raise IndexError("Deque Underflow: Deque is empty")

        value = self.deque[self.front]
        self.deque[self.front] = None

        # Single element case
        if self.front == self.rear:
            self.front = -1
            self.rear = 0
        else:
            self.front = (self.front + 1) % self.capacity

        self.size -= 1
        return value

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("Deque Underflow: Deque is empty")

        value = self.deque[self.rear]
        self.deque[self.rear] = None

        # Single element case
        if self.front == self.rear:
            self.front = -1
            self.rear = 0
        else:
            self.rear = (self.rear - 1 + self.capacity) % self.capacity

        self.size -= 1
        return value

    # -------------------------------
    # Peek Operations
    # -------------------------------
    def peek_front(self):
        # Return front element without removing it
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.deque[self.front]

    def peek_rear(self):
        # Return rear element without removing it
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.deque[self.rear]

    def current_state(self):
        # Return internal state for debugging and learning purposes
        return {
            "deque": self.deque,
            "front_index": self.front,
            "rear_index": self.rear,
            "size": self.size
        }


# Example usage:
if __name__ == "__main__":
    print("=== Built-in Deque ===")
    d1 = BuiltInDeque()
    d1.add_front(10)
    d1.add_rear(20)
    d1.add_front(5)
    print("Front:", d1.peek_front())
    print("Rear:", d1.peek_rear())
    print("Remove Front:", d1.remove_front())
    print("Remove Rear:", d1.remove_rear())

    print("\n=== Manual Deque ===")
    d2 = ManualDeque(capacity=5)
    d2.add_rear(1)
    d2.add_rear(2)
    d2.add_front(0)
    print("State:", d2.current_state())
    print("Remove Front:", d2.remove_front())
    print("Remove Rear:", d2.remove_rear())
    print("State:", d2.current_state())