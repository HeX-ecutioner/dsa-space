"""
Problem: Detect Linked List Cycle
Statement: Given head, the head of a linked list, determine if the linked list has a cycle in it.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    # Time Complexity: O(n) - Fast pointer reaches the end or laps the slow pointer.
    # Space Complexity: O(1) - Two pointers only.
    
    slow = head # Moves 1 step at a time
    fast = head # Moves 2 steps at a time
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        # If they meet, there is a cycle
        if slow == fast:
            return True
            
    return False # Fast reached the end, no cycle

# Example usage
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head # Create cycle
    print("Has Cycle:", hasCycle(head)) # Expected: True