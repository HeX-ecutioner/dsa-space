"""
Problem: Reverse Linked List II
Statement: Given the head of a singly linked list and two integers left and right, where left <= right,
           reverse the nodes of the list from position left to position right, and return the reversed list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    # Time Complexity: O(n) - Single pass through the list.
    # Space Complexity: O(1) - Constant extra space used.
    
    if not head or left == right:
        return head
        
    dummy = ListNode(0, head)
    prev = dummy
    
    # 1. Reach the node right before the 'left' position
    for _ in range(left - 1):
        prev = prev.next
        
    # 2. Start reversing
    curr = prev.next
    for _ in range(right - left):
        next_temp = curr.next
        curr.next = next_temp.next
        next_temp.next = prev.next
        prev.next = next_temp
        
    return dummy.next

# Example usage
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    rev = reverseBetween(head, 2, 4)
    
    res = []
    while rev:
        res.append(rev.val)
        rev = rev.next
    print("Reversed Between:", res) # Expected: [1, 4, 3, 2, 5]