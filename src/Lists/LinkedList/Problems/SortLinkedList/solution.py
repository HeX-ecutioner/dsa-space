"""
Problem: Sort List
Statement: Given the head of a linked list, return the list after sorting it in ascending order (using Merge Sort).
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head):
    # Time Complexity: O(n log n) - Merge sort divides list in half log(n) times and merges in O(n).
    # Space Complexity: O(log n) - For the recursion stack.
    
    if not head or not head.next:
        return head
        
    # 1. Split the list into two halves using slow/fast pointers
    left = head
    right = getMid(head)
    tmp = right.next
    right.next = None
    right = tmp
    
    # 2. Sort both halves
    left = sortList(left)
    right = sortList(right)
    
    # 3. Merge sorted halves
    return merge(left, right)

def getMid(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next

# Example usage
if __name__ == "__main__":
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    sorted_head = sortList(head)
    
    res = []
    while sorted_head:
        res.append(sorted_head.val)
        sorted_head = sorted_head.next
    print("Sorted List:", res) # Expected: [1, 2, 3, 4]