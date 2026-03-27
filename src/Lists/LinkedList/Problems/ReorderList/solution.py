"""
Problem: Reorder List
Statement: You are given the head of a singly linked-list. Reorder it to: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    # Time Complexity: O(n) - Find middle, reverse half, merge halves.
    # Space Complexity: O(1) - No extra structures utilized.
    
    if not head or not head.next:
        return

    # 1. Find the middle
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 2. Reverse the second half
    second = slow.next
    slow.next = None # split lists
    prev = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp

    # 3. Merge the two halves alternatingly
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

# Example usage
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    reorderList(head)
    
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    print("Reordered List:", res) # Expected: [1, 4, 2, 3]