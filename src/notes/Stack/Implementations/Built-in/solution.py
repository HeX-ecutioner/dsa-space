from collections import deque # Stack Implementation using Python's built-in collections.deque

class Stack:
    # A Stack implementation using deque for efficient operations.
    
    def __init__(self):
        # Initialize an empty stack.
        self.items = deque()
    
    def push(self, item):
        # Add an item to the top of the stack.
        self.items.append(item)
        print(f"Pushed: {item}")
    
    def pop(self):
        # Remove and return the top item from the stack.
        if not self.is_empty():
            item = self.items.pop()
            print(f"Popped: {item}")
            return item
        else:
            print("Stack is empty! Cannot pop.")
            return None
    
    def peek(self):
        # Return the top item without removing it.
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty!")
            return None
    
    def is_empty(self):
        # Check if the stack is empty.
        return len(self.items) == 0
    
    def size(self):
        # Return the number of items in the stack.
        return len(self.items)
    
    def display(self):
        # Display all items in the stack.
        if self.is_empty():
            print("Stack is empty!")
        else:
            print(f"Stack (top to bottom): {list(reversed(self.items))}")


# Demonstration of Stack functionalities
if __name__ == "__main__":
    stack = Stack()
    
    print("=== Stack Operations ===\n")
    
    # Push operations
    print("1. Push Operations:")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    print()
    
    # Display stack
    print("2. Display Stack:")
    stack.display()
    print()
    
    # Peek operation
    print("3. Peek Operation:")
    top = stack.peek()
    print(f"Top element: {top}\n")
    
    # Size operation
    print("4. Stack Size:")
    print(f"Size: {stack.size()}\n")
    
    # Pop operations
    print("5. Pop Operations:")
    stack.pop()
    stack.pop()
    print()
    
    # Display after pop
    print("6. Display Stack after Pop:")
    stack.display()
    print()
    
    # Check if empty
    print("7. Is Empty Check:")
    print(f"Is empty: {stack.is_empty()}\n")
    
    # Pop remaining elements
    print("8. Pop Remaining Elements:")
    stack.pop()
    stack.pop()
    print()
    
    # Try pop on empty stack
    print("9. Pop on Empty Stack:")
    stack.pop()