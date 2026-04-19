"""
Problem: Remove Loop in Linked List
Statement: Given a linked list with a loop, remove the loop by un-linking the last node.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeCycle(head):
    # Time Complexity: O(n) - Single traversal to find and remove.
    # Space Complexity: O(1)
    
    slow = fast = head
    has_cycle = False
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
            
    if not has_cycle:
        return head
        
    # Find start of cycle
    slow = head
    if slow == fast:
        # Edge case: Cycle starts at the head
        while fast.next != slow:
            fast = fast.next
    else:
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
            
    # Break the cycle
    fast.next = None
    return head

# Example usage
if __name__ == "__main__":
    head = ListNode(1)
    two = ListNode(2)
    three = ListNode(3)
    head.next = two
    two.next = three
    three.next = two # Cycle back to 2
    
    removeCycle(head)
    
    # Prove cycle is broken by safely iterating
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    print("List after removing cycle:", res) # Expected: [1, 2, 3]