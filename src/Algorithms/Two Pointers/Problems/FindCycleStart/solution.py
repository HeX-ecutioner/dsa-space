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

# Example usage:
if __name__ == "__main__":
    # Creating a linked list with a cycle for testing
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates a cycle here

    cycle_start = detect_cycle_start(node1)
    if cycle_start:
        print(f"Cycle starts at node with value: {cycle_start.val}") # Output: Cycle starts at node with value: 2
    else:
        print("No cycle detected.")