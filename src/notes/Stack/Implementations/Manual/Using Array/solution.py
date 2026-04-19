# Static Array Stack (fixed size)
class StaticArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def push(self, value):
        if self.top == self.capacity - 1:
            raise OverflowError("Stack Overflow")
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.top == -1:
            raise IndexError("Stack Underflow")
        value = self.stack[self.top]
        self.top -= 1
        return value

    def peek(self):
        # View top element without removing
        if self.top == -1:
            raise IndexError("Stack is empty")
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def size(self):
        return self.top + 1


# Dynamic Array Stack using Python list
class DynamicArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.stack:
            raise IndexError("Stack Underflow")
        return self.stack.pop()

    def peek(self):
        # View top element without removing
        if not self.stack:
            raise IndexError("Stack is empty")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        print(self.stack)


# Example usage:
if __name__ == "__main__":
    # Static Stack
    s1 = StaticArrayStack(5)
    s1.push(10)
    s1.push(20)
    s1.push(30)
    print(f"Top: {s1.peek()}")  # 30
    print(f"Popped: {s1.pop()}")  # 30
    print(f"Size: {s1.size()}")  # 2

    # Dynamic Stack
    s2 = DynamicArrayStack()
    s2.push(100)
    s2.push(200)
    print(f"Top: {s2.peek()}")  # 200

    # Additional stack operations
    stack = DynamicArrayStack()

    print("=== Stack Operations ===\n")

    # Check if empty
    print(f"Is stack empty? {stack.is_empty()}\n")

    # Push elements
    print("--- Pushing elements ---")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    print()

    # Display stack
    print("--- Current Stack ---")
    stack.display()
    print(f"Stack size: {stack.size()}\n")

    # Peek at top
    print("--- Peek operation ---")
    print(f"Top: {stack.peek()}")
    print()

    # Pop elements
    print("--- Popping elements ---")
    stack.pop()
    stack.pop()
    print()

    # Display stack after pop
    print("--- Stack after popping ---")
    stack.display()
    print(f"Stack size: {stack.size()}\n")

    # Pop remaining elements
    print("--- Pop all remaining ---")
    stack.pop()
    stack.pop()
    print()

    # Try to pop from empty stack
    print("--- Pop from empty stack ---")
    try:
        stack.pop()
    except IndexError as e:
        print(f"Error: {e}")
