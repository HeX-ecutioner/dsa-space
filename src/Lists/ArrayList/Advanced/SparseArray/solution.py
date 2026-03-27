# Implement an array that is mostly empty using a Hash Map to save memory.

class SparseArray:
    def __init__(self, size):
        # Time/Space Complexity for init: O(1)
        self.size = size
        self.data = {} # Dictionary stores only non-default values

    def set(self, index, value):
        # Time Complexity: O(1) average
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if value == 0:
             # Remove from map to save space if it's the default value
            if index in self.data:
                del self.data[index]
        else:
            self.data[index] = value

    def get(self, index):
        # Time Complexity: O(1) average
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.data.get(index, 0) # Return 0 if not explicitly set

if __name__ == "__main__":
    # Create an array of 1 million elements, but only use a few bytes!
    sparse = SparseArray(1000000)
    sparse.set(500, 42)
    sparse.set(999999, 100)
    
    print("Index 500:", sparse.get(500)) # Expected: 42
    print("Index 10:", sparse.get(10))   # Expected: 0
    print("Internal Map:", sparse.data)  # Expected: {500: 42, 999999: 100}