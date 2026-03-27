"""
Problem: Linked List Cycle II
Statement: Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head):
    # Time Complexity: O(n) - Traverses nodes linearly.
    # Space Complexity: O(1) - Floyd's Tortoise and Hare algorithm uses no extra memory.
    
    slow = head
    fast = head
    
    # 1. Find intersection point using fast/slow pointers
    intersection = None
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            intersection = slow
            break
            
    if not intersection:
        return None # No cycle
        
    # 2. Find the entrance to the cycle
    # Distance from head to cycle entrance == distance from intersection to cycle entrance
    slow = head
    while slow != intersection:
        slow = slow.next
        intersection = intersection.next
        
    return slow

# Example usage
if __name__ == "__main__":
    head = ListNode(3)
    cycle_start = ListNode(2)
    head.next = cycle_start
    cycle_start.next = ListNode(0)
    cycle_start.next.next = ListNode(-4)
    cycle_start.next.next.next = cycle_start # Loops back to 2
    
    start_node = detectCycle(head)
    print("Cycle starts at node with value:", start_node.val) # Expected: 2