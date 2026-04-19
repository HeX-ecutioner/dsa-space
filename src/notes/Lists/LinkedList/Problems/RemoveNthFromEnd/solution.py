"""
Problem: Remove Nth Node From End of List
Statement: Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    # Time Complexity: O(L) - One pass.
    # Space Complexity: O(1)
    
    dummy = ListNode(0, head)
    slow = dummy
    fast = dummy
    
    # Advance fast by n+1 steps so slow is right before the deletion target
    for _ in range(n + 1):
        fast = fast.next
        
    while fast:
        slow = slow.next
        fast = fast.next
        
    # Skip the nth node
    slow.next = slow.next.next
    
    return dummy.next

# Example usage
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    new_head = removeNthFromEnd(head, 2)
    
    res = []
    while new_head:
        res.append(new_head.val)
        new_head = new_head.next
    print("After Removal:", res) # Expected: [1, 2, 3, 5]