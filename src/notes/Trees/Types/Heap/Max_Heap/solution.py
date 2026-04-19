"""
Problem: Manual Max Heap Implementation
Statement: Implement an array-based Max Heap to demonstrate inverse ordering.
"""

class MaxHeap:
    # Time Complexity: Push O(log N), Pop O(log N), Peek O(1).
    # Space Complexity: O(N)
    
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()
        
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return max_val

    def _sift_up(self, index):
        parent = (index - 1) // 2
        # INVERSION: While node is LARGER than parent, swap
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _sift_down(self, index):
        n = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            # INVERSION: Find the LARGEST among parent and children
            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break

# Example usage
if __name__ == "__main__":
    h = MaxHeap()
    h.push(10)
    h.push(4)
    h.push(15)
    h.push(20)
    
    print("Popped (should be 20):", h.pop())
    print("Popped (should be 15):", h.pop())
    print("Current internal array state:", h.heap) # Expected: [10, 4]