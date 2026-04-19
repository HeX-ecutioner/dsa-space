class Node:
    # Node class for LinkedList

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    # Stack implementation using LinkedList (LIFO - Last In First Out)

    def __init__(self):
        # Initialize empty stack
        self.top = None

    def push(self, data):
        # Add element to the top of stack
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed {data} onto stack")

    def pop(self):
        # Remove and return top element from stack
        if self.is_empty():
            print("Stack underflow! Cannot pop from empty stack")
            return None

        data = self.top.data
        self.top = self.top.next
        print(f"Popped {data} from stack")
        return data

    def peek(self):
        # View top element without removing it
        if self.is_empty():
            print("Stack is empty!")
            return None

        print(f"Top element is {self.top.data}")
        return self.top.data

    def is_empty(self):
        # Check if stack is empty
        return self.top is None

    def size(self):
        # Return number of elements in stack
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        # Display all elements in stack from top to bottom
        if self.is_empty():
            print("Stack is empty!")
            return

        elements = []
        current = self.top
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Stack (top to bottom):", " -> ".join(elements))


# Test the Stack implementation
if __name__ == "__main__":
    stack = Stack()

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
    stack.peek()
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
    stack.pop()
