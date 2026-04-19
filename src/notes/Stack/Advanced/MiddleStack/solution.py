# Stack with middle element access
class MiddleStack:
    def __init__(self):
        """
        Stack implemented using a Python list.
        Middle element access is O(1) due to random indexing.
        """
        self.stack = []

    def push(self, x):
        """
        Push an element onto the stack.
        Time Complexity: O(1)
        """
        self.stack.append(x)

    def pop(self):
        """
        Pop and return the top element.
        Time Complexity: O(1)
        """
        if not self.stack:
            raise IndexError("Pop from empty stack")
        return self.stack.pop()

    def peek(self):
        """
        Return the top element without removing it.
        Time Complexity: O(1)
        """
        if not self.stack:
            raise IndexError("Peek from empty stack")
        return self.stack[-1]

    def middle(self):
        """
        Return the middle element of the stack.
        For even size, returns the lower middle.
        Time Complexity: O(1)
        """
        if not self.stack:
            raise IndexError("Middle from empty stack")
        return self.stack[len(self.stack) // 2]

    def size(self):
        return len(self.stack)
    
    
# Example usage:
ms = MiddleStack()

ms.push(10)
ms.push(20)
ms.push(30)
ms.push(40)
ms.push(50)

print("Stack size:", ms.size()) # Output: 5
print("Middle element:", ms.middle()) # Output: 30

ms.pop()
print("Middle element:", ms.middle()) # Output: 30

ms.pop()
print("Middle element:", ms.middle()) # Output: 20