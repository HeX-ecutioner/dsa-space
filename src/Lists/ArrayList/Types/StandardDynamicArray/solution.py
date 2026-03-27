# A minimal reference template for a dynamic array, showing the standard interface without the low-level ctypes implementation (which is handled in the Implementations/Manual folder)

class StandardDynamicArray:
    def __init__(self):
        self.data = [] # Relying on language built-in for simplicity here
        
    def add(self, element):
        # O(1) amortized
        self.data.append(element)
        
    def get(self, index):
        # O(1)
        return self.data[index]
        
    def remove_at(self, index):
        # O(N) because elements after the index must be shifted left
        if index < 0 or index >= len(self.data):
            raise IndexError()
        return self.data.pop(index)

if __name__ == "__main__":
    arr = StandardDynamicArray()
    arr.add(100)
    arr.add(200)
    arr.add(300)
    print("Removed:", arr.remove_at(1)) # Removes 200, shifts 300 to index 1
    print("Element at index 1 is now:", arr.get(1)) # Expected: 300