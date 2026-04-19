from typing import Optional

class ListNode:
    def __init__(self, val=0, nxt: Optional['ListNode']=None):
        self.val = val
        self.next = nxt

def check(head: Optional[ListNode]) -> bool:
    """
    Steps:
    1. Use fast/slow to find middle (slow will be at middle).
    2. Reverse second half in-place.
    3. Compare first half and reversed second half node-by-node.
    4. (Optional) Restore list by reversing second half again.
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return True

    # find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse second half starting at slow
    prev = None
    curr = slow
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # compare head.. and prev.. (prev is head of reversed second half)
    p1, p2 = head, prev
    result = True
    while p2:
        if p1.val != p2.val:
            result = False
            break
        p1 = p1.next
        p2 = p2.next

    # (Optional) restore second half - omitted to keep code concise.
    return result

def build_list(values):
    head = None
    current = None
    for v in values:
        node = ListNode(v)
        if not head:
            head = node
            current = node
        else:
            current.next = node
            current = node
    return head

# Example usage:
head1 = build_list([1, 2, 3, 2, 1])
print(check(head1))  # Output: True
head2 = build_list([1, 2, 3, 4])
print(check(head2))  # Output: False
head3 = build_list([7])
print(check(head3))  # Output: True
print(check(None))   # Output: True