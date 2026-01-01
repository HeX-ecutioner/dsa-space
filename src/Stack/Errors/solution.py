# Demonstrates stack overflow and underflow handling

class Stack:
    # Simple stack implementation with error handling
    def __init__(self, max_size=10):
        self.items = []
        self.max_size = max_size
    
    def push(self, item):
        # Push item onto stack
        if len(self.items) >= self.max_size:
            raise OverflowError("Stack Overflow: Maximum capacity reached")
        self.items.append(item)
    
    def pop(self):
        # Pop item from stack
        if not self.items:
            raise IndexError("Stack Underflow: Cannot pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        # View top item without removing
        if not self.items:
            raise IndexError("Stack Underflow: Stack is empty")
        return self.items[-1]


# Error handling examples:
def demonstrate_errors():
    stack = Stack(max_size=3)
    
    # Stack Overflow - adding beyond capacity
    try:
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)  # Exceeds max_size
    except OverflowError as e:
        print(f"✓ Caught: {e}")
    
    # Stack Underflow - removing from empty stack
    try:
        empty_stack = Stack()
        empty_stack.pop()
    except IndexError as e:
        print(f"✓ Caught: {e}")
    
    # Underflow on peek
    try:
        stack.peek()
    except IndexError as e:
        print(f"✓ Caught: {e}")


if __name__ == "__main__":
    demonstrate_errors()
