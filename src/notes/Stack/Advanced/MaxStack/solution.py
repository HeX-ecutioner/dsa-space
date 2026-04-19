# Stack supporting getMax() in O(1)
class MaxStack:
    def __init__(self):
        """
        Initialize two stacks:
        - stack: stores all pushed values
        - max_stack: stores the maximum value at each level
        """
        self.stack = []
        self.max_stack = []

    def push(self, x):
        """
        Push an element onto the stack.

        If the max_stack is empty OR the new element is
        greater than or equal to the current maximum,
        push it onto max_stack as well.
        """
        self.stack.append(x)

        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self):
        """
        Pop and return the top element from the stack.

        If the popped element is equal to the current maximum,
        pop it from max_stack as well.
        """
        if not self.stack:
            raise IndexError("Pop from empty stack")

        val = self.stack.pop()

        if val == self.max_stack[-1]:
            self.max_stack.pop()

        return val

    def get_max(self):
        """
        Return the maximum element in the stack in O(1) time.
        """
        if not self.max_stack:
            raise IndexError("Max from empty stack")

        return self.max_stack[-1]

    def peek(self):
        """
        Return the top element without removing it.
        """
        if not self.stack:
            raise IndexError("Peek from empty stack")

        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

# Example usage:
ms = MaxStack()
ms.push(5)
ms.push(3)
ms.push(7)
ms.push(7)
ms.push(2)

print("Current max:", ms.get_max())  # Output: 7

print("Popped:", ms.pop())           # Output: 2
print("Current max:", ms.get_max())  # Output: 7

print("Popped:", ms.pop())           # Output: 7
print("Current max:", ms.get_max())  # Output: 7

print("Popped:", ms.pop())           # Output: 7
print("Current max:", ms.get_max())  # Output: 5