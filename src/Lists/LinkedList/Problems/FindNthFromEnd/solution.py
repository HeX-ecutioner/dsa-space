"""
Problem: Find Nth Node From End of List
Statement: Given a linked list, return the value of the nth node from the end of the list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findNthFromEnd(head, n):
    # Time Complexity: O(L) - Where L is list length. One pass.
    # Space Complexity: O(1)
    
    fast = head
    slow = head
    
    # Give fast pointer a head start of n steps
    for _ in range(n):
        if not fast:
            return None # n is greater than list length
        fast = fast.next
        
    # Move both until fast hits the end
    while fast:
        slow = slow.next
        fast = fast.next
        
    return slow.val

# Example usage
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    nth_val = findNthFromEnd(head, 2)
    print("2nd from end:", nth_val) # Expected: 4