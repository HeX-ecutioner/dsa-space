class MyQueue:
    def __init__(self):
        self.stack1 = []  # For push operations
        self.stack2 = []  # For pop operations

    def push(self, x: int) -> None:
        """Add element to the back of the queue"""
        self.stack1.append(x)

    def pop(self) -> int:
        """Remove and return element from the front of the queue"""
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        """Get the front element without removing it"""
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        """Check if the queue is empty"""
        return len(self.stack1) == 0 and len(self.stack2) == 0


# Example usage:
if __name__ == "__main__":
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.pop())  # Output: 1
    print(queue.peek())  # Output: 2
    print(queue.empty())  # Output: False
    queue.pop()
    queue.pop()
    print(queue.empty())  # Output: True
