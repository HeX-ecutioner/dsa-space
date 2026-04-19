"""
Problem: Reverse Nodes in k-Group
Statement: Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    # Time Complexity: O(n) - We traverse the list to count and then to reverse.
    # Space Complexity: O(1) - Pointers only.
    
    # Helper function to count the remaining nodes
    def get_length(node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    length = get_length(head)
    dummy = ListNode(0, head)
    prev_group_end = dummy
    
    # Only reverse if we have at least k nodes left
    while length >= k:
        curr = prev_group_end.next
        next_node = curr.next
        
        # Reverse k nodes
        for _ in range(1, k):
            curr.next = next_node.next
            next_node.next = prev_group_end.next
            prev_group_end.next = next_node
            next_node = curr.next
            
        prev_group_end = curr
        length -= k
        
    return dummy.next

# Example usage
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    new_head = reverseKGroup(head, 2)
    
    res = []
    while new_head:
        res.append(new_head.val)
        new_head = new_head.next
    print("Reversed in K groups:", res) # Expected: [2, 1, 4, 3, 5]