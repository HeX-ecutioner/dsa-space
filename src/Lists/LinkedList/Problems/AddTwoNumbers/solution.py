"""
Problem: Add Two Numbers
Statement: You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    # Time Complexity: O(max(m, n)) - We iterate up to the longest list length.
    # Space Complexity: O(max(m, n)) - The new list will be at most max(m,n) + 1 nodes long.
    
    dummy = ListNode()
    curr = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Calculate new digit and carry
        total = val1 + val2 + carry
        carry = total // 10
        curr.next = ListNode(total % 10)
        
        # Move pointers
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        
    return dummy.next

# Example usage
if __name__ == "__main__":
    # 342 + 465 = 807 (represented as 2->4->3 + 5->6->4)
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    
    result = addTwoNumbers(l1, l2)
    res = []
    while result:
        res.append(result.val)
        result = result.next
    print("Added Lists:", res) # Expected: [7, 0, 8]