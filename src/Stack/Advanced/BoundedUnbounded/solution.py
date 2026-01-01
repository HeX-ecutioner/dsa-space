class BoundedStack(list):
    # Stack with maximum size limit
    def __init__(self, limit):
        super().__init__()
        self.limit = limit

    def push(self, x):
        # Add element if stack is not full
        if len(self) == self.limit:
            raise OverflowError("Stack is full")
        self.append(x)

    def pop(self):
        # Remove and return top element
        if len(self) == 0:
            raise IndexError("pop from empty stack")
        return super().pop()

    def peek(self):
        # Return top element without removing
        if len(self) == 0:
            raise IndexError("peek from empty stack")
        return self[-1]

    def is_empty(self):
        # Check if stack is empty
        return len(self) == 0
    

class UnboundedStack(list):
    # Stack with no size limit
    def push(self, x):
        # Add element to stack
        self.append(x)

    def pop(self):
        # Remove and return top element
        if len(self) == 0:
            raise IndexError("pop from empty stack")
        return super().pop()

    def peek(self):
        # Return top element without removing
        if len(self) == 0:
            raise IndexError("peek from empty stack")
        return self[-1]

    def is_empty(self):
        # Check if stack is empty
        return len(self) == 0


# Example usage:
if __name__ == "__main__":
    # Bounded stack example
    bounded = BoundedStack(3)
    bounded.push(10)
    bounded.push(20)
    bounded.push(30)
    try:
        bounded.push(40)  # Will raise OverflowError
    except OverflowError as e:
        print(f"Bounded stack is full! {e}")
    # Unbounded stack example
    unbounded = UnboundedStack()
    unbounded.push(1)
    unbounded.push(2)
    unbounded.push(3)
    print(f"Unbounded peek: {unbounded.peek()}")
    print(f"Unbounded pop: {unbounded.pop()}")