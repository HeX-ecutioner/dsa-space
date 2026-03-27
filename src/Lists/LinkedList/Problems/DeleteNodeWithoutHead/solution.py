"""
Problem: Delete Node in a Linked List
Statement: Given a reference to a node to be deleted in a singly-linked list, delete it. You will not be given access to the head of the list, only the node to be deleted.
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(node):
    # Time Complexity: O(1) - We simply copy the next node's data and skip it.
    # Space Complexity: O(1)
    
    """
    Since we don't have the previous node, we can't do prev.next = node.next.
    Instead, we copy the value of the NEXT node into the CURRENT node,
    and then we delete the NEXT node.
    """
    node.val = node.next.val
    node.next = node.next.next

# Example usage
if __name__ == "__main__":
    head = ListNode(4)
    del_node = ListNode(5)
    tail = ListNode(1)
    
    head.next = del_node
    del_node.next = tail
    
    deleteNode(del_node)
    
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    print("List after deletion:", res) # Expected: [4, 1]