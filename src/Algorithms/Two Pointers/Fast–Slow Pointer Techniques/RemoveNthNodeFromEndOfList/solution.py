# Remove N-th Node From End of List (two-pointer gap method)
from typing import Optional

class ListNode:
    def __init__(self, val=0, nxt: Optional['ListNode']=None):
        self.val = val
        self.next = nxt

def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Use dummy node to handle head removal.
    - Set fast ahead by n steps.
    - Then move both fast and slow until fast reaches end.
    - slow.next is the node to remove.
    Time: O(n), Space: O(1)
    """
    dummy = ListNode(0, head)
    fast = slow = dummy
    # advance fast by n+1 to keep gap
    for _ in range(n+1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    # remove slow.next
    slow.next = slow.next.next
    return dummy.next
