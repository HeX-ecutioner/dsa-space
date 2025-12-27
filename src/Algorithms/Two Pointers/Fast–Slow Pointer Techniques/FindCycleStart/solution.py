# Find Cycle Start in Linked List
# Problem: If cycle exists, return node where cycle begins (ListNode).
from typing import Optional

class ListNode:
    def __init__(self, val=0, nxt: Optional['ListNode']=None):
        self.val = val
        self.next = nxt

def detect_cycle_start(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Floyd's algorithm:
    1. Detect cycle using slow/fast.
    2. If found, set one pointer to head, keep other at meeting point.
       Move both one step at a time; the node where they meet is the cycle start.
    Explanation:
    - Let L be distance from head to cycle start, C be cycle length, x be distance from cycle start to meeting point.
    - After meeting, moving both pointers L steps brings them to cycle start.
    Time: O(n), Space: O(1)
    """
    slow = fast = head
    # detect
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # found meeting point
            ptr1 = head
            ptr2 = slow
            while ptr1 != ptr2:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            return ptr1
    return None
