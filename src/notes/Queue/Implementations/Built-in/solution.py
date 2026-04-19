from collections import deque  # Queue implementation using Python's built-in collections.deque

class Queue:
    # A Queue implementation using deque for efficient FIFO operations.

    def __init__(self):
        # Initialize an empty queue.
        self.items = deque()

    def enqueue(self, item):
        # Add an item to the rear of the queue.
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        # Remove and return the front item from the queue.
        if not self.is_empty():
            item = self.items.popleft()
            print(f"Dequeued: {item}")
            return item
        else:
            print("Queue is empty! Cannot dequeue.")
            return None

    def peek(self):
        # Return the front item without removing it.
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty!")
            return None

    def is_empty(self):
        # Check if the queue is empty.
        return len(self.items) == 0

    def size(self):
        # Return the number of items in the queue.
        return len(self.items)

    def display(self):
        # Display all items in the queue.
        if self.is_empty():
            print("Queue is empty!")
        else:
            print(f"Queue (front to rear): {list(self.items)}")


# Demonstration of Queue functionalities
if __name__ == "__main__":
    queue = Queue()

    print("=== Queue Operations ===\n")

    # Enqueue operations
    print("1. Enqueue Operations:")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    print()

    # Display queue
    print("2. Display Queue:")
    queue.display()
    print()

    # Peek operation
    print("3. Peek Operation:")
    front = queue.peek()
    print(f"Front element: {front}\n")

    # Size operation
    print("4. Queue Size:")
    print(f"Size: {queue.size()}\n")

    # Dequeue operations
    print("5. Dequeue Operations:")
    queue.dequeue()
    queue.dequeue()
    print()

    # Display after dequeue
    print("6. Display Queue after Dequeue:")
    queue.display()
    print()

    # Check if empty
    print("7. Is Empty Check:")
    print(f"Is empty: {queue.is_empty()}\n")

    # Dequeue remaining elements
    print("8. Dequeue Remaining Elements:")
    queue.dequeue()
    queue.dequeue()
    print()

    # Try dequeue on empty queue
    print("9. Dequeue on Empty Queue:")
    queue.dequeue()