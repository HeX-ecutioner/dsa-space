# Manual Dynamic Array Implementation

import ctypes # Used to create raw C-style arrays in Python

class DynamicArray:
    def __init__(self):
        self.size = 0       # Count of actual elements
        self.capacity = 1   # Total available slots
        self.array = self._make_array(self.capacity)

    def __len__(self):
        return self.size

    def __getitem__(self, k):
        # Time Complexity: O(1)
        if not 0 <= k < self.size:
            raise IndexError('invalid index')
        return self.array[k]

    def append(self, obj):
        # Time Complexity: O(1) amortized. Worst case O(n) when resizing.
        # Space Complexity: O(n) total allocated space.
        if self.size == self.capacity:
            self._resize(2 * self.capacity) # Double capacity
        
        self.array[self.size] = obj
        self.size += 1

    def _resize(self, new_cap):
        # Time Complexity: O(n) - copying all elements
        new_array = self._make_array(new_cap)
        for k in range(self.size):
            new_array[k] = self.array[k]
        self.array = new_array
        self.capacity = new_cap

    def _make_array(self, capacity):
        # Returns a new array with capacity using ctypes
        return (capacity * ctypes.py_object)()

if __name__ == "__main__":
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    arr.append(3) # Triggers resize
    
    print(f"Array size: {len(arr)}, Capacity: {arr.capacity}") # Expected: Size: 3, Capacity: 4
    print("Index 1:", arr[1]) # Expected: 2