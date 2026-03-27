"""
Problem: Flatten a Multilevel Doubly Linked List
Statement: You are given a doubly linked list where nodes also have a child pointer to a separate doubly linked list. Flatten the list so that all nodes appear in a single-level doubly linked list.
"""

# Specialized Node for Multilevel Doubly Linked List
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head):
    # Time Complexity: O(n) - We visit every node.
    # Space Complexity: O(1) - Iterative approach, modifying pointers directly.
    
    curr = head
    while curr:
        if curr.child:
            # Find the tail of the child branch
            tail = curr.child
            while tail.next:
                tail = tail.next
                
            # Connect tail to the next node in the main level
            tail.next = curr.next
            if curr.next:
                curr.next.prev = tail
                
            # Connect current node to the child branch
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None # Important: child must be set to null
            
        curr = curr.next
        
    return head

# Example usage
if __name__ == "__main__":
    # 1 <-> 2
    # |
    # 3
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    node1.next = node2
    node2.prev = node1
    node1.child = node3
    
    flat = flatten(node1)
    res = []
    while flat:
        res.append(flat.val)
        flat = flat.next
    print("Flattened List:", res) # Expected: [1, 3, 2]