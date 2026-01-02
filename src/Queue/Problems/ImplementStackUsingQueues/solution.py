class MyStack:
    def __init__(self):
        self.queue1 = []  # Main queue (acts like stack top at front)
        self.queue2 = []  # Helper queue

    def push(self, x: int) -> None:
        """
        Push element onto the stack.
        Costly operation: O(n)
        """
        # Step 1: push new element into queue2
        self.queue2.append(x)

        # Step 2: move all elements from queue1 to queue2
        while self.queue1:
            self.queue2.append(self.queue1.pop(0))

        # Step 3: swap queues
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        """
        Remove and return the top element of the stack.
        O(1)
        """
        if not self.queue1:
            raise IndexError("Pop from empty stack")
        return self.queue1.pop(0)

    def top(self) -> int:
        """
        Get the top element without removing it.
        O(1)
        """
        if not self.queue1:
            raise IndexError("Top from empty stack")
        return self.queue1[0]

    def empty(self) -> bool:
        """
        Check if the stack is empty.
        """
        return len(self.queue1) == 0


# Example usage:
if __name__ == "__main__":
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.pop())   # Output: 3
    print(stack.top())   # Output: 2
    print(stack.empty()) # Output: False

    stack.pop()
    stack.pop()
    print(stack.empty()) # Output: True
