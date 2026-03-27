"""
Problem: Rotate List
Statement: Given the head of a linked list, rotate the list to the right by k places.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    # Time Complexity: O(n) - One pass to find length, another partial pass to break ring.
    # Space Complexity: O(1) - Pointers only.
    
    if not head or not head.next or k == 0:
        return head
        
    # 1. Find length and the last node
    length = 1
    old_tail = head
    while old_tail.next:
        old_tail = old_tail.next
        length += 1
        
    # 2. Connect tail to head to form a circle
    old_tail.next = head
    
    # 3. Find the new tail: (length - k % length - 1)th node
    k = k % length
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next
        
    # 4. Break the circle
    new_head = new_tail.next
    new_tail.next = None
    
    return new_head

# Example usage
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    rotated = rotateRight(head, 2)
    
    res = []
    while rotated:
        res.append(rotated.val)
        rotated = rotated.next
    print("Rotated List:", res) # Expected: [4, 5, 1, 2, 3]