# Detect Cycle in Linked List (Floyd's Tortoise and Hare)
# Problem: Given singly linked list, return True if cycle exists.
# Note: We implement a minimal ListNode type for demonstration.
from typing import Optional

class ListNode:
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

# Example usage: create nodes and connect tail to a mid node to test cycle detection.
