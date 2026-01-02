# Demonstrates queue overflow and underflow handling
class Queue:
    # Simple queue implementation with error handling
    def __init__(self, max_size=10):
        self.items = []
        self.max_size = max_size

    def enqueue(self, item):
        # Add item to the rear of the queue
        if len(self.items) >= self.max_size:
            raise OverflowError("Queue Overflow: Maximum capacity reached")
        self.items.append(item)

    def dequeue(self):
        # Remove item from the front of the queue
        if not self.items:
            raise IndexError("Queue Underflow: Cannot dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        # View front item without removing
        if not self.items:
            raise IndexError("Queue Underflow: Queue is empty")
        return self.items[0]


# Error handling examples:
def demonstrate_errors():
    queue = Queue(max_size=3)

    # Queue Overflow: adding beyond capacity
    try:
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)  # Exceeds max_size
    except OverflowError as e:
        print(f"✓ Caught: {e}")

    # Queue Underflow: removing from empty queue
    try:
        empty_queue = Queue()
        empty_queue.dequeue()
    except IndexError as e:
        print(f"✓ Caught: {e}")

    # Underflow on peek
    try:
        queue.peek()
    except IndexError as e:
        print(f"✓ Caught: {e}")


if __name__ == "__main__":
    demonstrate_errors()