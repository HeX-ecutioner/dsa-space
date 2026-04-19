"""
Problem: Manual Min Heap Implementation
Statement: Implement an array-based Min Heap with push and pop operations, demonstrating sift-up and sift-down mechanics.
"""

class MinHeap:
    # Time Complexity: Push O(log N), Pop O(log N), Peek O(1).
    # Space Complexity: O(N) to store the array.
    
    def __init__(self):
        self.heap = []

    def push(self, val):
        # Add to the very end, then bubble it up to its correct position
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0: return None
        if len(self.heap) == 1: return self.heap.pop()
        
        # Swap the root (minimum) with the last element
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        
        # Bubble the new root down to its correct position
        self._sift_down(0)
        return min_val

    def _sift_up(self, index):
        parent = (index - 1) // 2
        # While the node is smaller than its parent, swap them
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _sift_down(self, index):
        n = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            # Find the absolute smallest among parent and its two children
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break # It's in the right place

# Example usage
if __name__ == "__main__":
    h = MinHeap()
    h.push(10)
    h.push(4)
    h.push(15)
    h.push(1)
    
    print("Popped (should be 1):", h.pop())
    print("Popped (should be 4):", h.pop())
    print("Current internal array state:", h.heap) # Expected: [10, 15]