# Static Array Queue (fixed size)
class StaticArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size_count = 0

    def enqueue(self, value):
        # Add element to rear of queue
        if self.size_count == self.capacity:
            raise OverflowError("Queue Overflow")
        self.rear += 1
        self.queue[self.rear] = value
        self.size_count += 1

    def dequeue(self):
        # Remove element from front of queue
        if self.size_count == 0:
            raise IndexError("Queue Underflow")
        value = self.queue[self.front]
        self.front += 1
        self.size_count -= 1
        return value

    def peek(self):
        # View front element without removing
        if self.size_count == 0:
            raise IndexError("Queue is empty")
        return self.queue[self.front]

    def is_empty(self):
        return self.size_count == 0

    def is_full(self):
        return self.size_count == self.capacity

    def size(self):
        return self.size_count


# Dynamic Array Queue using Python list
class DynamicArrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        # Add element to rear of queue
        self.queue.append(value)

    def dequeue(self):
        # Remove element from front of queue
        if not self.queue:
            raise IndexError("Queue Underflow")
        return self.queue.pop(0)

    def peek(self):
        # View front element without removing
        if not self.queue:
            raise IndexError("Queue is empty")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def display(self):
        print(self.queue)


# Example usage:
if __name__ == "__main__":
    # Static Queue
    q1 = StaticArrayQueue(5)
    q1.enqueue(10)
    q1.enqueue(20)
    q1.enqueue(30)
    print(f"Front: {q1.peek()}")       # 10
    print(f"Dequeued: {q1.dequeue()}") # 10
    print(f"Size: {q1.size()}")        # 2

    # Dynamic Queue
    q2 = DynamicArrayQueue()
    q2.enqueue(100)
    q2.enqueue(200)
    print(f"Front: {q2.peek()}")       # 100

    # Additional queue operations
    queue = DynamicArrayQueue()

    print("=== Queue Operations ===\n")

    # Check if empty
    print(f"Is queue empty? {queue.is_empty()}\n")

    # Enqueue elements
    print("--- Enqueuing elements ---")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    print()

    # Display queue
    print("--- Current Queue ---")
    queue.display()
    print(f"Queue size: {queue.size()}\n")

    # Peek at front
    print("--- Peek operation ---")
    print(f"Front: {queue.peek()}")
    print()

    # Dequeue elements
    print("--- Dequeuing elements ---")
    queue.dequeue()
    queue.dequeue()
    print()

    # Display queue after dequeue
    print("--- Queue after dequeuing ---")
    queue.display()
    print(f"Queue size: {queue.size()}\n")

    # Dequeue remaining elements
    print("--- Dequeue all remaining ---")
    queue.dequeue()
    queue.dequeue()
    print()

    # Try to dequeue from empty queue
    print("--- Dequeue from empty queue ---")
    try:
        queue.dequeue()
    except IndexError as e:
        print(f"Error: {e}")
