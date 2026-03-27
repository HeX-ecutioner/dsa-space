"""
Problem: Partition List
Statement: Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x. Maintain original relative order.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    # Time Complexity: O(n) - Single pass.
    # Space Complexity: O(1) - Rearranging existing nodes.
    
    # Create two dummy heads to hold the two partitions
    left_dummy = ListNode(0)
    right_dummy = ListNode(0)
    
    left_tail = left_dummy
    right_tail = right_dummy
    
    curr = head
    while curr:
        if curr.val < x:
            left_tail.next = curr
            left_tail = left_tail.next
        else:
            right_tail.next = curr
            right_tail = right_tail.next
        curr = curr.next
        
    # Combine the two partitions
    left_tail.next = right_dummy.next
    right_tail.next = None # End the right list to prevent cycles
    
    return left_dummy.next

# Example usage
if __name__ == "__main__":
    head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
    partitioned = partition(head, 3)
    
    res = []
    while partitioned:
        res.append(partitioned.val)
        partitioned = partitioned.next
    print("Partitioned List:", res) # Expected: [1, 2, 2, 4, 3, 5]