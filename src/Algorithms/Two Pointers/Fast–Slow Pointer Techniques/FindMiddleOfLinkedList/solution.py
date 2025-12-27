# Find Middle of Linked List (fast-slow)
from typing import Optional

class ListNode:
    def __init__(self, val=0, nxt: Optional['ListNode']=None):
        self.val = val
        self.next = nxt

def find_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Use slow and fast:
    - slow moves 1, fast moves 2
    - when fast reaches end, slow is at middle
    For even length, this returns the second middle (common convention).
    Time: O(n), Space: O(1)
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
