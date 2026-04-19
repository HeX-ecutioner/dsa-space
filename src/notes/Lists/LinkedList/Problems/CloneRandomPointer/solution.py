"""
Problem: Copy List with Random Pointer
Statement: A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null. Return a deep copy of the list.
"""

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head):
    # Time Complexity: O(n) - We traverse the list a couple of times (O(3n) = O(n)).
    # Space Complexity: O(1) - We weave the new nodes into the original list temporarily.
    
    if not head:
        return None
        
    # 1. Weave copied nodes right next to original nodes: A -> A' -> B -> B'
    curr = head
    while curr:
        new_node = Node(curr.val, curr.next)
        curr.next = new_node
        curr = new_node.next
        
    # 2. Assign random pointers for the copied nodes
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
        
    # 3. Separate the woven list into original and deep copy
    curr = head
    copy_head = head.next
    while curr:
        copy_node = curr.next
        curr.next = copy_node.next
        if copy_node.next:
            copy_node.next = copy_node.next.next
        curr = curr.next
        
    return copy_head

# Example usage
if __name__ == "__main__":
    n1 = Node(7)
    n2 = Node(13)
    n3 = Node(11)
    
    n1.next = n2
    n2.next = n3
    n2.random = n1
    
    copied = copyRandomList(n1)
    
    print("Original first node val:", n1.val) # 7
    print("Copied first node val:", copied.val) # 7
    print("Copied second node's random points to val:", copied.next.random.val) # 7