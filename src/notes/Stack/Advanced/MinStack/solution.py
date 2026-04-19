# Stack supporting getMin() in O(1)
class MinStack:
    def __init__(self):
        """
        Initialize two stacks:
        - stack: stores all pushed values
        - min_stack: stores the minimum value at each level
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        Push an element onto the stack.

        If the min_stack is empty OR the new element is
        less than or equal to the current minimum,
        push it onto min_stack as well.
        """
        self.stack.append(x)

        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        """
        Pop and return the top element from the stack.

        If the popped element is equal to the current minimum,
        pop it from min_stack as well.
        """
        if not self.stack:
            raise IndexError("Pop from empty stack")

        val = self.stack.pop()

        if val == self.min_stack[-1]:
            self.min_stack.pop()

        return val

    def get_min(self):
        if not self.min_stack: # Return the minimum element in the stack in O(1) time
            raise IndexError("Min from empty stack")

        return self.min_stack[-1]

    def peek(self):
        if not self.stack: # Return the top element without removing it
            raise IndexError("Peek from empty stack")

        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


# Example usage:
ms = MinStack()
ms.push(5)
ms.push(3)
ms.push(7)
ms.push(3)

print("Current min:", ms.get_min())  # Output: 3

print("Popped:", ms.pop())           # Output: 3
print("Current min:", ms.get_min())  # Output: 3

print("Popped:", ms.pop())           # Output: 7
print("Current min:", ms.get_min())  # Output: 3

print("Popped:", ms.pop())           # Output: 3
print("Current min:", ms.get_min())  # Output: 5