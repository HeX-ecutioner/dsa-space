"""
Problem: Middle of the Linked List
Statement: Given the head of a singly linked list, return the middle node. If there are two middle nodes, return the second middle node.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    # Time Complexity: O(n) - Single pass where fast moves at 2x speed.
    # Space Complexity: O(1)
    
    slow = head
    fast = head
    
    # When fast reaches the end, slow is exactly in the middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow

# Example usage
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    mid = middleNode(head)
    print("Middle Node Value:", mid.val) # Expected: 3