class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

def reverse_string(input_string):
    stack = Stack()
    
    # Push all characters of the string onto the stack
    for char in input_string:
        stack.push(char)
    
    # Pop all characters from the stack to get the reversed string
    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

# Example usage:
if __name__ == "__main__":
    input_str = "Hello, World!"
    print("Original String:", input_str)
    print("Reversed String:", reverse_string(input_str))