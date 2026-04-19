class BoundedQueue:
    # Queue with maximum size limit (FIFO)

    def __init__(self, limit):
        self.queue = []
        self.limit = limit

    def enqueue(self, x):
        # Add element to rear if queue is not full
        if len(self.queue) == self.limit:
            raise OverflowError("Queue is full")
        self.queue.append(x)

    def dequeue(self):
        # Remove and return front element
        if len(self.queue) == 0:
            raise IndexError("dequeue from empty queue")
        return self.queue.pop(0)

    def peek(self):
        # Return front element without removing
        if len(self.queue) == 0:
            raise IndexError("peek from empty queue")
        return self.queue[0]

    def is_empty(self):
        # Check if queue is empty
        return len(self.queue) == 0


class UnboundedQueue:
    # Queue with no size limit (FIFO)

    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        # Add element to rear
        self.queue.append(x)

    def dequeue(self):
        # Remove and return front element
        if len(self.queue) == 0:
            raise IndexError("dequeue from empty queue")
        return self.queue.pop(0)

    def peek(self):
        # Return front element without removing
        if len(self.queue) == 0:
            raise IndexError("peek from empty queue")
        return self.queue[0]

    def is_empty(self):
        # Check if queue is empty
        return len(self.queue) == 0


# Example usage:
if __name__ == "__main__":
    # Bounded queue example
    bounded = BoundedQueue(3)
    bounded.enqueue(10)
    bounded.enqueue(20)
    bounded.enqueue(30)
    try:
        bounded.enqueue(40)  # Will raise OverflowError
    except OverflowError as e:
        print(f"Bounded queue is full! {e}")

    # Unbounded queue example
    unbounded = UnboundedQueue()
    unbounded.enqueue(1)
    unbounded.enqueue(2)
    unbounded.enqueue(3)
    print(f"Unbounded peek: {unbounded.peek()}")
    print(f"Unbounded dequeue: {unbounded.dequeue()}")