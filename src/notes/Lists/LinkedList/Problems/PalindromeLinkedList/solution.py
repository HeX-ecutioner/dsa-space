"""
Problem: Palindrome Linked List
Statement: Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    # Time Complexity: O(n)
    # Space Complexity: O(1) - Modifies the list in place (reverses half).
    
    slow, fast = head, head
    
    # 1. Find middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    # 2. Reverse second half
    prev = None
    while slow:
        tmp = slow.next
        slow.next = prev
        prev = slow
        slow = tmp
        
    # 3. Check palindrome
    left, right = head, prev
    while right: # right will be shorter or equal
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
        
    return True

# Example usage
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    print("Is Palindrome:", isPalindrome(head)) # Expected: True