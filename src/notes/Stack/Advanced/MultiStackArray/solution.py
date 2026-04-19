# Two stacks in one array
class TwoStacks:
    def __init__(self, n):
        """
        Initialize an array of size n to hold two stacks.

        Stack 1 starts from index 0 and grows to the right.
        Stack 2 starts from index n-1 and grows to the left.
        """
        self.arr = [None] * n
        self.top1 = -1        # Top pointer for Stack 1
        self.top2 = n         # Top pointer for Stack 2

    def push1(self, x):
        """
        Push an element onto Stack 1.
        """
        # Check for overflow (no space left)
        if self.top1 + 1 == self.top2:
            raise OverflowError("Stack Overflow: No space left to push into Stack 1")

        self.top1 += 1
        self.arr[self.top1] = x

    def push2(self, x):
        """
        Push an element onto Stack 2.
        """
        # Check for overflow (no space left)
        if self.top1 + 1 == self.top2:
            raise OverflowError("Stack Overflow: No space left to push into Stack 2")

        self.top2 -= 1
        self.arr[self.top2] = x

    def pop1(self):
        """
        Pop and return the top element from Stack 1.
        """
        if self.top1 == -1:
            raise IndexError("Stack 1 Underflow: Stack 1 is empty")

        value = self.arr[self.top1]
        self.arr[self.top1] = None  # Optional cleanup
        self.top1 -= 1
        return value

    def pop2(self):
        """
        Pop and return the top element from Stack 2.
        """
        if self.top2 == len(self.arr):
            raise IndexError("Stack 2 Underflow: Stack 2 is empty")

        value = self.arr[self.top2]
        self.arr[self.top2] = None  # Optional cleanup
        self.top2 += 1
        return value

    def peek1(self):
        """
        Return the top element of Stack 1 without removing it.
        """
        if self.top1 == -1:
            raise IndexError("Stack 1 is empty")

        return self.arr[self.top1]

    def peek2(self):
        """
        Return the top element of Stack 2 without removing it.
        """
        if self.top2 == len(self.arr):
            raise IndexError("Stack 2 is empty")

        return self.arr[self.top2]

    def __str__(self):
        """
        Utility method to visualize the array and stack pointers.
        """
        return f"Array: {self.arr}\nTop1: {self.top1}, Top2: {self.top2}"
    
    
# Example usage:
stacks = TwoStacks(6) # Create a TwoStacks object with array size 6

# Push elements into Stack 1
stacks.push1(10)
stacks.push1(20)
stacks.push1(30)

# Push elements into Stack 2
stacks.push2(60)
stacks.push2(50)

print(stacks) # Output: [10, 20, 30, None, 50, 60]
# Top1: 2, Top2: 4

# Peek top elements
print("Top of Stack 1:", stacks.peek1())  # 30
print("Top of Stack 2:", stacks.peek2())  # 50

# Pop elements
print("Popped from Stack 1:", stacks.pop1())  # 30
print("Popped from Stack 2:", stacks.pop2())  # 50

print(stacks) # Output: [10, 20, None, None, None, 60]
# Top1: 1, Top2: 5