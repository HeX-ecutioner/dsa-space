"""
Problem: Swap Nodes in Pairs
Statement: Given a linked list, swap every two adjacent nodes and return its head.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    # Time Complexity: O(n) - Traverse the list once.
    # Space Complexity: O(1) - Iterative approach uses constant space.
    
    dummy = ListNode(0, head)
    prev = dummy
    curr = head
    
    while curr and curr.next:
        # Identify the two nodes to swap
        first = curr
        second = curr.next
        
        # Swapping logic
        prev.next = second
        first.next = second.next
        second.next = first
        
        # Move pointers forward for the next pair
        prev = first
        curr = first.next
        
    return dummy.next

# Example usage
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    swapped = swapPairs(head)
    
    res = []
    while swapped:
        res.append(swapped.val)
        swapped = swapped.next
    print("Swapped Pairs:", res) # Expected: [2, 1, 4, 3]