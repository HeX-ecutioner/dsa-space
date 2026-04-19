# Problem: Given singly linked list, return True if cycle exists (Floyd's Tortoise and Hare)
from typing import Optional

class ListNode: # We implement a minimal ListNode type for demonstration
    def __init__(self, val=0, nxt: Optional['ListNode']=None):
        self.val = val
        self.next = nxt

def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Use slow and fast pointers:
    - slow moves 1 step, fast moves 2 steps
    - if fast meets slow -> cycle exists
    - if fast reaches None -> no cycle
    Time: O(n), Space: O(1)
    """
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Example usage:
if __name__ == "__main__":
    # Create a linked list with a cycle for testing
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates a cycle here

    print(has_cycle(node1))  # Output: True

    # Create a linked list without a cycle for testing
    nodeA = ListNode(1)
    nodeB = ListNode(2)
    
    nodeA.next = nodeB

    print(has_cycle(nodeA))  # Output: False