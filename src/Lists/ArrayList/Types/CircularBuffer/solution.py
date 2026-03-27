# Implement a fixed-size queue-like array that wraps around to the beginning using modulo arithmetic, allowing O(1) enqueue and dequeue.

class CircularBuffer:
    def __init__(self, max_size):
        self.buffer = [None] * max_size
        self.max_size = max_size
        self.head = 0 # Pointer for reading (dequeue)
        self.tail = 0 # Pointer for writing (enqueue)
        self.size = 0 # Current number of elements
        
    def enqueue(self, item):
        # Time Complexity: O(1)
        # Space Complexity: O(N) where N is max_size
        if self.size == self.max_size:
            raise OverflowError("Buffer is full")
            
        self.buffer[self.tail] = item
        # Wrap around using modulo
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1
        
    def dequeue(self):
        # Time Complexity: O(1) - No shifting required!
        if self.size == 0:
            raise IndexError("Buffer is empty")
            
        item = self.buffer[self.head]
        self.buffer[self.head] = None # Clear slot
        # Wrap around using modulo
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return item

if __name__ == "__main__":
    cb = CircularBuffer(3)
    cb.enqueue("A")
    cb.enqueue("B")
    cb.enqueue("C")
    print("Dequeued:", cb.dequeue()) # Expected: A
    cb.enqueue("D") # Wraps around to index 0
    print("Internal Buffer State:", cb.buffer) # Expected: ['D', 'B', 'C']