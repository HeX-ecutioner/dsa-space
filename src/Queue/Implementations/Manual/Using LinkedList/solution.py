class Node:
    # Node class for LinkedList

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    # Queue implementation using LinkedList (FIFO - First In First Out)

    def __init__(self):
        # Initialize empty queue
        self.front = None
        self.rear = None

    def enqueue(self, data):
        # Add element to the rear of the queue
        new_node = Node(data)

        # If queue is empty, front and rear point to new node
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(f"Enqueued {data} into queue")

    def dequeue(self):
        # Remove and return front element from queue
        if self.is_empty():
            print("Queue underflow! Cannot dequeue from empty queue")
            return None

        data = self.front.data
        self.front = self.front.next

        # If queue becomes empty after dequeue
        if self.front is None:
            self.rear = None

        print(f"Dequeued {data} from queue")
        return data

    def peek(self):
        # View front element without removing it
        if self.is_empty():
            print("Queue is empty!")
            return None

        print(f"Front element is {self.front.data}")
        return self.front.data

    def is_empty(self):
        # Check if queue is empty
        return self.front is None

    def size(self):
        # Return number of elements in queue
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        # Display all elements in queue from front to rear
        if self.is_empty():
            print("Queue is empty!")
            return

        elements = []
        current = self.front
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Queue (front to rear):", " -> ".join(elements))


# Test the Queue implementation
if __name__ == "__main__":
    queue = Queue()

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
    queue.peek()
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
    queue.dequeue()
