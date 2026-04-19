"""
Problem: Fibonacci Heap Architecture
Statement: Demonstrate the Circular Doubly-Linked List node structure that allows O(1) insertions and merges.
"""

class FibNode:
    def __init__(self, val):
        self.val = val
        self.degree = 0
        self.parent = None
        self.child = None
        self.mark = False
        
        # O(1) insertion relies on a Circular Doubly Linked List!
        self.left = self  
        self.right = self 

class FibonacciHeapConceptual:
    def __init__(self):
        self.min_node = None
        self.total_nodes = 0

    def insert(self, val):
        """ O(1) Lazy Insertion: Just dump it into the root list! """
        new_node = FibNode(val)
        
        if not self.min_node:
            self.min_node = new_node
        else:
            # Insert new_node into the circular doubly linked list next to min_node
            new_node.right = self.min_node.right
            new_node.left = self.min_node
            self.min_node.right.left = new_node
            self.min_node.right = new_node
            
            # Update min_node if necessary
            if val < self.min_node.val:
                self.min_node = new_node
                
        self.total_nodes += 1
        return new_node

    def get_min(self):
        """ O(1) Peek """
        return self.min_node.val if self.min_node else None

# Example usage
if __name__ == "__main__":
    fib_heap = FibonacciHeapConceptual()
    
    # O(1) insertions! No bubbling up, no tree rotations. Just linking pointers.
    fib_heap.insert(20)
    fib_heap.insert(5)
    fib_heap.insert(15)
    
    print("Minimum element in Fibonacci Heap:", fib_heap.get_min()) # Expected: 5