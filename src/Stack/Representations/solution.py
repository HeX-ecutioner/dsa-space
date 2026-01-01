class ArrayStack:
    def __init__(self, capacity=10):
        self.stack = [None] * capacity
        self.top = -1
        self.capacity = capacity

    def push(self, item):
        if self.top + 1 >= self.capacity:
            raise Exception("Stack overflow")
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.top == -1:
            raise Exception("Stack underflow")
        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return item

    def peek(self):
        if self.top == -1:
            raise Exception("Stack is empty")
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def size(self):
        return self.top + 1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise Exception("Stack underflow")
        item = self.top.data
        self.top = self.top.next
        return item

    def peek(self):
        if self.top is None:
            raise Exception("Stack is empty")
        return self.top.data

    def is_empty(self):
        return self.top is None


# Example usage:
if __name__ == "__main__":
    # Array Stack
    array_stack = ArrayStack()
    array_stack.push(1)
    array_stack.push(2)
    print(array_stack.pop())  # Output: 2
    array_stack.push(3)
    
    # Linked List Stack
    linked_list_stack = LinkedListStack()
    linked_list_stack.push(1)
    linked_list_stack.push(2)
    print(linked_list_stack.pop())  # Output: 2
    linked_list_stack.push(3)